from fastapi import APIRouter, Depends, HTTPException, Response
from authx import AuthX, AuthXConfig
from models.user_login import UserLoginSchema

router = APIRouter(prefix="/login", tags=["login"])


config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config) 


@router.post("/login")
def login(creds: UserLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid=creds.username)  
        response.set_cookie(
            key=config.JWT_ACCESS_COOKIE_NAME,
            value=token,
            httponly=True,
            secure=False,
            samesite="lax"
        )
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@router.get("/protected")
def protected(user=Depends(security.access_token_required)):
    return {"data": "top secret", "user": user}
