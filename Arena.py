
class Arena:

    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2


    def fight(self):
        while not self.fighter1.is_dead() and not self.fighter2.is_dead():
            self.fighter1.attack_opponent(self.fighter2)
            self.fighter2.attack_opponent(self.fighter1)
