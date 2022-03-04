from random import randint


class Poction:
    def __init__(self, name, quality):
        self.name = name
        self.quility = quility
        
    def __str__(self):
        return f'This potion named: {self.name}'
    
    def __add__(self, other):
        self_len = len(self.name) // 2
        other_len = len(other.name) // 2
        new_name = self.name[0:self_len] + other.name[0:other_len]
        new_quility = (self.quility + other.quility) // 2
        return Poction(new_name, new_quility)

    def __sub__(self, other):
        new_quility = (self.quility + other.quility) // 2
        return Poction(self.name, new_quility)
    
    def check_quility(self):
        if self.quility < 75:
            print("больше 75(не вкл)")
        elif self.quility > 50:
            print("от 50(не вкл) до 75(вкл)")
        else:
            print("меньше или ровно 50")
            
class S(Poction):
    def special(self):
        return S(self.name, self.quility + 20)
    
class NotS(Poction):
    def special(self):
        return S(self.name, self.quility - 20)
    
quility = randint(1,100)
qPoction = S("a", quility)
print(qPoction)
game = True
potions = {}
while game:
    potion = input(f"What potion do you want to make? q - for quality, n - for non quality").lower()
    if potion == "exit":
        game = False
    else:
        potion_name = input("Enter potion name: ")
        potion_quality = randint(1,100)
        if potion == "q":
            new_potion = S(potion_name, potion_quality)
        elif potion == "n":
            new_potion = NotS(potion_name, potion_quality)
        potions[potion_name] = new_potion
    if len(potions) >= 2:
        action = input(f'(Add("+") or Sub("-") yuor potions?')
        potion1 = potions.popitem()[1]
        potion2 = potions.popitem()[1]

        if action == "+":
            mixed_potion = potion1 + potion2
        elif action == "-":
            mixed_potion = potion1 - potion2
        print("Start mixin potions...")
        
        if mixed_potion.quility < 10:
            print("Kaboom! Potion exploded! You die...")
            game = False
        else:
            potions[mixed_potion.name] = mixed_potion
            print(f"Your potions: {potions.keys()}")
            print(f"POrion quality: {mixed_potion.quility}, Be careful next time!")
