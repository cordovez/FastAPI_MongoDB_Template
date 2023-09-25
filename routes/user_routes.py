"""
User registration router
"""

from fastapi import APIRouter, Depends 
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from auth.current_user import get_current_user
from models.user_model import UserBase, UserIn, UserUpdate, UserOut
from models.message_models import Message
from models.thing_model import MyThing
from controllers.user_controllers import (create_user, get_users, get_user,
                                          delete_user_by_id, update_user_data)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_route = APIRouter()
# Create
@user_route.post("/add")
async def add_user_to_db( user: UserIn)-> UserOut:
    """To create a new user, you only need to pass in email, username, and
    password (model: UserIn).
    
    The password will be converted to a hash before saving and a generic avatar 
    will be generated.
    
    Return is a database document (model: UserBase)
    """
    new_user = await create_user(user)
    
    return new_user

# Read
@user_route.get("/all")
async def read_all_users(current_user: Annotated[UserBase, 
                                                 Depends(get_current_user)])->list[UserBase]:
    """ Route takes current_user as parameter, which requires ('Depends' on)
    the authorization 'get_current_user'. 
    """
    users_list = await get_users()

    return users_list

@user_route.get("/me" ) 
async def read_user_me( current_user: Annotated[UserBase, 
                                                   Depends(get_current_user)])-> UserOut:
    """ Route takes an id and current_user as parameters.  Route requires
    ('Depends' on) the authorization 'get_current_user'. 
    
    It searches for the id in the database and returns db document (model: UserBase)
    """
    return current_user

@user_route.get("/my_things")
async def get_my_things(current_user: Annotated[UserBase, 
                                                   Depends(get_current_user)]):
#    list_of_things =[]
#    for thing in current_user.things:
#        found = await MyThing.find_all({thing.owner == current_user.username})
#        await list_of_things.append(found.thing_name)
    
   user = await UserBase.get(str(current_user.id), fetch_links=True)
   return user.things    

# Update
@user_route.patch("/{id}/update")
async def update_user(id,
    update_data: UserUpdate,
    current_user: Annotated[UserBase, Depends(get_current_user)],
) :
    
    updated_this = await update_user_data(id, update_data )
    return updated_this
    
    

# Delete
@user_route.delete('/{id}/remove')
async def delete_user(id:str, current_user: Annotated[UserBase, 
                                              Depends(get_current_user)]
) -> Message :
    user_has_been_deleted = await delete_user_by_id(id)
    
    return user_has_been_deleted


