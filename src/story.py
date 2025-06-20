import random

# Заготовки
settings = [
    "в мрачном лесу, полном древних тайн",
    "в разрушенной империи, где магия запрещена",
    "в подземельях огромного города",
    "на далёком севере, среди вечно замёрзших земель",
    "в заброшенном монастыре на вершине гор"
]

origins = [
    "сын кузнеца, чья деревня была сожжена дотла",
    "дочь вождя племени, изгнанная за предательство",
    "ученик архимага, случайно открывший запретное знание",
    "сирота, воспитанная наёмниками и воровским братством",
    "избранник древнего пророчества, в которое никто не верит"
]

conflicts = [
    "преследуемый Инквизицией за магический дар",
    "охотится за убийцей семьи, но не знает его лица",
    "бежит от культа, в который его втянули в детстве",
    "должен вернуть украденный артефакт, иначе погибнет весь клан",
    "страдает от проклятия, превращающего его в монстра"
]

quests = [
    "отыскать ключ к древнему храму",
    "спасти ребёнка, который может изменить судьбу мира",
    "сломать проклятие, передающееся по крови",
    "объединить разрозненные королевства под единым флагом",
    "найти легендарную реликвию, способную воскресить мёртвых"
]

twists = [
    "но истинный враг всё это время был его наставником",
    "однажды он узнаёт, что сам является причиной всех бед",
    "и только враг может дать ему спасение",
    "но его прошлое начинает уничтожать всё, что он любит",
    "а тайна его рождения меняет всё"
]

def generate_story(character: dict) -> str:
    name = character.get("Имя", "Он")
    race = character.get("Раса", "человек")
    char_class = character.get("Класс", "странник")
    trait = character.get("Черта характера", "неизвестный")
    gender = character.get("Пол", "Мужской")
    
    pronoun = "Он" if gender == "Мужской" else "Она"

    # Формируем историю
    setting = random.choice(settings)
    origin = random.choice(origins)
    conflict = random.choice(conflicts)
    quest = random.choice(quests)
    twist = random.choice(twists)

    story = f"""
{name} — {race.lower()} и {char_class.lower()}, известный как {trait.lower()}.
Родился {setting}, {origin}.
С юных лет {pronoun.lower()} оказался в центре опасностей: {conflict}.
Теперь цель ясна — {quest}, но всё не так просто: {twist}.
    """.strip()

    return story

# Тест
if __name__ == "__main__":
    test_char = {
        "Имя": "Кай",
        "Раса": "Человек",
        "Пол": "Мужской",
        "Класс": "Некромант",
        "Черта характера": "Хитрый"
    }
    print(generate_story(test_char))
