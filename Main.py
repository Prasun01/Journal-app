import Journalnew
import json

login = {
        "user": "prasun",
        "password": "123abcd"
         }
with open("login.json", "w")as file:
            json.dump(login,file)

attempt = 3

while True:
    print("1. Login")
    print("2. Register")
    print("3. logout")
    menu = input("Choice: ")

    if menu == "1":
        print("Enter your loign details below")

        username = input("Enter your USERNAME: ")
        password = input("Enter your Password: ")

        if username == login["user"] and password == login["password"] :
            print("login successfull!")
            Journalnew.start()

        else:
            print("wrong username or password.")
            attempt = attempt - 1
            if attempt == 0:
                 print("Account locked")
                 break

    elif menu == "2":
        with open("login.json", "r")as file:
            login= json.load(file)

        print("Enter details")

        username = input("Enter your USERNAME: ")
        password = input("Enter your Password: ")

        login["user"] = username 
        login["password"] = password

        with open("login.json", "w") as file:
            json.dump(login , file)

        print("Account created. login now!")

    elif menu == "3":
        break