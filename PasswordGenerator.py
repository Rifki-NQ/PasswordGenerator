import random
import string

def password():
    upper = ''.join(random.choice(string.ascii_uppercase))
    lower = ''.join(random.choices(string.ascii_lowercase, k=5))
    numbers = ''.join(random.choices(string.digits, k=3))

    PASS = upper + lower + numbers
    return PASS

def MenuOne():
    with open("passwords.txt", "r") as f:
        text = f.readlines()
        if not text:
            print("NO Password has been made yet")
        else:
            print(text[len(text) - 1])

def MenuTwo():
    PASS = password()
    p = False
    with open("passwords.txt", "r") as f:
        x = f.read()
        if not x:
            p = True
    with open("passwords.txt", "a") as f:
        if p:
            f.write(f"{PASS}")
        else:
            f.write(f"\n{PASS}")
        print("New Password has been created!")

def MenuThree():
    with open("passwords.txt", "r+") as f:
        x = f.readlines()
        f.seek(0)
        if len(x) == 0:
            print("There is no password to delete")
        else:
            y = f.read()
            y = y.replace(x[len(x) - 1], "")
            y = y.strip()
            f.seek(0)
            f.truncate()
            f.write(y)

#The first menu to be accessed
print("Password Generator, please use the number index to access the menu")
while True:
    print("1. Show last password made\n2. Create new password\n3. Delete last password")
    menu = input("Input: ")
    if menu.isdigit():
        menu = int(menu)
        #Menu 1: Show last password made
        if menu == 1:
            print("Menu 1")
            MenuOne()
        #Menu 2: Create new password
        elif menu == 2:
            print("Menu 2")
            MenuTwo()
        #Menu 3: Delete last password
        elif menu == 3:
            print("Menu 3")
            MenuThree()
        elif menu == 10:
            break
        else:
            print("Error: Please input the correct index (1, 2, 3)")
    else:
        print("Error: Please use the number index to access the menu")