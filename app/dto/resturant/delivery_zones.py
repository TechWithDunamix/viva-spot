from typing import Optional, Union
from pydantic import BaseModel

class ResturantDelveryZones(BaseModel):
    
    name :str
    min_ammount : Union[str,int,float]
    delivery_fee :Optional[Union[str,int,float]]
    hidden :bool