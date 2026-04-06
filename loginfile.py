username = input("non d'utilisateur : ")
password = input("mot de passe : ")

if username == "admin" and password == "1234":
    print("accès autorisé")
else:
    print("accès refusé")