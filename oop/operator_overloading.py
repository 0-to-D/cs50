class Vault:
    def __init__(self, gallon=0, sickle=0, knuts=0):
        self.gallon = gallon
        self.sickle = sickle
        self.knuts = knuts

    def __str__(self):
        return f"gallons:{self.gallon}; sickles:{self.sickle}; knuts:{self.knuts}"
    
    def __add__(self, others):
        gallons = self.gallon + others.gallon
        sickles = self.sickle + others.sickle
        knuts = self.knuts + others.knuts
        return Vault(gallons, sickles, knuts)
        
potter = Vault(100, 50, 10)
print(potter)

draco = Vault(1000, 100, 10)
print(draco)

total = potter + draco
print(total)






