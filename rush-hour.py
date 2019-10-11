from tkinter import *


with open("Levels.txt", "r") as fichier :
	levels = fichier.read()

levels = levels.split("\n")
i = 0
while i < len(levels) :
	levels[i] = levels[i][5:]
	levels[i] = levels[i].split()
	i += 1

colors = ('green','yellow','purple','blue','orange','pink','brown','red','grey','cyan','plum','salmon','beige', 'greenyellow')

largeur_grille = 500
hauteur_grille = 500
nb_colonnes = 6
nb_lignes = 6
largeur_case = largeur_grille / nb_colonnes
hauteur_case = hauteur_grille / nb_lignes
win_toggle = False

nb_coups = 0

def choix_level(n) :

	global veh_xy

	choix = levels[n]

	lettres = ("Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M")

	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	veh_xy = []
	presence = False

	compteur_lettre = 0
	for lettre in lettres :
		nb_lettre = 0
		ligne = 0
		while ligne < 6 :
			colonne = 0
			while colonne < 6 :
				if lettres[compteur_lettre] == choix[ligne][colonne] :
					presence = True
					if nb_lettre == 0 :
						x1 = (colonne * largeur_case) + 5
						y1 = (ligne * hauteur_case) + 5
					else :
						x2 = (colonne * largeur_case) + (largeur_case - 5)
						y2 = (ligne * hauteur_case) + (hauteur_case - 5)
					nb_lettre += 1
				colonne += 1
			ligne += 1
		if presence :
			veh_xy.append((x1, y1, x2, y2))
		presence = False
		compteur_lettre += 1



#------------------------------------------------
def grille() :

	x1 = 0
	y1 = 0
	x = 0
	y = 0
	global grille_id
	grille_id = []

	while y < nb_lignes : 
		while x < nb_colonnes :
			grille = can.create_rectangle(x1, y1, x1 + largeur_case, y1 + hauteur_case, outline = "white", fill="black")
			grille_id.append(grille)
			x += 1
			x1 += largeur_case
		y += 1
		y1 += hauteur_case
		x = 0
		x1 = 0

	grille_id = set(grille_id)

#-------------------------------------------------
def vehicules() :

	global veh_id
	veh_id = []

	compteur = 0
	for veh in veh_xy :
		veh_id.append(can.create_rectangle(veh_xy[compteur][0], veh_xy[compteur][1], \
		veh_xy[compteur][2], veh_xy[compteur][3], outline = "white", fill = colors[compteur]))
		compteur += 1
	
def gauche(event) :

	global nb_coups
	if not win_toggle :
		if can.coords(vehicule_courant)[0] > 10 :
			liste = can.find_overlapping(can.coords(vehicule_courant)[0] - largeur_case, can.coords(vehicule_courant)[1], \
				can.coords(vehicule_courant)[2] - largeur_case, can.coords(vehicule_courant)[3])
			liste = set(liste) - grille_id
			if abs(can.coords(vehicule_courant)[0] - can.coords(vehicule_courant)[2]) > largeur_case :
				if vehicule_courant in liste and len(liste) <= 1 :
					can.move(vehicule_courant, -largeur_case, 0)
					nb_coups += 1
					compteur_coups.set(nb_coups)
				elif len(liste) <= 0 :
					can.move(vehicule_courant, -largeur_case, 0)
					coups += 1
					compteur_coups.set(coups)

def droite(event) :

	global nb_coups
	if not win_toggle :
		if can.coords(vehicule_courant)[2] < largeur_grille - 10 :
			liste = can.find_overlapping(can.coords(vehicule_courant)[0] + largeur_case, can.coords(vehicule_courant)[1], \
				can.coords(vehicule_courant)[2] + largeur_case, can.coords(vehicule_courant)[3])
			liste = set(liste) - grille_id
			if abs(can.coords(vehicule_courant)[0] - can.coords(vehicule_courant)[2]) > largeur_case :
				if vehicule_courant in liste and len(liste) <= 1 :
					can.move(vehicule_courant, largeur_case, 0)
					nb_coups += 1
					compteur_coups.set(nb_coups)
				elif len(liste) <= 0 :
					can.move(vehicule_courant, largeur_case, 0)
					coups += 1
					compteur_coups.set(coups)
		elif can.coords(vehicule_courant)[2] > largeur_grille - 10 and int(can.coords(vehicule_courant)[3]) == int((hauteur_case * 3) - 5) and vehicule_courant == veh_id[0]:
			you_win()

