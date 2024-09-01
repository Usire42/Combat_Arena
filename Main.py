from Fighter import Fighter
from Kostka import Kostka

def main():
    bojovnik = Fighter("Zalgoren", 100, 20, 10, 10,6)
    print(f"Bojovník: {bojovnik.name}")  # test __str__()
    print(f"Mrtev: {bojovnik.is_dead()}")  # test naživu
    bojovnik.health -=23
    print(f"Život: {bojovnik.life_bar()}")  # test graficky_zivot()







if __name__ == '__main__':
    main()