from dataclasses import field
from email.policy import default
from app.models.abstracts.base import BaseModel
from tortoise import fields
from .mixins.resturant_mixins import ResturantDeliveryMixins,ResturantDelveryZones,ResturantPickupMixins, ResturantTableReservation
class Resturants(BaseModel, ResturantDeliveryMixins,ResturantPickupMixins, ResturantTableReservation):
    
    name = fields.CharField(max_length = 255)
    phone = fields.CharField(max_length = 255, null = True)
    country = fields.CharField(max_length = 255, null = True)
    timezone = fields.CharField(max_length = 255,null = True)
    state = fields.CharField(max_length = 255,null = True)
    postal_code = fields.CharField(max_length = 255,null = True)
    street_name = fields.TextField(null = True)
    website = fields.CharField(null = True, max_length = 255)
    full_address = fields.TextField(null = True)
    restricted = fields.BooleanField(default = False)
    confirmed = fields.BooleanField(default = False)
    