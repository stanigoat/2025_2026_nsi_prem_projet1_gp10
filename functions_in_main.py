#Vous trouverez ici le code des différentes fonctions uniques à la fonction main
import json

quitting_words = ["quit", "stop", "bye"]

def load_database():
    with open("database.json", "r") as f:
        users_database = json.load(f)
    return users_database

def ask_user_choice():
    choice = input("Veuillez entrez votre choix : ")
    return choice

def re_ask_user_choice():
    choice = input("Veuillez choisir une option dans la liste ci-dessus : ")
    return choice

def login_user():
    global current_user
    users_database = load_database()
    user_answ = input("Veuillez rentrer votre prénom : ")
    while user_answ not in quitting_words:
        if user_answ in users_database:
            pin_check = int(input("Veuillez rentrer votre pin : "))
            if pin_check == users_database[user_answ]["PIN"]:
                print("Connexion réussie")
                current_user = user_answ
                return
            else: print("Veuillez réessayer")
        else: print("Votre nom n'est pas dans notre base de données")

def show_options():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Options")
    print("-----------------------------------------------------------")
    print("1. AFFICHER LE SOLDE")
    print("2. DEPOT")
    print("3. RETRAIT")
    print("-----------------------------------------------------------")

def show_user_balance():
    users_database = load_database()
    solde = users_database[current_user]["solde"]
    print(f"Votre solde banquaire est : {solde} €")