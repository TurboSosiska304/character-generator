import random
import json
from ages import MAX_AGE_BY_RACE
from story import generate_story

# Данные для генерации (можешь расширять)

races = ["Человек", "Эльф", "Гном", "Орк", "Троль"]
genders = ["Мужской", "Женский"]

names_male = ["Алексей", "Борис", "Виктор", "Дмитрий", "Евгений"]
names_female = ["Анна", "Беатрисса", "Валентина", "Дарина", "Екатерина"]

classes = ["Воин", "Маг", "Разведчик", "Жрец"]

traits = [
    "Смелый", "Умный", "Хитрый", "Добрый", "Жестокий",
    "Весёлый", "Застенчивый", "Гордый", "Трусливый"
]

skills_by_class = {
    "Воин": ["Сила", "Выносливость", "Стрельба", "Ближний бой"],
    "Маг": ["Магия Огня", "Магия Воды", "Магия Воздуха", "Магия Земли"],
    "Разведчик": ["Скрытность", "Ловкость", "Взлом", "Обаяние"],
    "Жрец": ["Лечение", "Священная Магия", "Защита", "Ритуалы"]
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
        skill: random.randint(40, 100)  # уровень навыка от 40 до 100 для разнообразия
        for skill in random.sample(skills_pool, 3)  # выбираем 3 навыка случайно
    }

    trait = random.choice(traits)

    character_data = {
        "Имя": name,
        "Раса": race,
        "Пол": gender,
        "Возраст": age,
        "Класс": class_,
        "Черта характера": trait,
        "Навыки": skillset,
        # История генерируем отдельно, прокидываем нужные данные
        "История": generate_story({
            "Имя": name,
            "Раса": race,
            "Пол": gender,
            "Возраст": age,
            "Класс": class_,
            "Черта характера": trait
        })
    }
    return character_data

def generate_characters(count=1):
    return [generate_character() for _ in range(count)]

def export_character(character, filename="персонаж.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in character.items():
            if key == "Навыки":
                f.write("Навыки:\n")
                for skill, lvl in value.items():
                    f.write(f"  - {skill}: {lvl}\n")
            elif key == "История":
                f.write("\nИстория персонажа:\n")
                f.write(value + "\n")
            else:
                f.write(f"{key}: {value}\n")

def export_characters_to_json(characters, filename="персонажи.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(characters, f, ensure_ascii=False, indent=4)

def export_characters_to_html(characters, filename="персонажи.html"):
    html_head = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Генератор персонажей</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #1e1e2f;
            color: #f0f0f0;
            padding: 20px;
        }
        .character {
            background: #2d2d44;
            border-radius: 8px;
            padding: 15px 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.6);
        }
        h2 {
            color: #79b8ff;
            margin-bottom: 10px;
        }
        .skills {
            margin-top: 10px;
            padding-left: 20px;
        }
        .skill {
            margin-bottom: 4px;
        }
        .story {
            background: #3a3a5c;
            padding: 10px;
            border-radius: 6px;
            margin-top: 15px;
            font-style: italic;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <h1>Сгенерированные персонажи</h1>
"""
    html_tail = """
</body>
</html>
"""
    body = ""
    for c in characters:
        body += '<div class="character">\n'
        body += f'<h2>{c["Имя"]} ({c["Раса"]}, {c["Пол"]}, {c["Возраст"]} лет)</h2>\n'
        body += f'<p><b>Класс:</b> {c["Класс"]} | <b>Черта характера:</b> {c["Черта характера"]}</p>\n'
        body += '<div class="skills"><b>Навыки:</b><br>\n'
        for skill, lvl in c["Навыки"].items():
            body += f'<div class="skill">{skill}: {lvl}</div>\n'
        body += '</div>\n'
        body += f'<div class="story"><b>История:</b><br>{c["История"]}</div>\n'
        body += '</div>\n'

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_head + body + html_tail)