def bas(event) :

	global nb_coups
	if not win_toggle :
		if can.coords(vehicule_courant)[3] < hauteur_grille - 10 :
			liste = can.find_overlapping(can.coords(vehicule_courant)[0], can.coords(vehicule_courant)[1] + hauteur_case, \
				can.coords(vehicule_courant)[2], can.coords(vehicule_courant)[3] + hauteur_case)
			liste = set(liste) - grille_id
			if abs(can.coords(vehicule_courant)[1] - can.coords(vehicule_courant)[3]) > hauteur_case :
				if vehicule_courant in liste and len(liste) <= 1 :
					can.move(vehicule_courant, 0, hauteur_case)
					nb_coups += 1
					compteur_coups.set(nb_coups)
				elif len(liste) <= 0 :
					can.move(vehicule_courant, 0, hauteur_case)
					coups += 1
					compteur_coups.set(coups)

def haut(event) :

	global nb_coups
	if not win_toggle :
		if can.coords(vehicule_courant)[1] > 10 :
			liste = can.find_overlapping(can.coords(vehicule_courant)[0], can.coords(vehicule_courant)[1] - hauteur_case, \
				can.coords(vehicule_courant)[2], can.coords(vehicule_courant)[3] - hauteur_case)
			liste = set(liste) - grille_id
			if abs(can.coords(vehicule_courant)[1] - can.coords(vehicule_courant)[3]) > hauteur_case :
				if vehicule_courant in liste and len(liste) <= 1 :
					can.move(vehicule_courant, 0, -hauteur_case)
					nb_coups += 1
					compteur_coups.set(nb_coups)
				elif len(liste) <= 0 :
					can.move(vehicule_courant, 0, -hauteur_case)
					coups += 1
					compteur_coups.set(coups)


def lien_clavier() :

	#import pdb; pdb.set_trace()
	can.bind_all("<Left>", gauche)
	can.bind_all("<Right>", droite)
	can.bind_all("<Down>", bas)
	can.bind_all("<Up>", haut)

def clic_souris(event) :

	global vehicule_courant
	x_souris = fen.winfo_pointerx() - can.winfo_rootx()
	y_souris = fen.winfo_pointery() - can.winfo_rooty()
	selection = can.find_closest(x_souris, y_souris)
	if selection[0] in veh_id :
		vehicule_courant = selection[0]


def you_win():

	global win_toggle
	win_toggle = True
	can.create_rectangle(largeur_grille/2 - 200, hauteur_grille/2 - 50, largeur_grille/2 + 200, hauteur_grille/2 + 50, fill = "white")
	can.create_text(largeur_grille /2, hauteur_grille /2, text = "You win !!", fill = "blue", font = ("Helvetica", 50))


def reset_level(n) :

	global can, nb_coups, win_toggle
	can.destroy()

	can = Canvas(fen, width=largeur_grille, height=hauteur_grille, bg="white")
	can.grid(column = 0, row = 1, columnspan = 7, rowspan = 6)

	grille()
	choix_level(n)
	vehicules()
	win_toggle = False
	nb_coups = 0
	compteur_coups.set(nb_coups)
	level_name.set("Niveau " + str(n + 1))


fen = Tk()

can = Canvas(fen, width=largeur_grille, height=hauteur_grille, bg="white")
can.grid(column = 0, row = 1, columnspan = 7, rowspan = 6)
grille()
choix_level(0)
vehicules()
lien_clavier()
can.bind_all("<Button-1>", clic_souris)
vehicule_courant = veh_id[0]


compteur_coups = IntVar()
compteur_coups.set(nb_coups)

level_name = StringVar()
level_name.set(" Niveau " + "1")

level_title = Label(fen, textvariable = level_name, font = ("Helvetica", 16), fg = "red")
level_title.grid(column = 0, row = 0, columnspan = 2)

instructions = Label(fen, text = "Guidez la pièce verte vers la sortie", font = ("Helvetica", 12))
instructions.grid(column = 3, row = 0, columnspan = 3)

bouton = Button(fen, text = "Niveau 01", command = lambda : reset_level(0))
bouton.grid(column = 0, row = 8)
bouton = Button(fen, text = "Niveau 02", command = lambda : reset_level(1))
bouton.grid(column = 1, row = 8)
bouton = Button(fen, text = "Niveau 03", command = lambda : reset_level(2))
bouton.grid(column = 2, row = 8)
bouton = Button(fen, text = "Niveau 04", command = lambda : reset_level(3))
bouton.grid(column = 3, row = 8)
bouton = Button(fen, text = "Niveau 05", command = lambda : reset_level(4))
bouton.grid(column = 4, row = 8)
bouton = Button(fen, text = "Niveau 06", command = lambda : reset_level(5))
bouton.grid(column = 5, row = 8)
bouton = Button(fen, text = "Niveau 07", command = lambda : reset_level(6))
bouton.grid(column = 6, row = 8)

