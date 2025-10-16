#Vous trouverez ici le code principal de notre logiciel
from functions_in_main import *

load_database()

def connection():
    show_intro()
    choice = ask_user_choice()

    while choice not in quitting_words:
        if choice == "1":
            login_user()
            exit()
        elif choice == "2":
            exit()
        else:
            choice = re_ask_user_choice()

connection()

def after_login():
    show_options()

    choice = ask_user_choice()

    if choice == "1":
        show_user_balance()
    if choice == "2":
        ask_user_depot()
    if choice == "3":
        ask_user_withdr()
    else:
        quit()

def after_action():
    ask_if_user_want_action()

    choice = ask_user_choice

    if choice == "1":
        after_login()
    elif choice == "2":
        quit()


    