define n = Character('Никита', color="#c33eef")
define m = Character('Я', color="#ff32f1")
image nroom = im.Scale("images/night room.png", 1920, 1080)

label start:
    scene nroom
    play music "music/future club.mp3" fadein 4.0
    "Это была та самая ночь"
    ""
    n "Привет. Чем занят? Меня тут внезапно позвали тусить чуваки с универа, говорят, будет весело, гоу со мной? Я там знаю только пару человек и то, только руку жму в коридоре. Не хочу сидеть один как дебил("
    m "Хмм, туса?"
    n "Ага, девчонки даже будут, а не как обычно!"
    m "Блин, ну хз, а когда? Прям сейчас что ли?"
    n "Да, собираются уже через час или что-то типа того, нужно решать быстрее"
    m "Дай подумать чуть"
    n "Хех, как будто у тебя миллион планов в пятницу вечером)"
    n "По-любому будешь играть в комп до утра, пойдем, а то так никогда не социализируешься"

    menu:
        "Согласиться пойти на вечеринку":
            jump party

        "Отказаться от вечеринки":
            jump noparty

label noparty:
    stop music fadeout 8.0
    m "Ахаха, очень смешно, но я все-таки сливаюсь"
    n "В принципе ожидаемо, ну ладно, хороших выходных)"
    m "Удачи)"
    "..."
    "Дурак, слился как обычно"
    "Может уже стоит перестать страдать от одиночества и попытаться хоть как-то наладить свою личную жизнь?"
    "Эх, может в следующий раз..."
    "Ну да, ну да"
    "Ладно, надо думать чем заняться"
    return

label party:
    m "Лааадно, уговорил, куда, во сколько?"
    n "Ееее, давай через час у метро Измайловская, тебе близко"
    m "Ага, пара станций"
    n "Возьми себе что-нибудь из алкоголя)"
    m "Ок, до встречи)"
    "..."
    "Ну что же, вечер обещает быть интересным"
    "Пойду одеваться, воткну наушники и выхожу"
    "Что бы послушать?..."

    menu:
        "Psytrance":
            play music "music/future club.mp3"

        "Metalcore":
            play music "music/future club.mp3"

        "Synthwave":
            play music "music/future club.mp3"

    jump city

label city:
    scene street
    with fade
    ""
    "На улице уже темно и моросит дождь"
