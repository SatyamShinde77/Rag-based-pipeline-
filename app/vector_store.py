import faiss
import numpy as np

dimension = 384  
index = faiss.IndexFlatL2(dimension)

documents = []

def store_embeddings(chunks, embeddings):
    global documents
    documents.extend(chunks)
    index.add(np.array(embeddings).astype("float32"))

    print("Embeddings stored in vector database!")
