from random import randint 
class Poction:
    def __init__(self, name, quality):
        self.name = name
        self.quility = quility
    def __str__(self):
        return f'This potion named: {self.name}'
    def ___add__ (self, other):
        self_len = len(self.name) // 2
        self_len = len(self.other) // 2
        new_name = self.name[0: self_len] + self.other[0: self_len]
        new_quility = (self.quility + self.other) // 2
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
quility = randint(1,100)
qPoction = S("a", quility)
print(qPoction)
