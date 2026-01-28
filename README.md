🚀 RAG-Based Question Answering System

A production-style Retrieval-Augmented Generation (RAG) system that allows users to upload documents (PDF/TXT) and ask intelligent questions grounded in document content.

This project demonstrates applied AI engineering, combining vector search, LLM reasoning, API design, background processing, rate limiting, performance metrics, and a client-facing UI.

🎯 Built to showcase real-world AI system design — not just a demo model.

🧠 Key Highlights

✅ Full RAG pipeline (Upload → Chunk → Embed → Retrieve → Generate)
✅ FastAPI backend with clean API architecture
✅ FAISS vector store for scalable similarity search
✅ LLM-powered answer generation
✅ Background ingestion jobs for performance
✅ Rate limiting to prevent API abuse
✅ Metrics tracking (retrieval time, generation latency, similarity)
✅ Confidence scoring & explainability
✅ Streamlit frontend (real product UI — not Swagger-only)
✅ Resume & document analysis demo use case
✅ Designed for internship-level evaluation & real-world relevance

📌 Problem Solved

Most QA systems hallucinate or answer without grounding.

This system ensures:

➢ Answers are based only on retrieved document content

➢ Retrieval quality is measured & optimized

➢ Latency and performance are monitored

➢ Users can see confidence & source relevance

🏗️ System Architecture

User Uploads Document
        ↓
Text Chunking (Context-Preserving)
        ↓
Embedding Generation
        ↓
Vector Storage (FAISS)
        ↓
Query Embedding + Similarity Search
        ↓
Relevant Chunk Retrieval
        ↓
LLM Answer Generation
        ↓
Answer + Confidence + Metrics + Citations

📂 Project Structure

📁 rag_project/
│
├── app/
│   ├── main.py          # FastAPI API Server
│   ├── ingestion.py     # Document chunking & embedding
│   ├── retriever.py     # Similarity search (FAISS)
│   ├── generator.py     # LLM answer generation
│   └── vector_store.py  # Vector database logic
│
├── frontend.py          # Streamlit user interface
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
└── EXPLANATION.md       # Technical deep-dive


⚙️ Tech Stack
Backend: FastAPI, Python
Frontend: Streamlit
Embeddings: Sentence Transformers (MiniLM)
Vector Database: FAISS
LLM Providers: Groq / OpenAI / LLaMA
Retrieval: Semantic Search + Ranking
Rate Limiting: SlowAPI
Deployment Ready: Docker / Cloud Ready

🚀 Features

📤 Document Ingestion

➢ Accepts PDF & TXT

➢ Chunking with overlap for better retrieval

➢ Runs in background tasks to avoid API blocking

🔍 Retrieval & Search

➢ Vector-based similarity search using FAISS

➢ Retrieves top relevant chunks

➢ Handles retrieval edge cases

🤖 Answer Generation

➢ LLM answers using ONLY retrieved content

➢ Reduces hallucination risk

➢ Produces grounded, explainable responses

📊 Metrics & Observability

Tracks:

➢ Retrieval latency (ms)

➢ Generation latency (ms)

➢ Similarity scores

➢ Confidence score

🚫 Rate Limiting

Prevents abuse:

Endpoint                                 	Limit
/upload	                               3 requests/min
/ask	                               5 requests/min

▶️ How to Run the Project
1️⃣ Install Dependencies

➢ pip install -r requirements.txt

2️⃣ Start Backend (FastAPI)

➢ python -m uvicorn app.main:app --reload


Open API Docs:

http://127.0.0.1:8000/docs

3️⃣ Start Frontend (Streamlit)
python -m streamlit run frontend.py


Open UI:

http://localhost:8501


🧪 Example Queries

Try asking:

➢ Summarize this document

➢ What skills does this resume show?

➢ Evaluate this candidate for an AI role

➢ List key projects mentioned

➢ Generate interview questions based on this resume

📉 Known Retrieval Failure Case (Honest Engineering Insight)

A failure occurs when:

➢ Questions are too vague

➢ Multiple chunks contain similar keywords

Example:

A question about projects retrieved a chunk about education

This highlights the importance of:

➢ Chunk boundary tuning

➢ Query specificity

➢ Embedding precision

We improved retrieval by adding chunk overlap & ranking filters.

📏 Chunk Size Decision

Chunk size: ~500–700 characters

Reason:

➢ Too small → loses semantic meaning

➢ Too large → reduces retrieval precision

This balance provides:
✔ Context completeness
✔ Better similarity accuracy
✔ Efficient vector search

📊 Metric Tracked

We tracked Retrieval Latency (ms)

Why:

➢ Measures vector search performance

➢ Ensures fast real-time responses

➢ Important for scalable AI systems

Average observed latency:

30–70 ms (FAISS-based retrieval)

💡 Real-World Use Cases

➢ Resume & candidate analysis

➢ Research paper Q&A

➢ Legal & policy document assistant

➢ Study material tutor

➢ Enterprise knowledge base search

🏆 Why This Project Makes High Impact

This project proves ability in:

✔ Applied AI & ML
✔ Backend API engineering
✔ Vector databases
✔ LLM integration
✔ Performance optimization
✔ Explainable AI
✔ Real product UI design
✔ Production-level system thinking


👨‍💻 Author

Satyam Shinde
Final-Year Computer Science Student
Specialization: Artificial Intelligence & Machine Learning
