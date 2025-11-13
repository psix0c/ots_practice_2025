# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: [Ваше ФИО]

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Иванов Иван Иванович",
        "academic_group": "ИВТИИбд-11",
        "github_link": "https://github.com/ivanov_ivan"
        "student_name": "Лукашин Никита Андреевич",
        "academic_group": "ИВТИИбд-14",
        "github_link": "https://github.com/psix0c"
    }
    return system_info

@@ -19,4 +19,4 @@
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
        print(f"- {key}: {value}")