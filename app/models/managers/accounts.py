from tortoise.manager import Manager
from app.routes.auth._utils.hashing import hash_password

class AccountManager(Manager):
    
    
    async def create_account(self, email :str, first_name :str, last_name :str, password :str, account_type :str, **kwargs):
        hashed_password = hash_password(password)
        account = await self.model.create(
            email = email,
            first_name = first_name.upper(),
            last_name = last_name.upper(),
            hashed_password = hashed_password,
            account_type = account_type,
            **kwargs
        )
        return account