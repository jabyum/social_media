from fastapi import FastAPI
from database import Base, engine
# создание таблиц в базе данных
Base.metadata.create_all(bind=engine)
import uvicorn
app = FastAPI()
from api.hashtag_api import hashtags
from api.photo_api import photos
from api.posts_api import posts
from api.users_api import users
from api.comments_api import comments
# @app.get("/hello")
# async def hello():
#     return {"Hello": "Fastapi"}
# @app.post("/hello")
# async def post_home(name: str):
#     return {'message': f"hello{name}"}