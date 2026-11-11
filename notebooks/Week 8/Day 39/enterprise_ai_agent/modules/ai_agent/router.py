from fastapi import APIRouter
from.schema import chat_payload

ai_agent_router = APIRouter(prefix="/ai")

@ai_agent_router.post("/chat")
def initiate_chat(query: chat_payload):
    print(query.model_dump())
    return query

@ai_agent_router.get("/history")
def get_history(sessionn_id : str):
    print("sessionn id has been recieved")

    #todo
    #define service/login

    return f"Here is the chat for {sessionn_id} session"
