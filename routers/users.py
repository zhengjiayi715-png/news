from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config import db_config
from models.users import User
from schems.users import UserRequest, UserAuthResponse, UserInfoResponse, UserUpdateRequest, UserChangePasswordRequest
from crud import users
from starlette import status
from utils.response import success_response
from utils.auth import get_current_user

router = APIRouter(prefix="/api/users", tags=["users"])

@router.post("register")
async def register(user_data:UserRequest,db:AsyncSession=Depends(db_config.get_db)):
    existing_user=await users.get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username already exists")
    user=await users.create_user(db, user_data)
    token=await users.create_token(db, user.id)
    # return{
    #     "code": 200,
    #     "message": "success",
    #     "data": {
    #         "token": token,
    #         "userInfo":{
    #             "id":user.id,
    #             "username":user.username,
    #             "bio":user.bio,
    #             "avatar":user.avatar,
    #         }
    #     }
    # }
    return success_response(message="User created successfully", data=UserAuthResponse(token=token,user_info=UserInfoResponse.model_validate(user)))

@router.post("/login")
async def login(user_data:UserRequest,db:AsyncSession  = Depends(db_config.get_db)):
    user=await users.authenticate_user(db,user_data.username, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token=await users.create_token(db, user.id)
    return success_response(message="User created successfully", data=UserAuthResponse(token=token,user_info=UserInfoResponse.model_validate(user)))

@router.get("/info")
async def get_user_info(user:User=Depends(get_current_user)):
    return success_response(message="User created successfully",data=UserInfoResponse.model_validate(user))

@router.put("/update")
async def update_user_info(user_data:UserUpdateRequest,user:User=Depends(get_current_user),db:AsyncSession=Depends(db_config.get_db)):
    user=await users.update_user(db,user.username,user_data)
    return success_response(message="User created successfully",data=UserInfoResponse.model_validate(user))

@router.put("/password")
async def update_password(password_data:UserChangePasswordRequest,user:User=Depends(get_current_user),db:AsyncSession=Depends(db_config.get_db)):
    res_change_pwd=await users.change_password(db,user,user.username,user.password)
    if not res_change_pwd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    return success_response(message="User created successfully")