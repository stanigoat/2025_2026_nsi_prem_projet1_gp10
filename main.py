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

    if choice == "1":
        login_user()
    elif choice == "2":
        exit()
    else: re_ask_user_choice()

connection()

