from models.user_model import UserBase


async def get_user_by_username(username):
    user_data = await UserBase.find_one(UserBase.username == username)
    if not user_data:
        return False
    return user_data
