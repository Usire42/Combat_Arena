from Fighter import Fighter
from Kostka import Kostka
from Arena import Arena

def main():
    Zalgoren = Fighter("Zalgoren", 100, 20, 10, 10,6)
    Shadow = Fighter("Shadow", 100, 20, 10, 6, 10)

    Arena(Zalgoren, Shadow).fight()







if __name__ == '__main__':
    main()