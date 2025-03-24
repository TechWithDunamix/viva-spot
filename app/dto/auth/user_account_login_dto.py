from pydantic import BaseModel

class UserAccountLoginDTO(BaseModel):
    
    email :str
    password :str 