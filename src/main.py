import random
from ages import MAX_AGE_BY_RACE

# Предустановки
names_male = ["Артур", "Рейн", "Кай", "Дарион", "Тору"]
names_female = ["Элира", "Сирис", "Мей", "Астелла", "Наоми"]

races = list(MAX_AGE_BY_RACE.keys())
genders = ["Мужской", "Женский"]
classes = ["Воин", "Маг", "Охотник", "Вор", "Жрец", "Некромант"]
traits = ["Добрый", "Мстительный", "Хитрый", "Отважный", "Безумный", "Невозмутимый"]

def generate_character():
    gender = random.choice(genders)
    name = random.choice(names_male if gender == "Мужской" else names_female)
    race = random.choice(races)
    max_age = MAX_AGE_BY_RACE.get(race, 100)

    character = {
        "Имя": name,
        "Раса": race,
        "Пол": gender,
        "Возраст": random.randint(16, max_age),
        "Класс": random.choice(classes),
        "Черта характера": random.choice(traits)
    }

    return character

# Генерация примера
if __name__ == "__main__":
    character = generate_character()
    print("🎲 Сгенерированный персонаж:\n")
    for key, value in character.items():
        print(f"{key}: {value}")
