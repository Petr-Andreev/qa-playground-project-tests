from pydantic import BaseModel, field_validator
from typing import List


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str

    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class Meta(BaseModel):
    total: int


class UserResponse(BaseModel):
    meta: Meta
    users: List[UserModel]


class UserModelDelete(BaseModel):
    code: int
    message: str
