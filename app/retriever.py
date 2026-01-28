from sentence_transformers import SentenceTransformer
import numpy as np
from app.vector_store import index, documents
import time

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query, k=3):
    if len(documents) == 0:
        return [], []

    start = time.time()
    query_vec = model.encode([query])

    distances, ids = index.search(np.array(query_vec).astype("float32"), k)

    chunks = []
    scores = []

    for i, d in zip(ids[0], distances[0]):
        if i < len(documents):
            chunks.append(documents[i])
            scores.append(float(d))

    retrieval_time_ms = (time.time() - start) * 1000

    return chunks, scores, retrieval_time_ms
