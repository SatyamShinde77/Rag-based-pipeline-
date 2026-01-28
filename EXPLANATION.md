1️⃣ Why We Chose This Chunk Size

We selected a chunk size of approximately 500–700 characters with a small overlap between chunks.

Reasoning:

Smaller chunks increase precision but may lose full context

Larger chunks preserve context but reduce retrieval accuracy

This chunk size provides a balanced trade-off:

Retains enough semantic meaning for embeddings

Improves similarity matching during retrieval

Prevents context fragmentation

Optimizes performance by limiting vector size

Result:

This strategy improves answer relevance while maintaining fast retrieval latency.

2️⃣ One Retrieval Failure Case Observed
Failure Case:

When the user asked a broad or ambiguous question, the retriever sometimes returned semantically similar but contextually incorrect chunks.

Example:

A query about projects retrieved a chunk about education, due to overlapping keywords.

Root Cause:

Overlapping vocabulary across different document sections

Limited context separation in long documents

Learning & Mitigation:

Improved chunk overlap strategy

Adjusted similarity ranking

Encouraged clearer query phrasing

This highlights a real-world limitation of embedding-based retrieval systems.

3️⃣ One Metric We Tracked

We tracked Retrieval Latency (milliseconds) to evaluate system efficiency.

Why This Metric:

Measures how quickly relevant chunks are retrieved

Indicates FAISS vector search performance

Critical for real-time user experience

Observations:

Average retrieval time: 30–70 ms

Performance remained stable even with multiple documents

We also tracked LLM generation time to monitor response speed.

📌 Additional Engineering Considerations

This system demonstrates:

Retrieval-Augmented Generation pipeline design

Real-world API engineering

Background job processing

Rate limiting for stability

Explainable AI via similarity scores

Observability using performance metrics

🎯 Summary

This project balances accuracy, performance, explainability, and scalability.

It demonstrates the ability to:
✔ Design real AI systems
✔ Handle retrieval edge cases
✔ Measure system performance
✔ Build production-style APIs
✔ Explain engineering trade-offs clearly