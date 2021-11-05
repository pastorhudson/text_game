from pprint import pprint
import random
import os
import time


# define the countdown func.
def countdown(character, t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Take a moment to consider your life choices. . . {character['name']}", timer, end="\r")
        time.sleep(1)
        t -= 1


choices = [1, 2]

bad_entry = ['Come on buddy lets be reasonable here.',
             'Do you kiss your mother with that mouth?',
             "I don't even do that on Saturdays."]

cant_pay = ["Nice Try buddy. . . \n",
                "Keep it up and I'll throw you out.\n",
                "We don't take kindly to thieves around here. . . \n",
                "You're lucky it's not a Saturday. . . \n"]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
    clear()
    # Use a breakpoint in the code line below to debug your script.
    print("""\nWelcome To Adventure Land.\nYou're not sure how you got here, but you do remember your name.""")  # Press Ctrl+F8 to toggle the breakpoint.


def new_character():
    name = input("\nWhat is your name?: ")
    character = {
        "hp": 100,
        "max_hp": 100,
        "mp": 10,
        "max_mp": 10,
        "gold": 100,
        "level": 1,
        "xp": 0,
        "base_attack": 1,
        "base_defense": 1,
        "name": name,
        "spells": {
            "heal": 6
        }
    }
    return character


def go_to_inn(character, town, didnt_pay=0):
    options = [f'',
               f'Welcome to {town} Inn:',
               "",
               '1. Stay for the night [50 gold]',
               '2. Exit Inn']
    print("\n".join(options))
    print_stats(character)
    choices = int(input(f"\nWhat do we do here {character['name']}?: "))
    match choices:
        case 1:
            if character['gold'] > 49:
                character['hp'] = character['max_hp']
                character['gold'] -= 50
                clear()
                print("You feel refreshed and ready to face the day!")
                find_town(character, town)
            didnt_pay += 1
            print(random.choice(cant_pay))
            if didnt_pay > 2:
                clear()
                print("The inn keeper thrusts you out of the shoppe in into the street!\n"
                      "'AND DON'T COME BACK!' He yells\n")
                countdown(character, 10)
                main_menu(character)
            go_to_inn(character, town, didnt_pay)
            find_town(character, town)
        case 2:
            find_town(character, town)


def go_to_shop(character, town, didnt_pay=0):

    options = [f'',
               f'Welcome to {town} Shoppe! Bellows a friendly shop keeper.\nHow can I help you?',
               '',
               '1. Upgrade Attack [50 gold]',
               '2. Upgrade Defense [50 gold]',
               '3. Exit Shop',
               '']
    print_stats(character, extended=True)
    print("\n".join(options))
    choice = int(input(f"What Do you want to do? [{character['gold']}G]: "))
    match choice:
        case 1:
            clear()
            increase = random.randint(1, 5)
            if character['gold'] > 49:
                character['gold'] -= 50
                print(f"\n\nBase attack +{increase}! now {character['base_attack'] + increase}\n")
                character['base_attack'] += increase
                go_to_shop(character, town)
            else:
                didnt_pay += 1
                print(random.choice(cant_pay))
                if didnt_pay > 2:
                    clear()
                    print("The Shoppe keeper thrusts you out of the shoppe in into the street!\n"
                          "'AND DON'T COME BACK!' He yells\n")
                    countdown(character, 10)
                    main_menu(character)
                go_to_shop(character, town, didnt_pay)
        case 2:
            clear()
            increase = random.randint(1, 5)
            if character['gold'] > 49:
                character['gold'] -= 50
                print(f"\n\nBase defense +{increase}! now {character['base_defense'] + increase}\n")
                character['base_defense'] += increase
                go_to_shop(character, town)
            else:
                didnt_pay += 1
                print(random.choice(cant_pay))
                if didnt_pay > 2:
                    clear()
                    print("The Shoppe keeper thrusts you out of the shoppe in into the street!\n"
                          "'AND DON'T COME BACK!' He yells\n")

                    countdown(character, 10)
                    main_menu(character)
                go_to_shop(character, town, didnt_pay)

        case 3:
            clear()
            find_town(character, town)
        case _:
            clear()
            print("The Shoppe keeper thrusts you out of the shoppe in into the street!\n"
                  "'AND DON'T COME BACK!' He yells")
            main_menu(character)


def find_town(character, town=None):
    clear()
    if not town:
        town = town_name()
        observations = [f"You walk for what seems like days. Just when you think all is lost you stumble into {town}",
                        f"You prepare yourself for a long walk, but it turns out {town} is just over the hill.",
                        f"You can see the sign for {town} in the distance. You're there before you know it.",
                        f"You take off running in no direction in particular. By sheer dumb luck you stumble upon {town}."]
    else:
        observations = [f'You step into the familiar street of {town}',
                        f"It's no Uniontown, but {town} has it's charm."]
    print("\n".join(["", random.choice(observations),
                     "",
                     "1. Head to the shop.",
                     "2. Go to the Inn",
                     "3. Leave Town",
                     "",
                     ]
                    )
          )
    print_stats(character)
    try:
        choice = int(input(f"What Do you want to do {character['name']}?: "))
    except ValueError:
        choice = None
    match choice:
        case 1:
            clear()
            go_to_shop(character, town)
        case 2:
            clear()
            go_to_inn(character, town)
        case 3:
            clear()
            main_menu(character)
        case _:
            clear()
            print("\n")
            print(random.choice(bad_entry), "\n")
            main_menu(character)
    return character


def town_name():
    first = ["Barkers,"
             "Collins",
             "Jacobs",
             "Lukas's",
             "Leigh's",
             "Ronnie's"]
    last = ["Run",
            "Mill",
            "Town",
            "Bryer",
            "Village"]
    return " ".join([random.choice(first), random.choice(last)])


def enemy_name():
    first = ["Angry",
             "Toxic",
             "Pedantic",
             "Abnormal",
             "Fluffy",
             "Cute",
             "Tired"]
    last = ["Bunny",
            "Beaver",
            "Bear",
            "Walrus",
            "Wolf",
            "Mummy",
            "Lizard",
            ]
    return f"{random.choice(first)} {random.choice(last)}"


def get_enemy(character):
    buff = random.randint(1, 10)
    gold = random.randint(5, 100)
    enemy = {
        "hp": character['max_hp'] / 2 + buff,
        "max_hp": character['max_hp'] / 2 + buff,
        "gold": gold,
        "level": 1,
        "xp": character['max_hp'] / 2 + buff * .2,
        "base_attack": character['level'],
        "base_defense": 1,
        "name": enemy_name(),
    }
    return enemy


def attack(character, enemy):
    character_attack_type = [f'You summon all of your courage and claw at {enemy["name"]}\'s eyes!',
                             f'You lung at the {enemy["name"]} and kick it in the arm.',
                             f'{enemy["name"]} is no match for your haymaker!',
                             f'You faint toward {enemy["name"]}\'s left and ruthlessly sweep the leg!',
                             f'POCKET SAND!!!']
    enemy_attack_type = [f'{enemy["name"]} spits in your eye!',
                         f'{enemy["name"]} lets out a blood curdling shriek and stomps on your toe!',
                         f'{enemy["name"]} pulls your hair!',
                         f'{enemy["name"]} walks slowly in front of the tv enraging you!',
                         f'{enemy["name"]} tells you a cringy dad joke!']

    # You [Random attack Name] and do X damage!
    print(random.choice(character_attack_type))
    print(f'For {character["base_attack"]} damage!')
    enemy['hp'] -= character['base_attack']
    if enemy['hp'] < 1:
        """You Killed The Enemy"""
        print(f'You Defeated the {enemy["name"]}!')
        print(f"You receive {enemy['max_hp'] / 3}, {enemy['gold']} Gold")
        character['xp'] += enemy['max_hp'] / 3
        character['gold'] += enemy['gold']
        clear()
        main_menu(character)

    # The [Enemy Name] doesn't like that and [Random attack name] back for X Damage!
    print(random.choice(enemy_attack_type))
    print(f'For {enemy["base_attack"]} damage!')
    character['hp'] -= enemy['base_attack']
    # If character dies
    if character['hp'] < 1:
        print("It just wasn't your day for adventuring. . . \n")
        choices = int(input("Do you want to try again? <y,n> : "))
        match choices:
            case 'y':
                start()
            case 'n':
                print("Thanks for playing!")
                quit()
            case _:
                print("You seem upset. . . we should probably quit for now.")
                quit()

    clear()
    find_fight(character, enemy)


def heal(character, enemy):
    if character['mp'] >= character['spells']['heal']:
        character['hp'] = character['max_hp']
        character['mp'] -= character['spells']['heal']
        clear()
        return find_fight(character, enemy)


def find_fight(character, enemy=None):
    if not enemy:
        enemy = get_enemy(character)
    observation = [f"You Kick the grass and a {enemy['name']} jumps out at you!",
                   f"You head deep into the woods and a {enemy['name']} jumps from behind a tree!",
                   f"A wild {enemy['name']} appears!",
                   f"It doesn't take long before you're attacked by a {enemy['name']}!"]

    print(f"\n{random.choice(observation)}\n")
    print("\n".join([f"{enemy['name']} Stats:\n",
                     f"- HP: {enemy['hp']}",
                     f"- Gold: {enemy['gold']}",
                     f"",
                     ]))

    print("\n".join(["",
                     "1. Attack!",
                     "2. Heal [6mp]",
                     "3. Flee",
                     "",
                     ]))
    print_stats(character)
    choice = int(input(f"What do you want to do {character['name']}?: "))

    match choice:
        case 1:
            attack(character, enemy)
            pass
        case 2:
            heal(character, enemy)
            pass
        case 3:
            pass
        case _:
            find_fight(character, enemy)


    main_menu(character)


def take_nap(character):
    pprint(character)
    return character


def main_menu(character):
    clear()
    observations = ["You find yourself on a dusty road. It doesn't look like there's much around.",
                    "You look up and see the sky grow dark. It's probably going to rain.",
                    "The sun is high in the sky, and it looks like a great day for adventure!",
                    "You can feel a bit of a pain in your stomach. Adventuring is hard work."]
    print("\n".join(["", random.choice(observations),
                     "",
                     "1. Look for a town.",
                     "2. Find something to kill!",
                     "3. Take a nap",
                     "",
                     ]
                    )
          )
    print_stats(character)
    try:
        choice = int(input(f"What Do you want to do {character['name']}?: "))
    except ValueError:
        choice = None
    match choice:
        case 1:
            clear()
            find_town(character)
        case 2:
            clear()
            find_fight(character)
        case 3:
            clear()
            take_nap(character)
        case _:
            clear()
            print("\n")
            print(random.choice(bad_entry), "\n")
            main_menu(character)


def print_stats(character, **kwargs):
    try:
        if kwargs['extended']:
            print("Current Stats:\n")
            for key, value in character.items():
                print(f"{key.upper()} - {value}")
    except KeyError:
        print(f"[LV {character['level']}] [HP {character['hp']}] [MP {character['mp']}] [{character['gold']}g]")

def start():
    intro()
    character = new_character()
    main_menu(character)

if __name__ == '__main__':
    start()