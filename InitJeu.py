import random

#Fonction EstNonOccupe renvoie vrai si la piece est 
def EstOccupe(List,i):
	return (List[i]!="")

#Retourne l'indice d'une case inoccupee
def TrouveCaseVide(listePieces):
	flag = True
	indice = 0
	while(flag):
		indice = random.randint(0,11)
		flag = EstOccupe(listePieces,indice)
	print " i : "+str(indice)
	return indice

#Initialisation du labyrinthe
def InitLabyrinth():
	#creation de la liste de pieces
	listePieces=[1,2,3,4,5,6,7,8,9,10,11,12]
	for i in range(12):
		listePieces[i]=""
	print listePieces

	#positionner les pieges
	iC1 = TrouveCaseVide(listePieces) #chauve souris 1
	listePieces[iC1]="C1"
	iC2 = TrouveCaseVide(listePieces) #chauve souris 2
	listePieces[iC2]="C2"
	iP1 = TrouveCaseVide(listePieces) #puit 1
	listePieces[iP1]="P1"
	iP2 = TrouveCaseVide(listePieces) #puit 2
	listePieces[iP2]="P2"
	iW = TrouveCaseVide(listePieces) #Wum Pus
	listePieces[iW]="iW"
	iX1 = TrouveCaseVide(listePieces) #Joueur 1
	listePieces[iX1]="X1"

	return listePieces


nbFleches = 3
labyrinthe = InitLabyrinth()
print labyrinthe