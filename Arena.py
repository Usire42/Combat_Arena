
class Arena:

    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2


    def fight(self):
        fighters = [self.fighter1, self.fighter2]
        while not self.fighter1.is_dead() and not self.fighter2.is_dead():
            # roll for initiative every round
            for fighter in fighters:
                fighter.initiative_roll()

            # sort fighters by initiative
            fighters = sorted(fighters, key=lambda figter: figter.initiative, reverse=True)

            # fight
            for fighter in fighters:

                #get index of fighter
                fighter_index = fighters.index(fighter)
                next_fighter_index = (fighter_index + 1) % 2

                # define attacker and defender
                fighter.attack_opponent(fighters[next_fighter_index])
                print(fighter._get_combat_Messages())
                print(fighters[next_fighter_index]._get_combat_Messages())

                #check if defender is dead
                if fighters[next_fighter_index].is_dead():
                    break
