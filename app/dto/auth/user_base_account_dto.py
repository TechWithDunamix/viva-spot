from pydantic import BaseModel, EmailStr, field_validator
from typing import Annotated

class UserBaseAccountDTO(BaseModel):
    first_name: Annotated[str, 255]  
    last_name: Annotated[str, 255]
    email: EmailStr
    password: str
    account_type: Annotated[str, 255]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        allowed_domains = {"gmail.com", "yahoo.com", "outlook.com"}
        domain = value.split("@")[-1]
        if domain not in allowed_domains:
            raise ValueError(f"Only emails from {', '.join(allowed_domains)} are allowed.")
        return value

    class Config:
        from_attributes = True
