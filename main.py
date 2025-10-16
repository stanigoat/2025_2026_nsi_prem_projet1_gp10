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
<<<<<<< HEAD

def after_login():
    show_options():

    choice = ask_user_choice()

    if choice == "1":
        show_user_balance()
=======
<<<<<<< HEAD
<<<<<<< Updated upstream

def after_connection():
    show_all_actions()

    choice = ask_user_choice

    if choice == "1":
        depot_user()
    elif choice == "2":
        retrait_user()
    elif choice == "3":
        show_balance_user()
    else : re_ask_user_choice()

after_connection()

>>>>>>> 0b8d23071764146a12dcac62f3a107be81825676
