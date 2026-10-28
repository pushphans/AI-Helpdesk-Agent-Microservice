from ai_helpdesk_agent_microservice.utils.enums import TicketPriority
from ai_helpdesk_agent_microservice.utils.enums import TicketStatus
from typing import TypedDict



class AgentState(TypedDict):
    # Ticket data
    title : str
    description : str
    status : TicketStatus
    priority : TicketPriority

    # Ticket analyzer
    category : str | None
    suggested_priority : TicketPriority | None
    summary : str | None

    # Find policy
    support_policy : str | None

    # suggested reply
    suggested_reply : str | None


