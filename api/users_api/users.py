from fastapi import Request
from pydantic import BaseModel
from typing import List, Dict
from database.userservice import register_user_db, check_user_data_db, check_user_password_db, change_user_data, profile_info_db
from api import app
# проверка почты
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False
# модель пользователя
class User(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str
    user_city: str

# регистрация пользователя
@app.post("/api/registration")
async def register_user(user_model: User):
    user_data = dict(user_model)
    mail_validation = mail_checker(user_model.email)
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data)
            return {"status": 1, "user_id": reg_user}
        except Exception as e:
            return {"status": 0, "message": e}
    return {"status": 0, "message": "Invalid email"}
# получить данные пользователя по user_id
@app.get("/api/user")
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)
    return {"status": 1, "message": exact_user}
# вход в аккаунт
@app.post("/api/login")
async def login_user(email: str, password: str):
    mail_validation = mail_checker(email)
    if mail_validation:
        login_checker = check_user_password_db(email, password)
        if login_checker.isdigit():
            return {"status": 1, "message": login_checker}
        return {"status": 0, "message": login_checker}
    return {"status": 0, "message": "Invalid email"}
@app.put("/api/change-profile")
async def change_user_profile(user_id: int, change_info: str, new_data: str):
    data = change_user_data(user_id, change_info, new_data)
    return {"status": 1, "message": data}

