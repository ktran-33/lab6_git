def encode(password):
    encoded = ""
    for i in password:
        digit = int(i) + 3
        if digit >= 10:
            digit = str(digit)
            digit = digit[1]
        encoded += str(digit)
    return encoded

def decode(password):
    decoded = ""
    for i in password:
        digit = int(i) - 3
        if digit == -1:
            digit = 9
        if digit == -2:
            digit = 8
        if digit == -3:
            digit = 7
        decoded += str(digit)
    return decoded

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")

if __name__=="__main__":
    choice = 4

    while choice != 3:
        print_menu()

        choice = int(input("Please enter an option: "))

        if choice == 1:
            user_password = input("Please enter your password: ")
            print("Your password has been encoded and stored!")
            encoded = encode(user_password)

        if choice == 2:
            print(f'The encoded password is {encoded}, and the original password is {decode(encoded)}.')