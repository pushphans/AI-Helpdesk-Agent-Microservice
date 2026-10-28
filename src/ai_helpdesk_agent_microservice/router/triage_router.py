from ai_helpdesk_agent_microservice.utils.auth_utils import check_service_auth
from fastapi import Depends
from ai_helpdesk_agent_microservice.service.triage_service import run_workflow
from ai_helpdesk_agent_microservice.schema.triage_schemas import TriageAgentRequestSchema
from fastapi import APIRouter, HTTPException

triage_router = APIRouter(prefix="/ai", tags=["AI"])

@triage_router.post("/tickets-analyze")
async def execute_run_workflow(
    data : TriageAgentRequestSchema,
    service_token : bool | None = Depends(check_service_auth)
):
    result = await run_workflow(data=data)
    return result