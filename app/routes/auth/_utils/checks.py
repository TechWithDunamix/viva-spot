from re import I
from typing import Any, Tuple,Union
from app.models import Users
from .hashing import verify_password
from .exceptions import UserAccountCreationCheckExcetiption
async def email_exists(email :str) -> Any:
    if await Users.query.filter(email = email).exists():
        raise UserAccountCreationCheckExcetiption(data = {"email": "Email Already Exists"}, message = "Email already exists")
        
        


async def authenticate_credentials(email :str, password :str) -> Tuple[bool, Union[Users, bool]]:
    print(email)
    user  :Users= await Users.manager.get_or_none(email =email)
    if not user:
        return None, None
    
    if not verify_password(password, user.hashed_password):
        return None, None
    
    
    return True, user
    
    
    