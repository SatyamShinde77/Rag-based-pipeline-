from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from app.vector_store import store_embeddings

model = SentenceTransformer("all-MiniLM-L6-v2")

CHUNK_SIZE = 300  

def chunk_text(text):
    words = text.split()
    return [" ".join(words[i:i+CHUNK_SIZE]) for i in range(0, len(words), CHUNK_SIZE)]

def process_document(file):
    text = ""

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        for page in reader.pages:
            text += page.extract_text()
    else:
        text = file.file.read().decode()

    chunks = chunk_text(text)

    embeddings = model.encode(chunks)

    store_embeddings(chunks, embeddings)

    print("Document loaded successfully!")
    print("Total chunks created:", len(chunks))
    print("Embeddings generated and saved!")
