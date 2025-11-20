#Vous trouverez ici le code des différentes fonctions uniques à la fonction main
import json

quitting_words = ["quit", "stop", "bye"]
cash_options = [500, 200, 100, 50, 20, 10, 5, 2, 1]

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
            pin_check = int(input("Veuillez rentrer votre pin ( ex : 1234 ): "))

            while pin_check != users_database[user_answ]["PIN"]:
                print("Veuillez réessayer")
                pin_check = int(input("Veuillez rentrer votre PIN ( ex : 1234 ): "))

            print("Connexion réussie")
            current_user = user_answ
            return  

        else: print("Votre nom n'est pas dans notre base de données")
        user_answ = input("Veuillez rentrer votre prénom : ")

def show_options():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Options")
    print("-----------------------------------------------------------")
    print("1. AFFICHER LE SOLDE")
    print("2. DEPOT")
    print("3. RETRAIT")
    print("4. MONTRER HISTORIQUE")
    print("5. QUITTER")
    print("-----------------------------------------------------------")

def show_user_balance():
    users_database = load_database()
    solde = users_database[current_user]["Balance"]
    print(f"Votre solde banquaire est : {solde} €")

def ask_user_depot():
    amount = input("Veuillez rentrer le montant de votre dépôt : ")

    while not is_amount_valid(amount):
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


def is_amount_valid(amount):
    if not amount.strip():
        return False
    try:
        return int(amount) > 0
    except ValueError:
        return False

def re_ask_amount():
    amount = input("Veuillez rentrez un nombre positif et inférieur ou égal à votre solde comme montant de dépôt/retrait/virement : ")
    return amount

def withdr_is_possible(amount):
    users_database = load_database()
    possibility = users_database[current_user]["Balance"] - int(amount)
    return possibility >= 0

def ask_user_withdr():
    amount = input("Veuillez rentrer le montant de votre retrait : ")

    while not is_amount_valid(amount) or not withdr_is_possible(amount):
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

    print(f"Vous avez effectué un retrait de {amount} €, votre solde banquaire est donc désormais de {withdr}")

def ask_if_user_want_action():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Voulez-vous continuez à utiliser notre logiciel ?")
    print("-----------------------------------------------------------")
    print("1. CONTINUER")
    print("2. QUITTER")
    print("-----------------------------------------------------------")


def cut_in_cash(amount, cash_cut):
    count = 0
    while amount >= cash_cut:
        amount = amount - cash_cut
        count = count + 1
    return count

def cut_withdr_cash(amount):
    while amount != 0:
        for cash_cut in cash_options:
            counter = cut_in_cash(amount, cash_cut)

            if counter > 0:
                result[cash_cut] = counter

def actualize_history():
    pass

def re_ask_reciever():
    account = input("Veuillez rentrer un destinataire valide : ")
    return account

def ask_user_transfer_reciever():
    users_database = load_database()
    reciever = input("Veuillez rentrer le nom du destinataire de votre virmement")

    while reciever not in users_database or reciever == current_user:
        reciever = re_ask_reciever()

    return reciever

def transfer_to_account(amount, reciever):
    users_database = load_database()
    balance = users_database[current_user]["Balance"]
    reciever_balance = users_database[reciever]["Balance"]

    debit = balance - int(amount)
    users_database[current_user]["Balance"] = debit

    balance_reciever = users_database[reciever]["Balance"] + int(amount)
    users_database[reciever]["Balance"] = balance_reciever

    with open("database.json", "w") as f:
        json.dump(users_database, f, indent=4)

    print(f"Vous avez effectué un virement de {amount} € adresse a {reciever}, votre solde banquaire est donc désormais de {debit}")

def bank_transfer():
    amount = input("Veuillez rentrer le montant de votre virement : ")

    while not is_amount_valid(amount) or not withdr_is_possible(amount):
        amount = re_ask_amount()

    reciever = ask_user_transfer_reciever()
    transfer_to_account(amount, reciever)

def show_private_info():
    pass

def show_history():
    pass

def change_card_pin():
    pass
 