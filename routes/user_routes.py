"""
User registration router
"""

from fastapi import APIRouter, Depends, Query, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from auth.current_user import get_current_user
from models.user_model import UserBase

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_route = APIRouter()
# Create
@user_route.post("/add")
async def add_user_to_db( user):
    pass

# Read
@user_route.get("/{id}" ) 
async def read_user_me(current_user: Annotated[UserBase, Depends(get_current_user)]):
    pass

# Update
@user_route.patch("/{id}/update")
async def update_user(
    user_update_data,
    current_user,
):
    pass

# Delete
@user_route.delete('/{id}/remove')
async def delete_user(
    current_user,
):
    pass


