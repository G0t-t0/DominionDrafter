class Cartes:
    "carte dominion"

    def __init__(self, nom, type, cout:int, effet):
        print("création de la carte "+nom)
        self.nom = nom
        self.type = type
        self.cout = cout
        self.effet = effet

chapelle=Cartes("chapelle", "action", 2, "écartez jusqu'à 4 cartes de votre main")
print(chapelle.nom+" / "+chapelle.effet)