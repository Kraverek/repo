class koszyk:
	def __init__ (self):
		self.koszyk = []
	def dodaj(self,obiekt):
		self.koszyk.append(obiekt)
	def rozmiar(self):
		return len(self.koszyk)

s = koszyk()
s.dodaj("pierwszy wpis")
s.dodaj("drugi wpis")
print (s.__dict__)