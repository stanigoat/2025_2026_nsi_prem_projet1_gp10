#Vous trouverez ici le code principal de notre logiciel
from functions_in_main import *

load_database()



def connection():
    show_intro()
    choice = ask_user_choice()

    while choice not in quitting_words:
        if choice == "1":
            login_user()
            return
        elif choice == "2":
            exit()
        else:
            choice = re_ask_user_choice()

def after_login():
    show_options()

    choice = ask_user_choice()

    if choice == "1":
        show_user_balance()
        return
    elif choice == "2":
        ask_user_depot()
        return
    elif choice == "3":
        ask_user_withdr()
        return
    elif choice == "4":
        bank_transfer()
        return
    elif choice == "5":
        show_history()
        return
    elif choice == "6":
        log_out()
        return
    elif choice == "7":
        quit()
    else:
        choice = re_ask_user_choice()

def after_action():
    ask_if_user_want_action()

    choice = ask_user_choice()

    if choice == "1":
        after_login()
        return True
    elif choice == "2":
        quit()

connection()
after_login()
while True:
    after_action()


        
    