bouton = Button(fen, text = "Niveau 08", command = lambda : reset_level(7))
bouton.grid(column = 0, row = 9)
bouton = Button(fen, text = "Niveau 09", command = lambda : reset_level(8))
bouton.grid(column = 1, row = 9)
bouton = Button(fen, text = "Niveau 10", command = lambda : reset_level(9))
bouton.grid(column = 2, row = 9)
bouton = Button(fen, text = "Niveau 11", command = lambda : reset_level(10))
bouton.grid(column = 3, row = 9)
bouton = Button(fen, text = "Niveau 12", command = lambda : reset_level(11))
bouton.grid(column = 4, row = 9)
bouton = Button(fen, text = "Niveau 13", command = lambda : reset_level(12))
bouton.grid(column = 5, row = 9)
bouton = Button(fen, text = "Niveau 14", command = lambda : reset_level(13))
bouton.grid(column = 6, row = 9)

bouton = Button(fen, text = "Niveau 15", command = lambda : reset_level(14))
bouton.grid(column = 0, row = 10)
bouton = Button(fen, text = "Niveau 16", command = lambda : reset_level(15))
bouton.grid(column = 1, row = 10)
bouton = Button(fen, text = "Niveau 17", command = lambda : reset_level(16))
bouton.grid(column = 2, row = 10)
bouton = Button(fen, text = "Niveau 18", command = lambda : reset_level(17))
bouton.grid(column = 3, row = 10)
bouton = Button(fen, text = "Niveau 19", command = lambda : reset_level(18))
bouton.grid(column = 4, row = 10)
bouton = Button(fen, text = "Niveau 20", command = lambda : reset_level(19))
bouton.grid(column = 5, row = 10)
bouton = Button(fen, text = "Niveau 21", command = lambda : reset_level(20))
bouton.grid(column = 6, row = 10)

bouton = Button(fen, text = "Niveau 22", command = lambda : reset_level(21))
bouton.grid(column = 0, row = 11)
bouton = Button(fen, text = "Niveau 23", command = lambda : reset_level(22))
bouton.grid(column = 1, row = 11)
bouton = Button(fen, text = "Niveau 24", command = lambda : reset_level(23))
bouton.grid(column = 2, row = 11)
bouton = Button(fen, text = "Niveau 25", command = lambda : reset_level(24))
bouton.grid(column = 3, row = 11)
bouton = Button(fen, text = "Niveau 26", command = lambda : reset_level(25))
bouton.grid(column = 4, row = 11)
bouton = Button(fen, text = "Niveau 27", command = lambda : reset_level(26))
bouton.grid(column = 5, row = 11)
bouton = Button(fen, text = "Niveau 28", command = lambda : reset_level(27))
bouton.grid(column = 6, row = 11)

bouton = Button(fen, text = "Niveau 29", command = lambda : reset_level(28))
bouton.grid(column = 0, row = 12)
bouton = Button(fen, text = "Niveau 30", command = lambda : reset_level(29))
bouton.grid(column = 1, row = 12)
bouton = Button(fen, text = "Niveau 31", command = lambda : reset_level(30))
bouton.grid(column = 2, row = 12)
bouton = Button(fen, text = "Niveau 32", command = lambda : reset_level(31))
bouton.grid(column = 3, row = 12)
bouton = Button(fen, text = "Niveau 33", command = lambda : reset_level(32))
bouton.grid(column = 4, row = 12)
bouton = Button(fen, text = "Niveau 34", command = lambda : reset_level(33))
bouton.grid(column = 5, row = 12)
bouton = Button(fen, text = "Niveau 35", command = lambda : reset_level(34))
bouton.grid(column = 6, row = 12)

bouton = Button(fen, text = "Niveau 36", command = lambda : reset_level(35))
bouton.grid(column = 0, row = 13)
bouton = Button(fen, text = "Niveau 37", command = lambda : reset_level(36))
bouton.grid(column = 1, row = 13)
bouton = Button(fen, text = "Niveau 38", command = lambda : reset_level(37))
bouton.grid(column = 2, row = 13)
bouton = Button(fen, text = "Niveau 39", command = lambda : reset_level(38))
bouton.grid(column = 3, row = 13)
bouton = Button(fen, text = "Niveau 40", command = lambda : reset_level(39))
bouton.grid(column = 4, row = 13)


sortie = Label(fen, text = "<-- EXIT  ", font = ("Helvetica", 10, "bold"))
sortie.grid(column = 7, row = 3)

texte_coups = Label(fen, text = "Nombre de déplacements :", font = ("Helvetica", 20))
texte_coups.grid(column = 0, row = 15, columnspan = 6)

nbre_coups = Label(fen, textvariable = compteur_coups, font = ("Helvetica", 20))
nbre_coups.grid(column =6, row = 15)

fen.rowconfigure(8, pad = 7)
fen.rowconfigure(9, pad = 7)
fen.rowconfigure(10, pad = 7)
fen.rowconfigure(11, pad = 7)
fen.rowconfigure(12, pad = 7)
fen.rowconfigure(13, pad = 7)

fen.columnconfigure(3, pad = 5)
fen.columnconfigure(8, pad = 5)

bouton5 = Button(fen, text = "Quitter", command = fen.destroy)
bouton5.grid(column = 6, row = 13)

fen.mainloop()