from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class UserRequest(BaseModel):
    username: str
    password: str

class UserInfoBase(BaseModel):
    nickname: Optional[str] = Field(None, max_length=50, description="昵称")
    avatar: Optional[str] = Field(None, max_length=255, description="头像UR")
    gender: Optional[str] = Field(None, max_length=10, description="性别")
    bio: Optional[str] = Field(None, max_length=500, description="个⼈简介")

class UserInfoResponse(UserInfoBase):
    id:int
    username: str
    model_config = ConfigDict(from_attributes=True)

class UserAuthResponse(BaseModel):
    token: str
    user_info:UserInfoResponse=Field(...,alias="userInfo")
    model_config = ConfigDict(
        populate_by_name=True,
    )

class UserUpdateRequest(BaseModel):
    nickname: str
    avatar: str
    gender: str
    bio: str
    phone_number: str

class UserChangePasswordRequest(BaseModel):
    old_password: str = Field(..., alias="oldPassword")
    new_password: str = Field(..., min_length=6, alias="newPassword")
    model_config = ConfigDict(populate_by_name=True)
