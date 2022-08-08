import os
import os.path
from itertools import islice

# vars

path        = os.path.expanduser('~') + "\pythonLogin\login.txt"
folderPath   = os.path.expanduser('~') + "\pythonLogin"

b        = "\n"

defID   = "admin"
defKey     = "admin"

# Classes

class data:
    money = 200

# Funcs

def _ready():
    pass


def saveLogin(id, key):

    # save ID
    file = open(path, 'w')
    file.writelines(id + "\n" + key)
    file.close()


def loadID():
    
    file = open(path, 'r')
    lines = file.readlines()
    ide = lines[0].rstrip()
    return ide
    file.close()


def loadKey():
    
    file = open(path, 'r')
    lines = file.readlines()
    keye = lines[1]
    return keye
    file.close()


def register():
    global id
    global key

    note = "(No Spaces between characters allowed)"
    
    print("Please enter\nyour Username: " + note)
    id = defID = input()

    print("Please enter\na Password: " + note)
    key = defkey = input()

    saveLogin(id, key)
    print("Registration Succesful.")
    benningin()


def login():
    
    rid = loadID()
    rkey = loadKey()

    print("Please enter your Username:")
    idTry = input()

    print("Now enter your Password:")
    keyTry = input()

    if idTry != rid or keyTry != rkey:
        print("Incorrect Password or ID")
        benningin()

    elif idTry == rid and keyTry == rkey:
        print("Login has been a Success!")
        suc()


def read():
    file = open(path, "r")

    lines = file.readlines()
    anso = input()
    if anso == "user":
        print("Your Username is: " + lines[0].rstrip())
        read()
    elif anso == "pass":
        print("Your Password is: " + lines[1])
        read()
    elif anso == "go":
        benningin()
  
    file.close()


def checkfile():
    if os.path.exists(folderPath) == False:
        os.makedirs(folderPath)


def help():
    m = "\n"
    print("Here are the commands:")
    print(
        " - /help : Display commands."+m+
        " - /bank : Display your money left in your bank account."+m+
        " - /logout : Will log you out (of your account)."+m+"And will redirect you to the login/register page."+m+
        " - More commands soon... - "
    )
    command()


def command():
    ans = input()

    if ans == "/help":
        help()
    elif ans == "/bank":
        print("You have: "+ str(data.money))
        command()
    elif ans == "/logout":
        benningin()
    


def benningin():
    
    checkfile()

    print("Type '/login' to login.\nType '/register' to register:")
    ans = input().lower()
    if ans == "/register":
        register()
    elif ans == "/login":
        login()
    elif ans == "/read":
        read()
    elif ans == "/quit":
        quit()
    else:
        print(" - Unknown command - ")
        benningin()


def suc():

    file = open(path, 'r')
    lines = file.readlines()
    id = lines[0].rstrip()
    key = lines[1].rstrip()
    file.close()

    print("You're logged in as:", id + ".")
    print("Please type a command (or type '/help')")
    command()

# Start Here
if __name__ == "__main__":
    benningin()
