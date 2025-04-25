from pydantic import BaseModel, EmailStr, field_validator
from typing import Annotated

class UserBaseAccountDTO(BaseModel):
    first_name: Annotated[str, 255]  
    last_name: Annotated[str, 255]
    email: EmailStr
    password: str
    account_type: Annotated[str, 255]

   

    class Config:
        from_attributes = True
