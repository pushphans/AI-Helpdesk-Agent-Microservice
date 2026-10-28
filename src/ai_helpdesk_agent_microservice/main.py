from ai_helpdesk_agent_microservice.router.triage_router import triage_router
from fastapi import FastAPI


app = FastAPI()


app.include_router(triage_router)


@app.get("/")
def health():
    return {
        "status" : "ok"
    }