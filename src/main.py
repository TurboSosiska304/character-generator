import random
from ages import MAX_AGE_BY_RACE
from story import generate_story  # 👈 добавили

names_male = ["Артур", "Рейн", "Кай", "Дарион", "Тору"]
names_female = ["Элира", "Сирис", "Мей", "Астелла", "Наоми"]

races = list(MAX_AGE_BY_RACE.keys())
genders = ["Мужской", "Женский"]
classes = ["Воин", "Маг", "Охотник", "Вор", "Жрец", "Некромант"]
traits = ["Добрый", "Мстительный", "Хитрый", "Отважный", "Безумный", "Невозмутимый"]

skills_by_class = {
    "Воин": ["Фехтование", "Выживание", "Устрашение"],
    "Маг": ["Магия огня", "Магия льда", "Алхимия"],
    "Охотник": ["Стрельба из лука", "Выживание", "Ловкость"],
    "Вор": ["Скрытность", "Взлом", "Ловкость"],
    "Жрец": ["Целительство", "Алхимия", "Харизма"],
    "Некромант": ["Магия тьмы", "Целительство", "Устрашение"]
}

def generate_character():
    gender = random.choice(genders)
    name = random.choice(names_male if gender == "Мужской" else names_female)
    race = random.choice(races)
    class_ = random.choice(classes)
    max_age = MAX_AGE_BY_RACE.get(race, 100)
    age = random.randint(16, max_age)

    skills_pool = skills_by_class[class_]
    skillset = {
        skill: random.randint(40, 100)
        for skill in random.sample(skills_pool, 3)
    }

    character = {
        "Имя": name,
        "Раса": race,
        "Пол": gender,
        "Возраст": age,
        "Класс": class_,
        "Черта характера": random.choice(traits),
        "Навыки": skillset
    }

    # Добавляем историю персонажа
    character["История"] = generate_story(character)

    return character

def export_character(character, filename="персонаж.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for key, value in character.items():
            if key == "Навыки":
                file.write("Навыки:\n")
                for skill, lvl in value.items():
                    file.write(f"  - {skill}: {lvl}\n")
            elif key == "История":
                file.write("\nИстория персонажа:\n")
                file.write(value + "\n")
            else:
                file.write(f"{key}: {value}\n")
