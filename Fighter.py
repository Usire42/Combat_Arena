#imports
import random
from Kostka import Kostka

class Fighter:
    def __init__(self, name, health, attack, defense, attack_dice, defense_dice):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attack_dice = attack_dice
        self.defense_dice = defense_dice
        self.max_hit_blocs = 10


#    def __str__(self):
#        return str(self.name)

    # set attack values
    def attack_opponent(self):
        attack_current = Kostka(self.attack_dice).roll() + self.attack
        return attack_current

    # set defense values
    def defend(self):
        current_defense = Kostka(self.defense_dice).roll() + self.defense
        return current_defense

    # take damage
    def take_damage(self, damage):
        defended = self.defend()
        # check if damage is greater than defense
        wound = damage - defended
        wounded = {wound <= 0: 0}.get(wound)
        self.health -= wounded
        # check if dead
        if self.is_dead():
            print(self.name + " has died")
        print(self.life_bar())



    # check if dead
    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    # visualize life bar
    def life_bar(self):
        hit_blocks = int((self.health / self.max_health) * self.max_hit_blocs)
        if not self.is_dead() and hit_blocks <= 0:
            hit_blocks = 1
        hp_string = f"[{'#' * hit_blocks}{'_' * (self.max_hit_blocs - hit_blocks)}]"
        return hp_string

