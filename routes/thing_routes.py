
from fastapi import APIRouter, Depends 
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from auth.current_user import get_current_user
from models.user_model import UserBase, UserIn, UserUpdate, UserOut
from models.message_models import Message
from models.thing_model import MyThing, MyThingIn, MyThingOut


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

thing_route= APIRouter()

# Create
@thing_route.post("/thing")
async def add_thing_to_db(thing: MyThingIn, current_user: Annotated[UserBase, 
                                                 Depends(get_current_user)])->MyThingOut:
  
    new_thing = MyThing(thing_name= thing.thing_name, 
                        thing_description=thing.thing_description,
                        owner=current_user.username)
    
    await MyThing.create(new_thing)
    
    current_user.things.append(new_thing)
    await current_user.save()
    
    user = await UserBase.get(str(current_user.id), fetch_links=True)
    return user.things 
    