import users  # Модуль с классами пользователей
import db_utils  # Модуль для работы с базой данных


def main():  # Основная функция программы
    # Загрузка данных о пользователях из базы данных
    users_list = db_utils.get_users_from_db()

    # Проверка наличия пользователей в базе данных
    if not users_list:
        print("В базе данных нет пользователей. Добавьте их вручную.")
        return

        # Определение текущего пользователя
    current_user = None
    while True:
        user_id = int(input("Введите ID пользователя: "))
        for user in users_list:
            if user.get_user_id() == user_id:
                current_user = user
                break

        if current_user:
            print(f"Приветствую, {current_user.get_name()}!")
            break
        else:
            print("Неверный ID пользователя.")

    # Отображение меню в зависимости от уровня доступа пользователя
    if current_user.get_access_level() == "admin":
        while True:
            print("\nМеню администратора:")
            print("1. Добавить пользователя")
            print("2. Удалить пользователя")
            print("3. Выход")

            choice = input("Введите ваш выбор: ")

            if choice == "1":
                new_user_id = int(input("Введите ID нового пользователя: "))
                new_name = input("Введите имя нового пользователя: ")
                new_user = users.User(new_user_id, new_name, "user")
                current_user.add_user(new_user)
            elif choice == "2":
                user_id_to_remove = int(input("Введите ID пользователя для удаления: "))
                current_user.remove_user(user_id_to_remove)
            elif choice == "3":
                break
            else:
                print("Неверный выбор.")
    else:
        print("У вас нет прав администратора.")


if __name__ == "__main__":
    main()
