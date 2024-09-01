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
        self._message = ""


#    def __str__(self):
#        return str(self.name)

    # set attack values
    def attack_opponent(self, opponent):
        attack_current = Kostka(self.attack_dice).roll() + self.attack
        print(self.name + " attacks " + opponent.name + " with " + str(attack_current))
        opponent.take_damage(attack_current)
        #return attack_current

    # set defense values
    def defend(self):
        current_defense = Kostka(self.defense_dice).roll() + self.defense
        return current_defense

    # take damage
    def take_damage(self, damage):
        # calculate damage
        defended = self.defend()
        # check if damage is greater than defense
        wound = damage - defended
        # check if damage is positive
        if wound > 0:
            wounded = wound
            attack_message = (self.name + " takes " + str(wound) + " damage")
        else:
            wounded = 0
            attack_message = (self.name + " takes no damage")
        self.health -= wounded
        # check if dead
        if self.is_dead():
            attack_message = (self.name + " has died")
        self._set_combat_Messages(attack_message,self.life_bar())



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

    def _set_combat_Messages(self, message, hp_bar):
        self._message = message

    def _get_combat_Messages(self):
        return f'{self._message} \n {self.life_bar()}'