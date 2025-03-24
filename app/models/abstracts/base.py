from tortoise import Model,fields
from app.models.managers.base import Manager
from tortoise.manager import Manager as BaseManager
class BaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted = fields.BooleanField(default = False)
    
    objects = Manager()
    query = BaseManager()

    class Meta:
        abstract = True