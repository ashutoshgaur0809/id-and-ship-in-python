dict = {'B': 'BattleShip', 'b': 'BattleShip', 'C': 'Cruiser',
        'c': 'Cruiser', 'd': 'Destroyer', 'D': 'Destroyer', 'f': 'Frigate', 'f': 'Frigate'}
T = int(input("Enter how many test cases you want = "))
for i in range(T):
    a = input()
    print(dict[a])
