from pprint import pprint
import random
import os
import time
from colorama import init
from colorama import Fore, Back, Style


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
    print(Fore.MAGENTA + """\nWelcome To Adventure Land.\nYou're not sure how you got here, but you do remember your name.""")  # Press Ctrl+F8 to toggle the breakpoint.


def new_character():
    name = input(Fore.BLUE + "\nWhat is your name?: ")

    character = {
        "hp": 100,
        "max_hp": 100,
        "mp": 10,
        "max_mp": 10,
        "gold": 100,
        "level": 1,
        "xp": 0,
        "base_attack": 10,
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
                character['mp'] = character['max_mp']
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
    try:
        choice = int(input(Fore.BLUE + f"What Do you want to do? [{character['gold']}G]: "))
    except ValueError:
        choice = None
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
    print("\n".join(["",Fore.MAGENTA + random.choice(observations),
                    Fore.LIGHTWHITE_EX + "",
                     "1. Head to the shop.",
                     "2. Go to the Inn",
                     "3. Leave Town",
                     Fore.RESET + "",
                     ]
                    )
          )
    print_stats(character)
    try:
        choice = int(input(Fore.BLUE + f"What Do you want to do {character['name']}?: "))
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
        "hp": int(character['max_hp'] / 2 + buff),
        "max_hp": character['max_hp'] / 2 + buff,
        "gold": gold,
        "level": 1,
        "xp": character['max_hp'] / 2 + buff * .2,
        "base_attack": buff,
        "base_defense": 1,
        "name": enemy_name(),
    }
    return enemy


def level_up(character):
    while character['xp'] > 99:
        character['xp'] -= 100
        character['level'] += 1
        character['max_hp'] += random.randint(5, 10)
        character['max_mp'] += random.randint(1, 4)
        character['base_attack'] += random.randint(5, 10)
        character['base_defense'] += random.randint(5, 10)

        print("You Leveled UP!")


def attack(character, enemy):
    character_attack_type = [f'You summon all of your courage and claw at {enemy["name"]}\'s eyes!',
                             f'You lunge at the {enemy["name"]} and kick it in the arm.',
                             f'{enemy["name"]} is no match for your haymaker!',
                             f'You faint toward {enemy["name"]}\'s left and ruthlessly sweep the leg!',
                             f'POCKET SAND!!!']
    enemy_attack_type = [f'{enemy["name"]} spits in your eye!',
                         f'{enemy["name"]} lets out a blood curdling shriek and stomps on your toe!',
                         f'{enemy["name"]} pulls your hair!',
                         f'{enemy["name"]} walks slowly in front of the tv enraging you!',
                         f'{enemy["name"]} tells you a cringy dad joke!']

    # You [Random attack Name] and do X damage!
    clear()
    print(Fore.MAGENTA + random.choice(character_attack_type))
    print(Fore.LIGHTRED_EX + f'For {character["base_attack"]} damage!\n')
    print(Fore.MAGENTA)
    enemy['hp'] -= character['base_attack']
    if enemy['hp'] < 1:
        """You Killed The Enemy"""
        print(f'You Defeated the {enemy["name"]}!')
        print(f"You receive {int(enemy['max_hp'] / 3)} XP, {enemy['gold']} Gold")
        character['xp'] += int(enemy['max_hp'] / 3)
        character['gold'] += enemy['gold']
        level_up(character)
        main_menu(character, draw_clear=False)

    # The [Enemy Name] doesn't like that and [Random attack name] back for X Damage!
    print(random.choice(enemy_attack_type))
    print(Fore.LIGHTRED_EX + f'For {enemy["base_attack"]} damage!\n')
    character['hp'] -= enemy['base_attack']
    # If character dies
    if character['hp'] < 1:
        print("It just wasn't your day for adventuring. . . \n")
        choices = input("Do you want to try again? <y,n> : ")
        match choices:
            case 'y':
                start()
            case 'n':
                print("Thanks for playing!")
                quit()
            case _:
                print("You seem upset. . . we should probably quit for now.")
                quit()

    find_fight(character, enemy, new=False)


