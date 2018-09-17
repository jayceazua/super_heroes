import random

class Ability:
    def __init__(self, name, attack_strength): # Initalize starting values
        # Set Ability name
        self.name = name
        # Set attack strength
        self.attack_strength = attack_strength

    def attack(self): # Return attack value
        # Calculate lowest attack value as an integer
        full_attack = 20
        lowest_attack = full_attack // 2
        # Use random.randit(a, b) to select a random attack value.
        attack_value = random(lowest_attack, full_attack)
        # Return attack value between 0 and the full attack
        return attack_value


    def update_attack(self, attack_strength): # Update attack value
        attack_value = attack_strength


class Weapon(Ability):
    
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """


class Team:
    def init(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

    def view_all_heroes(self):
        """Print out all heroes to the console."""

class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = list() self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self): # Run attack() on every ability hero has
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attacks

if name == "__main__": # If you run this file from the terminal this block is executed.
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
