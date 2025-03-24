from .abstracts.base import BaseModel
from app.models.managers.accounts import AccountManager
from tortoise import fields
class Users(BaseModel):
    
    first_name = fields.CharField(
        max_length = 255,
        null = False
    )
    last_name = fields.CharField(
        max_length = 255,
        null = False
    )
    
    email = fields.CharField(
        max_length = 255,
        null = False
    )
    
    hashed_password = fields.TextField()
    
    account_type = fields.CharField(
        max_length = 255,
        null = False
    )
    
    class Meta:
        table = "users_base_account"
        unique_together = ("email",)
        
        
        
    manager = AccountManager()