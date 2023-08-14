from database.models import User
from datetime import datetime
from database import get_db
# регистрация пользователя
def register_user_db(name, email, phone_number, password, user_city):
    # создание подключение к бд
    db = next(get_db())
    new_user = User(name=name, email=email, phone_number=phone_number, password=password, user_city=user_city,
                    reg_date=datetime.now())
    # Добавляем в базу
    db.add(new_user)
    db.commit()
    return new_user.id
# проверка на наличие пользователя в базе
def check_user_data_db(phone_number, email):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number, email=email).first()
    if checker:
        return False
    return True
# проверка пароля пользователя
def check_user_password_db(email, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        if checker.password == password:
            return checker.id
        else:
            return "Неверный пароль"
    else:
        return "Неверная почта"
# получить информацию о пользователю
def profile_info_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        return exact_user.email, exact_user.phone_number, exact_user.id, exact_user.name,\
            exact_user.reg_date, exact_user.user_city
    return "Пользователь не найден"
# изменение данных пользователя
def change_user_data(user_id, change_info, new_data):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        if change_info == "email":
            exact_user.email = new_data
        elif change_info == "number":
            exact_user.phone_number = new_data
        elif change_info == "name":
            exact_user.name = new_data
        elif change_info == "city":
            exact_user.user_city = new_data
        elif change_info == "password":
            exact_user.password = new_data
        db.commit()
        return "Данные успешно изменены"
    return "Пользователь не найден"
# сброс пароля

