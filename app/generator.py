from groq import Groq
from app.retriever import retrieve_chunks
import time

client = Groq(api_key="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")

def answer_query(question):
    chunks, scores, retrieval_time = retrieve_chunks(question)

    if len(chunks) == 0:
        return {
            "answer": "No relevant document content found.",
            "confidence": 0.0,
            "metrics": {"retrieval_time_ms": retrieval_time}
        }

    context = "\n".join(chunks)

    prompt = f"""
Answer ONLY using the document context below:

{context}

Question: {question}
Answer clearly:
"""

    start_gen = time.time()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    generation_time_ms = (time.time() - start_gen) * 1000

    answer = response.choices[0].message.content

    confidence = round(1 / (1 + sum(scores)), 3)

    return {
        "answer": answer,
        "confidence": confidence,
        "similarity_scores": scores,
        "metrics": {
            "retrieval_time_ms": retrieval_time,
            "generation_time_ms": generation_time_ms
        }
    }













