from fastapi import FastAPI
from modules.ai_agent.router import ai_agent_router

# Import Routers
from modules.ai_agent.router import ai_agent_router

app = FastAPI()
app.include_router(
    ai_agent_router,
    tags=["AI Modules"]
)

app.include_router(
    ai_agent_router,
    tags=["AI Module"]
)


@app.get("/",status_code=200)
async def root():
<<<<<<< HEAD
    return {"message": "Hello World"}
=======
    return {
        "message":  "Your at the Xander's Backend"
    }

   
>>>>>>> fd96dbd0b84e69ed02a7bd817072e7414bcc5eb6
