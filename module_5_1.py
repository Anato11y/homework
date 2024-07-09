# 1
class House:
# 2
    def __init__(self, name, number_of_floors):
# 3
        self.name = name
        self.number_of_floors = number_of_floors
# 4
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


# 5
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# 6
h1.go_to(5)
h2.go_to(10)