import numpy as np
import os
from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq

router = APIRouter()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

model = None
index= None
chunks = None

class ChatRequest(BaseModel):
    query: str

def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def get_index():
    global index, chunks

    if index is not None:
        return index, chunks

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    RULES_PATH = os.path.join(BASE_DIR, "services", "rules.txt")

    with open(RULES_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

    model = get_model()
    embeddings = model.encode(chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index, chunks  

def retrieve_context(query, top_k=3):
    index, chunks = get_index()
    model = get_model()
    q_emb = model.encode([query])

    D, I = index.search(np.array(q_emb), top_k)

    results = []
    for idx in I[0]:
        results.append(chunks[idx])

    return "\n".join(results)



def generate_answer(query, context):
    prompt = f"""
You are the official assistant for an Inter-College Technical Fest.

Your job:
- Answer ONLY using the context provided 
- Answer the question clearly  
- Do not confuse yourself
- Do NOT invent information
- If answer not in context → say:
  "Please contact the event coordinator for this information."

Instructions:
- Be short and specific
- Use bullet points if needed
- Mention rules clearly
- Mention team size if relevant
- Mention time/venue if asked


Context:
{context}

Question:
{query}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return completion.choices[0].message.content


def rag_chat(query):
    context = retrieve_context(query)
    answer = generate_answer(query, context)
    return answer


@router.post("/chat")
def chat_api(req: ChatRequest):
    answer = rag_chat(req.query)
    return {"answer": answer}
