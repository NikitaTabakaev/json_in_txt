import json


def new_file(name_json_file):
    """Функция для создание файла: Nickname пользователя, Id пользователя"""
    with open(f"{name_json_file}", 'r') as file:
        name_json_file = json.load(file)

    for info in name_json_file:
        format_name = f"{info['user_name']}_{info['id']}.txt"

        text = open(format_name, "w")
        text.writelines(f"Имя: {info['first_name']}\n"
                        f"Фамилия: {info['last_name']}\n"
                        f"Ранг игрока: {info['rang']}\n")

        if info['ban']:
            text.writelines(f"Причина бана: {info['ban_text']}\n"
                            f"Длительность бана: {info['ban_time']} мин.")

        text.close()


new_file("info_users.json")
