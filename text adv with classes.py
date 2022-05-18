import random


# """
# enemy_evasion_chance only checks whether enemy dodges the users attack or if the enemy takes damage
# """


def enemy_evasion_chance(enemy):
    dodge_roll = random.randint(1, 5)
    print(dodge_roll)
    if dodge_roll <= 3:
        enemy.health -= elf_hero.attack()
        print("strike successful, is the enemies new health", enemy.health)
    else:
        print("you missed")


# """
# character_evasion chance as long as enemy health and users health is above 0 the encounter continues.
# encounter_two is called when enemy health is less than 0 breaking the loop. Randomly rolls a number
# and determines whether you dodge enemies attack or take damage based on this.
# """


def character_evasion_chance(enemy):
    while enemy.health > 0:
        if elf_hero.health < 0:
            print("ran out of health")
            exit()
        dodge_roll = random.randint(1, 5)
        print(dodge_roll)
        if dodge_roll <= 3:
            print("You evaded the enemies attack, you try your attack")
            enemy_evasion_chance(enemy)
        elif dodge_roll > 3:
            elf_hero.health -= 40
            print("you take a hit and lose some health", "your new health is", elf_hero.health)
            enemy_evasion_chance(enemy)


def scene_two():
    print("\nyou killed the monster but now run into a bear!")
    print("you still have ", elf_hero.health, " health left ")
    input("continue?")
    character_evasion_chance(enemy_two)


def first_encounter():
    print(""" you run into a goblin
a) hit    
    """)
    user = input("abc").lower()
    if user == "a":
        character_evasion_chance(enemy_one)


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


enemy_one = Enemy(200, 30)
enemy_two = Enemy(300, 40)


class Hero:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self):
        self.weapon = 40
        return self.weapon


# """
# start game
# """

user = input("which hero do you select: elf: ").lower()

elf_hero = Hero("jeff", 150, "sword")
if user == "elf":
    print("your hero's name is", elf_hero.name, "health", elf_hero.health, "weapon", elf_hero.weapon)

first_encounter()

scene_two()

# """
# Issues i had:
# doesnt work with if user == 1 or 2 or 3. needed to use user>=3.
# got 3 errors when using plus to concatenate object with strings
# you take a hit and lose some health","your new health is" + elf_hero.health
# use a comma to solve this!
# """

# """
# worked it out. make the character_evasion function take in (enemy) argument.
# then input enemy_one when you need it. then when u call 2nd encounter
# pass in enemy_two. same with enemy evasion chance pass in the (enemy)
# so it reuses the same function for the entire process. Could also
# have made another function to solve this but unnecessary. It would not go to encounter 2 without this
# as enemy_one health would be 0. so it would exit.
# """
