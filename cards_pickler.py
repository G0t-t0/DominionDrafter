import pickle

class Cartes:
    "carte dominion"

    def __init__(self, nom, types, cout:int, effet):
        print("création de la carte "+nom)
        self.nom = nom
        self.types = types
        self.cout = cout
        self.effet = effet
        cartes.append(self)

cartes=[]

chapelle=Cartes("chapelle", ['action'], 2, "écartez jusqu'à 4 cartes de votre main")
cave=Cartes("cave", ['action'], 2, "+1 action. Défaussez autant de cartes que vous voulez, puis piochez-en le même nombre")
douves=Cartes("douves", ['action', 'réaction'], 2, "+2 cartes. Quand un autre joueur joue une carte attaque, vous pouvez révéler cette carte de votre main, vous n'êtes pas affecté")
village=Cartes("village", ['action'], 3, "+1 carte. +2 actions")
atelier=Cartes("atelier", ['action'], 3, "obtenez une carte coûtant jusque 4")
chancelier=Cartes("chancelier", ['action'], 3, "+2 sous. Vous pouvez immédiatement défausser votre deck")
bucheron=Cartes("bucheron", ['action'], 3, "+1 achat. +2 sous")
bureaucrate=Cartes("bureaucrate", ['action', 'attaque'], 4, "Placez une carte argent sur votre deck. Chaque joueur adverse révèle une carte victoire de sa main et la place sur son deck (ou révèle sa main s'il n'a pas de carte victoire")
jardins=Cartes("jardins", ['victoire'], 4, "vaut 1 victoire pour chaque 10 cartes dans votre deck (arrondi à l'inférieur)")
milice=Cartes("milice", ['action', 'attaque'], 4, "+2 sous. Chaque autre joueur défausse sa main pour n'avoir plus que 3 cartes dans sa main")
preteur_sur_gages=Cartes("preteur_sur_gages", ['action'], 4, "Ecartez une carte cuivre de votre main, +3 sous")
renovation=Cartes("renovation", ['action'], 4, "Ecartez une carte de votre main. Obtenez une carte coûtant jusqu'à 2 sous de plus")
forgeron=Cartes("forgeron", ['action'], 4, "+3 cartes")
voleur=Cartes("voleur", ['action', 'attaque'], 4, "chaque autre joueur révèle les deux premières cartes de son deck. S'il y a des cartes trésor parmi les cartes révélées, ils en écartent une de votre choix. Vous pouvez obtenir une ou plusieurs des cartes écartées. Les autres cartes sont défaussées")
espion=Cartes("espion", ['action', 'attaque'], 4, "+1 carte. +1 action. Chaque joueur révèle la première carte de son deck. choisissez si chacun la défausse ou la replace au dessus")
festin=Cartes("festin", ['action'], 4, "écartez cette carte. Obtenez une carte coûtant jusque 5 sous")
salle_du_trone=Cartes("salle_du_trone", ['action'], 4, "choisissez une carte action de votre main, jouez la deux fois")
chambre_du_conseil=Cartes("chambre_du_conseil", ['action'], 5, "+4 cartes. +1 achat. chaque autre joueur pioche une carte")
festival=Cartes("festival", ['action'], 5, "+2 actions. +1 achat. +2 sous")
laboratoire=Cartes( "laboratoire", ['action'], 5, "+2 cartes. +1 action")
bibliotheque=Cartes("bibliotheque", ['action'], 5, "piochez jusqu'à avoir 7 cartes dans votre main. Vous pouvez placez sur le côté n'importe quelle carte action que vous piochez de cette façon. défaussez les cartes cartes mises de côté quand vous avez fini de piocher")
marche=Cartes("marche", ['action'], 5, "+1 carte. +1 action. +1 achat. +1 sous")
mine=Cartes("mine", ['action'], 5, "écartez une carte trésor de votre main. Obtenez une carte trésor coûtant jusque 3 sous de plus et placez la dans votre main")
sorciere=Cartes("sorciere", ['action'], 5, "+2 cartes. chaque autre joueur obtient une malédiction")
aventurier=Cartes("aventurier", ['action'], 6, "révélez les cartes de votre deck jusqu'à ce que vous ayiez révélé 2 cartes trésor. Places les cartes trésor dans votre main et les autres dans la défausse")

pickle.dump(cartes, open('cards.pickle', 'wb'))

cartes = pickle.load(open("cards.pickle", "rb"))

print(cartes[0].nom)