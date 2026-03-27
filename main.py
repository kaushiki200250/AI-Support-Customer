from Database.db import save_chat, get_chats
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
def chat(request: ChatRequest):
    user_input = request.query.lower()

    if "hello" in user_input:
        reply = "Hello Kaushiki ! 😊"
    elif "loan" in user_input:
        reply = "We offer loans."
    elif "card" in user_input:
        reply = "We provide cards."
    else:
        reply = "Sorry, I didn’t understand."

    try:
        save_chat(request.query, reply)
    except Exception as e:
        print("DB Error:", e)

    return {
        "user_query": request.query,
        "ai_response": reply
    }
@app.get("/history")
def get_history():
    chats = get_chats()
    return {"chats": chats}