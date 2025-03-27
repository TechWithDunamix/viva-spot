from datetime import datetime
from typing import List
from pydantic import BaseModel


class OpeningHour(BaseModel):
    
    days :List[BaseModel]
    from_ :str
    to_ :str
    
    
class Exceptions(BaseModel):
    name :str
    start :datetime
    end :datetime
    message :str
    
    