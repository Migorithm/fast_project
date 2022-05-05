from passlib.context import CryptContext
from cores.models.database import users
from cores.schemas.user import UserDB
from fastapi_login import LoginManager
import os
from fastapi import Request,HTTPException
from fastapi.responses import RedirectResponse


pass_ctx = CryptContext(schemes=["bcrypt"])

def get_hashed_password(plain_password):
    return pass_ctx.hash(plain_password)

def verify_password(plain_password,hashed_password) -> bool:
    return pass_ctx.verify(plain_password,hashed_password)

def authenticate_user(username:str,password:str):
    if username in users:
        return verify_password(password,users[username].get("hashed_password"))


#LoginManager
class NotAuthenticatedException(Exception):
    pass

manager = LoginManager(
    os.urandom(24).hex(),
    token_url="/login",
    use_cookie=True,
    custom_exception=NotAuthenticatedException
    )

@manager.user_loader()
def user_loader(username):
    if username in users:
        return UserDB(**users[username])

def not_authenticated_exception_handler(req:Request,exce):
    return RedirectResponse("/login")

