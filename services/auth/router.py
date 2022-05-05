from fastapi import APIRouter,Depends,Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from .utility import authenticate_user,manager

endpoint = APIRouter(
    prefix="/login",
    tags = ["login"]
)


@endpoint.get('')
def login_get():
    return {"Welcome to":"FastAPI!"}

@endpoint.post('')
def login_post(request: Request, user_info : OAuth2PasswordRequestForm = Depends()):
    if authenticate_user(user_info.username, user_info.password):
        token = manager.create_access_token(data = {"sub":user_info.username})
        resp = RedirectResponse('/',status_code=302)
        manager.set_cookie(resp,token)
        return resp
    else : 
        return RedirectResponse('/login',status_code=307)

@endpoint.get('/test')
def login_test(user = Depends(manager)):
    return {"Hey":"You got in!"}