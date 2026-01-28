import streamlit as st
import requests
import time

# --- Configuration ---
API_URL = "http://127.0.0.1:8000"  # Your FastAPI backend URL

# --- Page Config ---
st.set_page_config(
    page_title="Cited RAG Assistant",
    page_icon="📚",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
.stChatInput {border-radius: 20px;}
.reportview-container {background: #f0f2f6;}
.sidebar .sidebar-content {background: #ffffff;}
div[data-testid="stMetricValue"] {font-size: 1.2rem;}
</style>
""", unsafe_allow_html=True)

# --- Sidebar: Document Upload ---
with st.sidebar:
    st.title("📂 Document Hub")
    st.write("Upload your PDF or TXT to start analysis.")
    
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt"])
    
    if uploaded_file is not None:
        if st.button("Process Document", type="primary"):
            with st.spinner("Chunking & Embedding..."):
                files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                try:
                    response = requests.post(f"{API_URL}/upload", files=files)

                    if response.status_code == 200:
                        st.success("✅ Indexing Complete!")
                    elif response.status_code == 429:
                        st.error("⚠️ Rate Limit Hit! Wait a moment.")
                    else:
                        st.error(f"Error: {response.text}")

                except Exception as e:
                    st.error(f"Connection Error: {e}")

    st.divider()
    st.markdown("### 📊 System Stack")
    st.info("""
Backend: FastAPI  
Vector DB: FAISS  
Embeddings: MiniLM-L6  
LLM: Llama-3  
Pipeline: Custom RAG  
""")

# --- Main Chat Interface ---
st.title("🤖 Cited RAG Assistant")
st.caption("Ask questions based on uploaded documents. Answers include confidence & retrieval metrics.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        if "metrics" in msg:
            cols = st.columns(3)
            cols[0].metric("Confidence", f"{msg['metrics']['confidence']:.2f}")
            cols[1].metric("Retrieval Time", f"{msg['metrics']['retrieval_ms']:.0f} ms")
            cols[2].metric("Generation Time", f"{msg['metrics']['gen_ms']:.0f} ms")

            if msg["metrics"]["sources"]:
                with st.expander("📚 View Sources"):
                    for s in msg["metrics"]["sources"]:
                        st.markdown(f"- {s}")

# --- Chat Input ---
if prompt := st.chat_input("Ask something about your document..."):

    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call backend API
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("Thinking...")

        try:
            response = requests.post(f"{API_URL}/ask", params={"question": prompt})

            if response.status_code == 200:
                data = response.json()

                # ✅ Correct parsing from backend response
                payload = data.get("answer", {})

                answer = payload.get("answer", "No answer returned.")
                confidence = payload.get("confidence", 0.0)
                metrics = payload.get("metrics", {})

                ret_time = metrics.get("retrieval_time_ms", 0)
                gen_time = metrics.get("generation_time_ms", 0)
                sources = payload.get("sources", [])

                # Show answer
                placeholder.markdown(answer)

                # Show metrics
                cols = st.columns(3)
                cols[0].metric("Confidence", f"{confidence:.2f}")
                cols[1].metric("Retrieval Time", f"{ret_time:.0f} ms")
                cols[2].metric("Generation Time", f"{gen_time:.0f} ms")

                # Show sources
                if sources:
                    with st.expander("📚 View Sources"):
                        for src in sources:
                            st.markdown(f"- {src}")

                # Save history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "metrics": {
                        "confidence": confidence,
                        "retrieval_ms": ret_time,
                        "gen_ms": gen_time,
                        "sources": sources
                    }
                })

            elif response.status_code == 429:
                placeholder.error("⏳ Too many requests — wait a moment.")
            else:
                placeholder.error(f"Server Error: {response.text}")

        except Exception as e:
            placeholder.error(f"Connection Failed: {e}")
