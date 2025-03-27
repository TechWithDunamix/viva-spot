from typing import List
from tortoise import Model, fields
from app.dto.resturant.delivery_zones import ResturantDelveryZones
from app.dto.resturant.openinghours import OpeningHour,Exceptions

class ResturantPickupMixins(Model):
    
    pickups = fields.BooleanField(default = False)
    
    class Meta:
        abstract = True
    
    
class ResturantDeliveryMixins(Model):
    delivery = fields.BooleanField(default = True)
    zones :List[ResturantDelveryZones] = fields.JSONField(default = [])
    address_form_fields = fields.JSONField(default = [])
    class Meta:
        abstract = True
    
    
class ResturantTableReservation(Model):
    reservation = fields.BooleanField(default = True)
    minimum_guest = fields.IntField(default = 0)
    maximum_guest = fields.IntField(default = 8)
    allow_pre_order = fields.IntField(default = 2)
    maximu_time_in_advance = fields.IntField(default = 8)
    mimimum_time_in_advance = fields.IntField(default = 8)
    
    class Meta:
        abstract = True
    
    
    
class OnPromis(Model):
    promise = fields.BooleanField(default = True)
    
    class Meta:
        abstract = True
class OpeningHours(Model):
    hours :List[OpeningHour] = fields.JSONField(default = [])
    exceptions :List[Exceptions]= fields.JSONField(default = [])
    class Meta:
        abstract = True
    
    
    
    
    
    