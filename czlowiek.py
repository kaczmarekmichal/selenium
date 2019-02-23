class Czlowiek():
    def __init__(self, imie):
    #    print("wywoluje sie konstruktor")
        self.imie=imie
    gatunek="human"
    def jump(self):
        print('podskoczylem!')
    def __del__(self):
        print("narazie")


class Dziecko(Czlowiek):
    def bawimy_sie(self):
        print("juhu")



#tworzenie instancji

marcin=Czlowiek('marcin')
marcin.jump()
print(marcin.imie)

print(marcin.gatunek)

basia=Czlowiek('basia')

barcin=Dziecko('barcin')

barcin.bawimy_sie()
