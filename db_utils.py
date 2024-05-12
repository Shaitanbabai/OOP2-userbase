import pandas as pd
import users

# Путь к файлу базы данных
DATA_FILE = "users_data.xlsx"


def get_users_from_db():
    try:
        data = pd.read_excel(DATA_FILE)
        all_users = []  # Используем all_users вместо users
        for index, row in data.iterrows():
            user_id = int(row["user_id"])
            name = row["name"]
            access_level = row["access_level"]  # Используем правильное имя столбца
            user = users.User(user_id, name, access_level)  # Сохраняем объект user в список
            all_users.append(user)  # Добавляем user в all_users
        return all_users
    except FileNotFoundError:
        print(f"Файл базы данных {DATA_FILE} не найден.")
        return []


def add_user_to_db(new_user):  # Добавить нового пользователя в базу данных
    if isinstance(new_user, users.User):
        try:
            # Загрузка данных из файла
            data = pd.read_excel(DATA_FILE)

            # Добавление нового пользователя в DataFrame
            new_user_data = {
                "user_id": [new_user.get_user_id()],
                "name": [new_user.get_name()],
                "access_level": [new_user.get_access_level()]
            }
            new_user_df = pd.DataFrame(new_user_data)

            # Объединение с существующими данными
            data = pd.concat([data, new_user_df], ignore_index=True)

            # Сохранение обновленных данных в файл
            data.to_excel(DATA_FILE, index=False)
            print(f"Пользователь {new_user.get_name()} добавлен в базу данных.")
        except Exception as e:
            print(f"Ошибка при добавлении пользователя: {e}")
    else:
        print("Неверный тип данных для добавления пользователя.")


def remove_user_from_db(user_id):
    """Удалить пользователя из базы данных."""
    if isinstance(user_id, int) and user_id > 0:
        try:
            # Загрузка данных из файла
            data = pd.read_excel(DATA_FILE)

            # Удаление пользователя по ID
            data = data[data["user_id"] != user_id]

            # Сохранение обновленных данных в файл
            data.to_excel(DATA_FILE, index=False)
            print(f"Пользователь с ID {user_id} удален из базы данных.")
        except Exception as e:
            print(f"Ошибка при удалении пользователя: {e}")
    else:
        print("Неверный ID пользователя для удаления.")
