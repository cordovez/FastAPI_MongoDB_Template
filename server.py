from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# from config.db import init_db
from routes.user_routes import user_route
from routes.token_route import token_route


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(CORSMiddleware, 
                   allow_origins= origins, 
                   allow_credentials = True, 
                   allow_methods=["*"], 
                   allow_headers=["*"], )



@app.get("/", tags=["root"])
def root():
    return "Welcome to the users api."

app.include_router(user_route, prefix="/users", tags=["users"])
app.include_router(token_route, tags=["token"])

# @app.on_event("startup")
# async def connect():
#     await init_db()


if __name__ == "__main__":
    uvicorn.run(reload=True, app="server:app")
