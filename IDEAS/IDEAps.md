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



def show_history():
    #montrer historique dépenses
    


Parfait !
Si tu veux **afficher uniquement “historique” et son contenu** pour un client, voici la manière la plus simple et directe.

---

# ✅ Code minimal pour afficher uniquement l'historique

```python
def montrer_historique(client_name, clients):
    # Vérification si le client existe
    if client_name not in clients:
        print("Client introuvable.")
        return
    
    # Récupérer l'historique uniquement
    historique = clients[client_name]["historique"]

    print("\n=== HISTORIQUE ===")
    for entry in historique:
        print(entry)
```

---

# 🎯 Résultat affiché (exemple pour Patrick)

```
=== HISTORIQUE ===
{'Action': 'Dépôt', 'Montant': 3000, 'AncienSolde': 44655, 
 'NouveauSolde': 47655, 'Date': '2025-08-10T11:13:47'}

{'Action': 'Retrait', 'Montant': 500, 'AncienSolde': 45155, 
 'NouveauSolde': 44655, 'Date': '2025-07-28T15:28:09'}

...
```

---

# 💡 Si tu veux un affichage plus propre :

```python
def montrer_historique(client_name, clients):
    if client_name not in clients:
        print("Client introuvable.")
        return
    
    historique = clients[client_name]["historique"]

    print("\n=== HISTORIQUE ===")
    for op in historique:
        print(f"{op['Date']} - {op['Action']} de {op['Montant']} € "
              f"(Solde: {op['AncienSolde']} → {op['NouveauSolde']})")
```

---

# 🎯 Résultat plus propre

```
=== HISTORIQUE ===
2025-08-10T11:13:47 - Dépôt de 3000 € (Solde: 44655 → 47655)
2025-07-28T15:28:09 - Retrait de 500 € (Solde: 45155 → 44655)
2025-06-14T10:01:22 - Retrait de 845 € (Solde: 46000 → 45155)
...
```

---

Si tu veux que je t’intègre cette fonction directement dans ton **menu**, je peux t’écrire la version complète.

    

