# -- coding: utf-8 --
import random
#jeu pierre feuille ciseaux

print("Bienvenue dans pierre feuille ciseaux :")
nom_joueur = input ("Veuillez entrez votre nom de joueur :")
print ("Binvenue",nom_joueur)
print ( nom_joueur, "choisissez ce que voulez jouer : pierre = 1 | feuille = 2 | ciseaux = 3")
choix_joueur = input ("Entrez un numéro :")
print ("Vous avez choisi : ", choix_joueur)
choix_ordi = print ("L'ordinateur choisi à son tour : ")

for i in range(1):
    choix_ordi = random.randint (1,3)
    print ("L'ordinateur a choisi : ", str(choix_ordi))
if int(choix_joueur) == 1 and choix_ordi == 3:
    print ("FELICITATIONS," , choix_joueur , "vous avez gagné !")
elif int(choix_joueur) == 3 and choix_ordi == 1:
    print ("DOMMAGE, C'EST PERDU! L'ordinateur à gagné")
elif int(choix_joueur) == 3 and choix_ordi == 2:
    print ("DOMMAGE, C'EST PERDU! L'ordinateur à gagné")
elif int(choix_joueur) == 2 and choix_ordi == 1:
    print ("FELICITATIONS," , choix_joueur , "vous avez gagné !")
elif int(choix_joueur) == 2 and choix_ordi == 3:
    print ("DOMMAGE,C'EST PERDU! L'ordinateur à gagné")
elif int(choix_joueur) == 3 and choix_ordi == 2:
    print ("FELICITATIONS,",choix_joueur, 'vous avez gagné !')
elif int(choix_joueur) == 1 and choix_ordi == 1:
    print ("Il y a égalité !")
elif int(choix_joueur) == 2 and choix_ordi == 2:
    print ("Il y a égalité !")
elif int(choix_joueur) == 3 and choix_ordi == 3:
    print ("Il y a égalité !")


print ("Merci d'avoir joué")
