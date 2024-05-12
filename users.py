import db_utils


class User:
    def __init__(self, user_id, name, access_level):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, new_user_id):
        if isinstance(new_user_id, int) and new_user_id > 0:
            self.__user_id = new_user_id
        else:
            raise ValueError("ID пользователя должен быть целым числом больше 0.")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            raise ValueError("Имя пользователя должно быть непустой строкой.")

    def get_access_level(self):
        return self.__access_level

    def __str__(self):
        return f"User ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level}"


class Admin(User):

    def __init__(self, user_id, name):
        super().__init__(user_id, name, "admin")

    def add_user(self, new_user):
        if isinstance(new_user, User):
            if self.get_access_level() == "admin":
                db_utils.add_user_to_db(new_user)
                print(f"Пользователь {new_user.get_name()} добавлен в систему.")
            else:
                print("У вас нет прав на добавление пользователей.")
        else:
            print("Неверный тип данных для добавления пользователя.")

    def remove_user(self, user_id):
        if isinstance(user_id, int) and user_id > 0:
            if self.get_access_level() == "admin":
                db_utils.remove_user_from_db(user_id)
                print(f"Пользователь с ID {user_id} удален из системы.")
            else:
                print("У вас нет прав на удаление пользователей.")
        else:
            print("Неверный ID пользователя для удаления.")
