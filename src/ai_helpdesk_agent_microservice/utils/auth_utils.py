import jwt
import hmac
from ai_helpdesk_agent_microservice.core.config import settings
from fastapi import Depends
from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


service_security = HTTPBearer(auto_error=False)



async def check_service_auth(
    credentials : HTTPAuthorizationCredentials | None = Depends(service_security)
) -> bool:

    if credentials is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid token"
        )

    recieved_token = credentials.credentials
    expected_token = settings.SERVICE_ACTIVATION_TOKEN

    service_token_valid = hmac.compare_digest(recieved_token, expected_token)

    if not service_token_valid:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid token"
        )

    return True

    


async def decode_jwt(token : str):
    decoded_token = jwt.decode(
        token,
        algorithms=["HS256"],
        key=settings.JWT_SECRET_KEY
    )

    return decoded_token