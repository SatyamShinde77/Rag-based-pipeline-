from fastapi import FastAPI, UploadFile, BackgroundTasks, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

from app.ingestion import process_document
from app.generator import answer_query

app = FastAPI()

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests. Please slow down."}
    )

@app.get("/")
def home():
    return {"message": "RAG API Running Successfully"}

# Upload endpoint with rate limit
@app.post("/upload")
@limiter.limit("3/minute")
async def upload_document(
    request: Request,
    file: UploadFile,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(process_document, file)
    return {"message": "Document uploaded. Processing started."}

# Ask question endpoint with rate limit
@app.post("/ask")
@limiter.limit("5/minute")
async def ask_question(request: Request, question: str):
    answer = answer_query(question)
    return {"answer": answer}
