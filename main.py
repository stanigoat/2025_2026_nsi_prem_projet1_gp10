#Vous trouverez ici le code principal de notre logiciel

def connection():
    print("******************** LOGICIEL BANQUAIRE ********************")
    print("Options")
    print("-----------------------------------------------------------")
    print("1. SE CONNECTER")
    print("2. QUITTER")

    ask_user_choice()

    if answer == "1":
        register_user()
    elif answer == "2":
        sys.exit
    else: re_ask_user_choice()