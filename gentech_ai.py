from fastapi import FastAPI, Request
from pydantic import BaseModel
from azure_openai_client import test_chat, test_embedding

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to GenTech AI — powered by Azure OpenAI"}

@app.post("/ask")
async def ask_ai(request: QueryRequest):
    try:
        response = test_chat(request.query)
        return {
            "response": response.choices[0].message.content
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/embed")
async def get_embedding(request: QueryRequest):
    try:
        response = test_embedding(request.query)
        embedding = response.data[0].embedding
        return {
            "embedding_sample": embedding[:5],
            "embedding_dim": len(embedding)
        }
    except Exception as e:
        return {"error": str(e)}
