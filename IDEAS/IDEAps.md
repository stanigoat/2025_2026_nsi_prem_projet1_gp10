# faire apparaitre un message d'accueil 'bonjour, veuillez entrer votre PIN' #

# base44 #

# touche on/off pour mettre en route le DAB #

# pour creeer interfzce graphique --> utiliser 'TkInter' -----> avec import tkinter
# EX : MaFenetre = tkinter.Tk() #
# EX : MonLabel = tkinter.Label (MaFenetre , texte= " ma premiere fenetre ! ")
# pour l'ajouter dans la fenetre, faire : MonLabel.pack() 
# https://www.youtube.com/watch?v=xnRP3VN6jjo&t=137s #

l'utilisation de tkinter ne sert peut etre à rien ou ne marche tout simplement pas. 

def choisir_langue () : 
    print ("******************** CHOISIR LANGUE ********************")
    print ("1.FRANCAIS")
    print ("2.ANGLAIS ")
    print ("3.ESPAGNOL")
    print ("4.ITALIEN")
    print ("5.PORTUGAIS")
    print ("6.ALLEMAND")

    choice = input("******************** ENTREZ VOTRE CHOIX ********************")

def ask_language () :
    choisir_langue () 
    choice = ask_user_choice () 

    while choice not in quitting_words:
        if choice == "1" :
            langue = " français "
        elif choice == "2" : 
            langue = " anglais "
        elif choice == "3" : 
            langue = " espagnol "
        elif choice == "4" : 
            langue = 'italien' 
        elif choice == "5" : 
            langue = " portugais "
        elif choice == "6" : 
            langue = " allemand "
        else :
            choice = re_ask_user_choice ()

    print ("******************** LANGUE CHOSIE : {langue}")
    return langue 

