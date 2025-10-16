#Vous trouverez ici le code principal de notre logiciel
from functions_bank_balance import *
from functions_in_main import *

load_database()

def connection():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Options")
    print("-----------------------------------------------------------")
    print("1. SE CONNECTER")
    print("2. QUITTER")
    print("-----------------------------------------------------------")

    choice = ask_user_choice()

    while choice not in quitting_words:
        if choice == "1":
            login_user()
        elif choice == "2":
            exit()
        else: choice = re_ask_user_choice()

connection()

def after_login():
    show_options():

    choice = ask_user_choice()

    if choice == "1":
        show_user_balance()
