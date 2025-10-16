#Vous trouverez ici le code des différentes fonctions uniques à la fonction main
import json

quitting_words = ["quit", "stop", "bye"]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def load_database():
    with open("database.json", "r") as f:
        users_database = json.load(f)
    return users_database

def show_intro():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Options")
    print("-----------------------------------------------------------")
    print("1. SE CONNECTER")
    print("2. QUITTER")
    print("-----------------------------------------------------------")


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

def ask_user_depot():
    amount = input("Veuillez rentrer le montant de votre dépôt : ")
    while not_a_number(amount):
        amount = re_ask_amount()

    depot_to_balance(amount)
    return amount

def depot_to_balance(amount):
    users_database = load_database()
    balance = users_database[current_user]["Balance"]

    depot = balance + int(amount)
    users_database[current_user]["Balance"] = depot

    with open("database.json", "w") as f:
        json.dump(users_database, f, indent=4)

    print(f"Vous avez effectué un dépôt de {amount} €, votre solde banquaire est donc désormais de {depot}€")

def not_a_number(number):
    for character in number:
        if character not in numbers_list:
            return False
        else:
            return True

def re_ask_amount():
    amount = input("Veuillez rentrez un nombre comme montant de dépôt/retrait")

def ask_user_withdr():
    amount = input("Veuillez rentrer le montant de votre dépôt/retrait : ")
    while not_a_number(amount):
        amount = re_ask_amount()

    withdr_to_balance(amount)
    return amount

def withdr_to_balance(amount):
    users_database = load_database()
    balance = users_database[current_user]["Balance"]

    withdr = balance - int(amount)
    users_database[current_user]["Balance"] = withdr

    with open("database.json", "w") as f:
        json.dump(users_database, f, indent=4)

    print(f"Vous avez effectué un dépôt de {amount} €, votre solde banquaire est donc désormais de {withdr}")

def ask_if_user_want_action():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Voulez-vous continuez à utiliser notre logiciel ?")
    print("-----------------------------------------------------------")
    print("1. CONTINUER")
    print("2. QUITTER")
    print("-----------------------------------------------------------")
