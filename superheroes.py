import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return random.randint(self.attack_strength // 2 , self.attack_strength)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        power = 0
        for ability in self.abilities:
            power += ability.attack()
        return power

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        defense_points = 0

        if self.health <= 0:
            return int(defense_points)
        else:
            for armor in self.armors:
                defense_points += armor.defense
        return int(defense_points)

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

    def add_armor(self, armor):
        """
            This was not in the tutorial to add and append the armor.
        """
        self.armors.append(armor)


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        return random.randint(0, self.attack_strength)


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        return random.randint(0, self.defense)


class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if hero.name is name:
                self.heroes.remove(hero)
        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero  in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        total_attack = 0
        for hero in self.heroes:
            total_attack += hero.attack()
        self.update_kills(other_team.defend(total_attack))


    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()
        excess_damage = damage_amt - total_defense
        return self.deal_damage(excess_damage)

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        deaths = 0
        damage_amt = damage // len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(damage_amt)
            if hero.health <= 0:
                self.remove_hero(hero.name)
                deaths += 1
        return deaths

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        for hero in self.heroes:
            ratio = (hero.kills / hero.deaths) * 100
            print(ratio)


    def update_kills(self, num_kills):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            hero.add_kill(num_kills)



class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_armor(self):
        armors = [
            "Calculator",
            "Laser Shield",
            "Invisibility",
            "SFPD Strike Force",
            "Social Workers",
            "Face Paint",
            "Damaskus Shield",
            "Bamboo Wall",
            "Forced Projection",
            "Thick Fog",
            "Wall of Will",
            "Wall of Walls",
            "Obamacare",
            "Thick Goo"]
        name = armors[random.randint(0, len(armors) - 1)]
        power = random.randint(23, 700000)
        return Armor(name, power)


    def create_weapon(self):
        weapons = [
            "Antimatter Gun",
            "Star Cannon",
            "Black Hole Ram Jet",
            "Laser Sword",
            "Laser Cannon",
            "Ion Accellerated Disc Drive",
            "Superhuman Strength",
            "Blinding Lights",
            "Ferociousness",
            "Speed of Hermes",
            "Lightning Bolts"]
        name = weapons[random.randint(0, len(weapons) - 1)]
        power = random.randint(27, 700000)
        return Weapon(name, power)


    def create_ability(self):
        abilities = [
            "Alien Attack",
            "Science",
            "Star Power",
            "Immortality",
            "Grandmas Cookies",
            "Blinding Strength",
            "Cute Kittens",
            "Team Morale",
            "Luck",
            "Obsequious Destruction",
            "The Kraken",
            "The Fire of A Million Suns",
            "Team Spirit",
            "Canada"]
        name = abilities[random.randint(0, len(abilities) - 1)]
        power = random.randint(45, 700000)
        return Ability(name, power)

    def create_hero(self):
        heroes = [
            "Athena",
            "Jodie Foster",
            "Christina Aguilera",
            "Gamora",
            "Supergirl",
            "Wonder Woman",
            "Batgirl",
            "Carmen Sandiego",
            "Okoye",
            "America Chavez",
            "Cat Woman",
            "White Canary",
            "Nakia",
            "Mera",
            "Iris West",
            "Quake",
            "Wasp",
            "Storm",
            "Black Widow",
            "San Luis Obispo",
            "Ted Kennedy",
            "San Francisco",
            "Bananas"]
        name = heroes[random.randint(0, len(heroes) - 1)]
        power = random.randint(3, 700000)
        hero = Hero(name, power)
        for _ in range(3):
            hero.add_ability(self.create_ability())
        hero.add_ability(self.create_weapon())
        hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        teams = [
            "Orchids",
            "Red",
            "Blue",
            "Cheese Steaks",
            "Warriors",
            "49ers",
            "Marvel",
            "DC",
            "Rat Pack",
            "The Little Red Riding Hoods",
            "Team One",
            "Generic Team",
            "X-men",
            "Team Two",
            "Golden Champions",
            "Vegan Protectors",
            "The Cardinals",
            "Winky Bears",
            "Steelsmiths",
            "Boilermakers",
            "Nincompoops"]
        name = teams[random.randint(0, len(teams) - 1)]
        self.team_one = Team(name)
        for _ in range(5):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        teams = ["Orchids", "Red", "Blue", "Cheese Steaks", "Warriors", "49ers",
            "Marvel", "DC", "Rat Pack", "The Little Red Riding Hoods", "Team One",
            "Generic Team", "X-men", "Team Two", "Golden Champions", "Vegan Protectors",
            "The Cardinals", "Winky Bears", "Steelsmiths", "Boilermakers", "Nincompoops"]
        name = teams[random.randint(0, len(teams) - 1)]
        self.team_two = Team(name)
        for _ in range(5):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        while len(self.team_one.heroes) != 0 and len(self.team_two.heroes) != 0:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            # Team 2 fight
        winner = self.team_one.name if len(self.team_two.heroes) == 0 else self.team_two.name
        print(winner, "won!")

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        pass

if __name__ == "__main__":
    # Instantiate Game Arena
    arena = Arena()
    game_is_running = True
    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
