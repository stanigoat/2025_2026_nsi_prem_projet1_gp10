import tkinter

compteur = 0

def onClick (event) : 
    global compteur
    compteur = compteur + 1
    monLabel.config (text = 'compteur : ' + str(compteur))

maFenetre = tkinter.Tk()

monBouton = tkinter.Button (maFenetre, text= 'Clique ici !', widht = 50)
monBouton.pack ()
monBouton.bind( '<ButtonRelease-1>', onClick)

monLabel = tkinter.Label (MaFenetre , text= 'Compteur : 0')
monLabel.pack() 

#revoir le code au dessus, possibilité que cela ne marche pas. à voir 
# possibilité donc que cela ne serve à rien