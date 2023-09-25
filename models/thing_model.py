"""
User Models
"""
import pytz
from datetime import datetime
from typing import Optional

from beanie import Document, Link
from pydantic import BaseModel, EmailStr, ConfigDict



central_europe = pytz.timezone('Europe/Paris')


class MyThingIn(BaseModel):
    thing_name: str
    thing_description: Optional[str] | None = None
    
     
class MyThingOut(BaseModel):
    thing_name: str
    owner: str
    
class MyThing(Document):
    """User database representation"""
    model_config = ConfigDict(extra='allow') 
    
    thing_name: str | None = None
    created_at: datetime = datetime.now(central_europe)
    owner: str | None = None

    class Settings:
        name = "Things"
        