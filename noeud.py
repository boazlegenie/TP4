"""class Noeud:
    #Question 1:
    def __init__(self,valeur):
        self.valeur=valeur #Valeur de Noeud.
        self.liste=[]      #Liste des Noeuds.
     #Question 2:   
    def ajouter_Noeud(self,noeud):
        self.liste.append(noeud) #Ajout d'un noeud dans la liste.
    #Question 3:
    def affichage_polonais(self):
        resultat=str(self.valeur)
        for el in self.liste:
            resultat="" + el.affichage_polonais()
        return resultat
    #Question 4: Dans le main.py"""
    
class Noeud:
    """
    Classe représentant un noeud dans un arbre d'expression mathématique.
    """
    def __init__(self, valeur):

        """
        Initialise un noeud avec une valeur donnée.
        Args:
            valeur: La valeur du noeud, qui peut être une chaîne de caractères,
            un entier ou un nombre flottant.
        """
        # La valeur peut être de type str (variable/opération) ou int/float (constante)
        self.valeur = valeur
        # La liste des noeuds enfants est une liste d'objets de type Noeud
        self.enfants = []

    def ajouter_enfant(self, noeud_enfant):
        """Ajoute un noeud à la liste des noeuds enfants."""
        self.enfants.append(noeud_enfant)

    def afficher_polonais(self):
        """Affiche l'expression mathématique en utilisant l'affichage polonais."""
        resultat = str(self.valeur)
        for enfant in self.enfants:
            resultat += " " + enfant.afficher_polonais()
        return resultat
    

    

        
    
    
