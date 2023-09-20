"""
User Models
"""

from datetime import datetime
from typing import Optional, Annotated

from beanie import Document, Link
from pydantic import BaseModel, EmailStr, Extra


class ImageBase(BaseModel):
    public_id: str
    uri: str

class UserBase(Document):
    """User database representation"""
    first_name: Optional[str]
    last_name: Optional[str]
    # plants: list[Link[PlantMongoDB]] = []
    avatar: dict 
    created_at: Optional[datetime] = datetime.now()
    disabled: bool = False
    email: Optional[EmailStr] | None = None
    username: Optional[str] | None = None
    password_hash: Optional[str] | None = None

    class Settings:
        name = "Users"
        
    class Config:
        extra = Extra.allow

    
    
class UserIn(BaseModel):
    email: EmailStr
    username: str
    password: str
    avatar: Optional[ImageBase]


class UserOut(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    plants: Optional[list]
    avatar: dict
    email: EmailStr
    username: str
    created_at: datetime


class UserUpdate(BaseModel):
    """User database representation"""
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    email: Optional[EmailStr] | None = None
    username: Optional[str] | None = None
