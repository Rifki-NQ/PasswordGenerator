import random
import string

def password():
    upper = ''.join(random.choice(string.ascii_uppercase))
    lower = ''.join(random.choices(string.ascii_lowercase, k=5))
    numbers = ''.join(random.choices(string.digits, k=3))

    PASS = upper + lower + numbers
    return PASS

def MenuTwo():
    PASS = password()

#The first menu to be accessed
while True:
    print("Password Generator, please use the number index to access the menu")
    print("1. Show last password made\n2. Create new password\n3. Delete last number")
    menu = input("Input: ")
    if menu.isdigit():
        menu = int(menu)
        if menu > 0 and menu < 4:
            break
        else:
            print("Error: Please input the correct index (1, 2, 3)")
    else:
        print("Error: Plaese use the number index to access the menu")