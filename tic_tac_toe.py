import random
from typing import List
CaseT = str
# les elements de CaseT sont soit " " soit "O" soit "X"
PlateauT = List[List[CaseT]]
# les elements de PlateauT sont des matrices 3x3

def plateau_vide()->PlateauT:
    """Prend rien en entree et envoie un plateau de jeu vide pour tic tac toe."""
    return [[" " for i in range (3)] for j in range (3)]
#for j in range(3): Elle s’exécute 3 fois et crée 3 lignes. À chaque tour, elle génère une nouvelle liste qui représentera une ligne du plateau.
#'' for i n range(3) :Pour chaque ligne, cette boucle crée 3 éléments, chacun étant le caractère " " (un espace). Ce sont les 3 cases vides de la ligne. 

def videt (p:PlateauT, i:int, j:int)-> bool:
    """Pre: 3>i>=0 and 3>j>=0
    verifie si la case de coordonnees (i, j) du plateau est vide.."""
    return p[i][j]== ' '

def joue(p:PlateauT, s:str ,i:int, j:int)-> None:
    """ ***Procédure***
    Hypothese: (0<=i<=2) and (0<=j<=2) and (s=='X' or s=='O')
    inscrit le symbole X dans la case de coordonnees (i, j)."""
    if videt(p , i, j):
        p[i][j]= s

def dessine_plateaut0(p:PlateauT)->str:
    """renvoie une chaine de caractere correspondant a un affichage du plateau."""
    i:int=0
    j:int
    s:str=''
    while i<3:
        for j in range(3): 
            s=s+ p[i][j]
        s=s+'\n'
        i=i+1
    return s
pla1: PlateauT= plateau_vide()
joue(pla1, 'X', 0, 2)
joue(pla1, 'O', 1, 1)
#print(dessine_plateaut0(pla1))

def dessine_plateaut(p:PlateauT)->str:
    """renvoie une chaine de caractere correspondant a un affichage du plateau avec les bords."""
    i:int=0
    j:int
    s:str=''
    while i<3:
        s=s+ '|'
        for j in range(3): 
            s=s+ p[i][j]
        s=s+ '|' +'\n'
        i=i+1
    return '/---\\\n' + s + '\\---/'
#print(dessine_plateaut(pla1))

def gagnet(p:PlateauT, s:str)->bool:
    """Pre: s=='O' or s=='X'
    verifie si s a gagne ce jeu de tic tac toe"""
    i:int=0
    while i<3:
        if p[i]==[s,s,s]:
            return True
        i=i+1
    j:int=0
    while j<3:
        if p[0][j]==s and p[1][j]==s and p[2][j]==s :
            return True
        j=j+1
    if p[0][0]==s and p[1][1]==s and p[2][2]==s:
        return True
    if p[0][2]==s and p[1][1]==s and p[2][0]==s:
        return True
    return False

def pleint(p:PlateauT)->bool:
    """Verifie si notre plateau est plein"""
    i:int
    j:int
    for i in range(3):
        for j in range(3):
            if p[i][j]==' ':
                return False
    return True

#On a acces a la primitive random.random()−>float qui renvoie un nombre flottant aleatoire compris entre 0.0 (inclus) et 1.0 (exclus). Ici on le multiplie par 3 pour avoir un nombre entre 0 et 3 (exclus).
def Jouer()->None:
    """***Procédure***
    Vous permet de choisir votre symbol et ou jouer, après c*est à l'ordinateur de jouer jusqu'à avoir un gagnant ou qu'il y ait plus de place"""
    p: PlateauT= plateau_vide()
    symbol=input("Choisissez entre 'X' et 'O': ")
    while symbol!='X' and symbol!='O':
        symbol=input("Choisissez imperativement entre 'X' et 'O': ")
    if symbol=='X':
        ordi:str= 'O'
    elif symbol=='O':
        ordi:str= 'X'
    while not pleint(p):
        i=int(input("Choisissez l'indice de la ligne où vous souhaitez jouer (entre 0 et 2) :"))
        while i<0 or i>2:
            i=int(input("Choisissez l'indice de la ligne où vous souhaitez jouer imperativement entre 0 et 2 :"))
        j=int(input("Choisissez l'indice du columne où vous souhaitez jouer (entre 0 et 2) :"))
        while j<0 or j>2:
            i=int(input("Choisissez l'indice du columne où vous souhaitez jouer imperativement entre 0 et 2 :"))
        while not videt(p,i,j):
            print("Le coup n'est pas legal! Choisissez un autre:")
            i=int(input("Choisissez l'indice de la ligne où vous souhaitez jouer (entre 0 et 2) :"))
            while i<0 or i>2:
                i=int(input("Choisissez l'indice de la ligne où vous souhaitez jouer imperativement entre 0 et 2 :"))
            j=int(input("Choisissez l'indice du columne où vous souhaitez jouer (entre 0 et 2) :"))
            while j<0 or j>2:
                i=int(input("Choisissez l'indice du columne où vous souhaitez jouer imperativement entre 0 et 2 :"))
        joue(p, symbol, i, j)
        if gagnet(p, symbol):
            print(dessine_plateaut(p))
            print('VOUZ GAGNEZ!')
            return
        elif pleint(p):
            print(dessine_plateaut(p))
            print('EGAL!')
        else:
            i1:int=int(3*random.random())
            j1:int=int(3*random.random())
            while not videt(p,i1,j1):
                i1:int=int(3*random.random())
                j1:int=int(3*random.random())
            joue(p,ordi,i1,j1)
            print(dessine_plateaut(p))
            print("l'ordinateur a joue en (" + str(i1) + ", " + str(j1) + ")")
            if gagnet(p, ordi):
                print("L'ORDINATEUR GAGNE!")
                return
            elif pleint(p):
                print('EGAL!')
#Jouer()