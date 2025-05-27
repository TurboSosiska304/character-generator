import random

# Предустановки
names_male = ["Артур", "Рейн", "Кай", "Дарион", "Тору"]
names_female = ["Элира", "Сирис", "Мей", "Астелла", "Наоми"]

races = ["Человек", "Эльф", "Демон", "Зверочеловек", "Орк", "Драконид"]
genders = ["Мужской", "Женский"]
classes = ["Воин", "Маг", "Охотник", "Вор", "Жрец", "Некромант"]
traits = ["Добрый", "Мстительный", "Хитрый", "Отважный", "Безумный", "Невозмутимый"]

def generate_character():
    gender = random.choice(genders)
    name = random.choice(names_male if gender == "Мужской" else names_female)

    character = {
        "Имя": name,
        "Раса": random.choice(races),
        "Пол": gender,
        "Возраст": random.randint(16, 100),
        "Класс": random.choice(classes),
        "Черта характера": random.choice(traits)
    }

    return character

# Генерация примера
if __name__ == "__main__":
    character = generate_character()
    for key, value in character.items():
        print(f"{key}: {value}")
