def encode(password): # Function that changes password into a super secret one
    encoded = ""
    for i in password:
        digit = int(i) + 3
        if digit >= 10: # If the number is two-digit, just take the ones place
            digit = str(digit)
            digit = digit[1]
        encoded += str(digit)
    return encoded

def decode(password):
    # Variables
    password_digits = [*password] # Creates a list with the digits in the password
    # A dictionary with the password digits and their corresponding encoded values
    decoded_digits = {
        "3": "0",
        "4": "1",
        "5": "2",
        "6": "3",
        "7": "4",
        "8": "5",
        "9": "6",
        "0": "7",
        "1": "8",
        "2": "9"
    }
    decoded_password = "" # Creates an empty string to store the password

    for digit in password_digits: # Goes through every digit in the list containing the password digits
        # If the digit is in the dictionary it is encoded and added to the empty string
        if digit in decoded_digits:
            decoded_password += decoded_digits[digit]

    return decoded_password

def print_menu(): # Print Menu
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")

if __name__=="__main__":
    choice = 4 # Just so the loop works

    while choice != 3: # This is the exit option
        print_menu()

        choice = int(input("Please enter an option: "))

        if choice == 1:
            user_password = input("Please enter your password: ")
            print("Your password has been encoded and stored!")
            encoded = encode(user_password)

        if choice == 2:
            print(f'The encoded password is {encoded}, and the original password is {decode(encoded)}.')