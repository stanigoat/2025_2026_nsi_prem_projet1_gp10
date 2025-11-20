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



"Historique" : [
            {
                "Action": "Dépôt",
                "Montant": 3000,
                "AncienSolde": 44655,
                "NouveauSolde": 47655,
                "Date": "2025-08-10T11:13:47"
            },
            {
                "Action": "Retrait",
                "Montant": 500,
                "AncienSolde": 45155,
                "NouveauSolde": 44655,
                "Date": "2025-07-28T15:28:09"
            },
            {
                "Action": "Retrait",
                "Montant": 845,
                "AncienSolde": 46000,
                "NouveauSolde": 45155,
                "Date": "2025-06-14T10:01:22"
            },
            {
                "Action": "Dépôt",
                "Montant": 1500,
                "AncienSolde": 44500,
                "NouveauSolde": 46000,
                "Date": "2025-05-05T19:14:58"
            }
        ]

"Historique" : [
            {
                "Action": "Retrait",
                "Montant": 500,
                "AncienSolde": 50500,
                "NouveauSolde": 50000,
                "Date": "2025-07-19T14:45:02"
            },
            {
                "Action": "Retrait",
                "Montant": 250,
                "AncienSolde": 50750,
                "NouveauSolde": 50500,
                "Date": "2025-06-03T12:18:44"
            },
            {
                "Action": "Dépôt",
                "Montant": 1000,
                "AncienSolde": 49750,
                "NouveauSolde": 50750,
                "Date": "2025-05-17T09:21:10"
            },
            {
                "Action": "Retrait",
                "Montant": 750,
                "AncienSolde": 50500,
                "NouveauSolde": 49750,
                "Date": "2025-04-29T17:52:30"
            }
        ]


"Historique" : [
            {
                "Action": "Retrait",
                "Montant": 200,
                "AncienSolde": 354764,
                "NouveauSolde": 354564,
                "Date": "2025-05-12T10:34:55"
            },
            {
                "Action": "Dépôt",
                "Montant": 1200,
                "AncienSolde": 353564,
                "NouveauSolde": 354764,
                "Date": "2025-04-22T16:12:01"
            },
            {
                "Action": "Retrait",
                "Montant": 1000,
                "AncienSolde": 354564,
                "NouveauSolde": 353564,
                "Date": "2025-04-10T08:11:29"
            }
        ]