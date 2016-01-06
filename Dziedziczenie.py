class A:
    def __str__(self):
        return "Jestem wesolym obiektem klasy A"

    def __len__(self):
        return 6

    def __gt__(self, other): #metoda zwracajaca wartosc logiczna  PRZECIAZENIE OPERATORA
        return True

class B(A):
    def __init__(self):
        A.__init__()
    def __len__(self):
        return 7

b = B()
print(b)
""" zmiany"""
""" kolejne zmiany"""