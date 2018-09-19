import random

class Ability:
    def __init__(self, name, attack_strength):
        # TODO: Set Ability name
        self.name = name
        # TODO: Set attack strength
        self.attack_strength = attack_strength

    def attack(self):
        # TODO: Calculate lowest attack value as an integer.
        # TODO: Use random.randint(a, b) to select a random attack value.
        # TODO: Return attack value between 0 and the full attack.
        return random.randint(self.attack_strength // 2 , self.attack_strength)



    def update_attack(self, attack_strength):
        # TODO: update the value of the current attack strength with the new value passed in as a parameter.
        self.attack_strength = attack_strength


class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.ability.append(ability)

    def attack(self):
        # Call the attack method on every ability in our ability list
        for ability in self.abilities:
        # Add up and return the total of all attacks



if __name__ == "__main":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
