class UFO:
    ilosc = 0
    max_predkosc = 0
    biegi = 0
    predkosc = 0
    bieg = 0
    ruch = 0
    ilosc_ludzi = 0
    def __init__(self):
        self.UFO = 0
    def ilosc_kol(self,ilosc):
        self.ilosc = ilosc
    def max_predkosc(self,max_predkosc):
        self.max_predkosc = max_predkosc
    def ilosc_biegow(self,biegi):
        self.biegi = biegi
    def predkosc(self,predkosc):
        self.predkosc = predkosc
    def bieg(self,bieg):
        self.bieg = bieg
    def ilosc_ludzi_w_klatce(self,ilosc_ludzi):
        self.ilosc_ludzi = ilosc_ludzi
    def ruch(self,ruch):
        self.ruch = ruch

class FIAT(UFO):
    def __init__(self):
        UFO.__init__(self)
    opis = 'Zwolnij!'

class OPEL(UFO):
    def __init__(self):
        UFO.__init__(self)
    ilosc = 5
    biegi = 5
    ruch = 2

class BMW(UFO):
    def __init__(self):
        UFO.__init__(self)
    opis = 'Szybciej!'

class SAMOLOT(UFO):
    def __init__(self):
        UFO.__init__(self)
    opis = 'Wystartuj'


f = FIAT()
f.ilosc_ludzi_w_klatce(10)
print ("Ilosc ludzi w klatce:")
print (f.ilosc_ludzi)
print (f.opis)
print ("")

o = OPEL()
print ("Ilosc biegow:")
print (o.biegi)
print ("")

s = SAMOLOT()
print (s.opis)
print ("Predkosc samolotu")
s.predkosc(160)
print (s.predkosc)
print ("km/h")
