from pydantic import BaseModel, EmailStr, validator
from fastapi import HTTPException


class NewUserForm(BaseModel):
    email: str
    name: str
    password: str

    @validator("email", "name", "password")
    def check_empty(cls, v):
        if not v or v.isspace():
            raise HTTPException(status_code=422, detail="필수 항목을 입력해주세요.")
        return v

    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise HTTPException(
                status_code=422, detail="비밀 번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요."
            )
        if not any(char.isdigit() for char in v):
            raise HTTPException(
                status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요."
            )
        if not any(char.isalnum() for char in v):
            raise HTTPException(
                status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요."
            )

        return v