def heal(character, enemy):
    if character['mp'] >= character['spells']['heal']:
        character['hp'] = character['max_hp']
        character['mp'] -= character['spells']['heal']
        clear()
        print(f"You heal yourself!")
        find_fight(character, enemy, new=False)
    else:
        clear()
        print("You wave your hand confidently shouting Abbra Kadabra!! But nothing happens. . .")
        find_fight(character, enemy, new=False)


def find_fight(character, enemy=None, new=True):
    if not enemy:
        enemy = get_enemy(character)
    observation = [f"You Kick the grass and a {enemy['name']} jumps out at you!",
                   f"You head deep into the woods and a {enemy['name']} jumps from behind a tree!",
                   f"A wild {enemy['name']} appears!",
                   f"It doesn't take long before you're attacked by a {enemy['name']}!"]
    if new:
        print(Fore.MAGENTA + f"\n{random.choice(observation)}\n")
    print("\n".join([Fore.MAGENTA + f"{enemy['name']} Stats:\n",
                     Fore.LIGHTGREEN_EX + f"- HP: {enemy['hp']}",
                     Fore.LIGHTYELLOW_EX + f"- Gold: {enemy['gold']}",
                     Fore.RESET + f"",
                     ]))

    print("\n".join(["",
                     Fore.RED + "1. Attack!",
                     Fore.GREEN + "2. Heal [6mp]",
                     Fore.YELLOW + "3. Flee",
                     "",
                     ]))
    print_stats(character)
    try:
        choice = int(input(Fore.BLUE + f"What do you want to do {character['name']}?: "))
    except ValueError:
        choice = None
    match choice:
        case 1:
            attack(character, enemy)
            pass
        case 2:
            heal(character, enemy)
            pass
        case 3:
            clear()
            print('\nYou tuck tail and run. . . bringing shame upon your family name.')
            character['name'] += " The Coward"
            main_menu(character, draw_clear=False)
        case _:
            clear()
            print("\n")
            print(random.choice(bad_entry), "\n")
            find_fight(character, enemy, new=False)


    main_menu(character)


def take_nap(character):
    observation = ['You find a shade tree and close your eyes for a second.',
                   'You collapse from exhaustion in middle of the road and don\'t even care.',
                   'Shouldn\'t you find an inn?']
    clear()
    print(Fore.MAGENTA + random.choice(observation))
    print(Fore.RESET)
    main_menu(character, draw_clear=False)


def main_menu(character, draw_clear=True):
    if draw_clear:
        clear()
    observations = ["You find yourself on a dusty road. It doesn't look like there's much around.",
                    "You look up and see the sky grow dark. It's probably going to rain.",
                    "The sun is high in the sky, and it looks like a great day for adventure!",
                    "You can feel a bit of a pain in your stomach. Adventuring is hard work."]
    print("\n".join(["", Fore.MAGENTA + random.choice(observations),
                     Fore.LIGHTWHITE_EX + "",
                     "1. Look for a town.",
                     "2. Find something to kill!",
                     "3. Take a nap",
                     Fore.RESET + "",
                     ]
                    )
          )
    print_stats(character)
    try:
        choice = int(input(Fore.BLUE + f"What Do you want to do {character['name']}?: "))
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
            main_menu(character, draw_clear=False)


def print_stats(character, **kwargs):
    try:
        if kwargs['extended']:
            print("Current Stats:\n")
            for key, value in character.items():
                print(f"{key.upper()} - {value}")
    except KeyError:
        print(Fore.CYAN + f"[LV {character['level']}] [XP {character['xp']}/100] [HP {character['hp']}] [MP {character['mp']}] [{character['gold']}g]")
        print(Fore.RESET)


def start():
    init()  # Initilize Colorama
    intro()
    character = new_character()
    main_menu(character)


if __name__ == '__main__':
    start()