"""from noeud import Noeud

# 1. Création des "feuilles" (tout en bas de l'arbre)
Noeud_2=Noeud(2)
Noeud_y=Noeud('y')

# 2. Création des noeuds
noeud_add=Noeud('+') # Création du noeud d'addition
noeud_add.ajouter_Noeud(Noeud_2)
noeud_add.ajouter_Noeud(Noeud_y)

# 3.Création de l'opérateur unaire exp
racine=Noeud('exp') # Création du noeud de la racine 
racine.ajouter_Noeud(noeud_add)

# 4. Vérification de l'affichage
affichage=racine.affichage_polonais()

print("Affichage polonais attendu : exp + 2 y")
print(f"Affichage polonais obtenu  : {affichage}")"""



from noeud import Noeud

# Création des feuilles : la valeur 2 et la variable y
noeud_2 = Noeud(2)
noeud_y = Noeud('y')

# Création de l'opérateur d'addition et ajout des enfants
noeud_add = Noeud('+')
noeud_add.ajouter_enfant(noeud_2)
noeud_add.ajouter_enfant(noeud_y)

# Création de la racine (opérateur unaire exp)
racine = Noeud('exp')
racine.ajouter_enfant(noeud_add)

# Vérification de la notation polonaise
affichage = racine.afficher_polonais()
print(f"Affichage polonais : {affichage}") 
# Doit afficher : exp + 2 y








