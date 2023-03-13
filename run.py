import gsheets as gsheets
import blockchain

row_ID = 0
incorrect_attempts = 0

# READING FROM THE SPREADSHEET

# Searching for a value in a cell in the specified column
# and return the row number
# cell = sheet.find("jarrad", in_column=1).row
# print(cell)

# ITERATE THROUGH GIVEN CELLS
# for cell in sheet.range('A2:A6'):
#     print(cell.value)

# PRINT A GIVEN CELL
# print(sheet.acell('A3').value)

# PRINT A WHOLE GIVEN COLUMN
# print(sheet.col_values(1))

# PRINT A WHOLE GIVEN ROW
# print(sheet.row_values(2))


# WRITING TO THE SPREADSHEET

# UPDATE A GIVEN CELL BY CALL VALUE
# sheet.update_acell('A2', 'Connor')

# UPDATE A GIVEN CELL BY CELL COORDINATES (row, col, value)
# sheet.update_cell(3, 2, 10)

# UPDATE A RANGE OF CELLS
# sheet.update('A2:C2', [['alex', 'alex123', 10000]])


def show_start_menu():
    print(" _________     _______    ________    _______    _______   __ ")
    print("|___   ___|   |  _____|  |  ____  |  |__   __|  |   _   | |  |")
    print("    | |       | |        | |    | |     | |     |  | |  | |  |")
    print("    | |       | |        | |    | |     | |     |  | |  | |  |")
    print("    | |       | |        | |    | |     | |     |  | |  | |  |")
    print(" ___| |       | |_____   | |____| |   __| |__   |  | |  |_|  |")
    print("|_____|       |_______|  |________|  |_______|  |__| |_______|")
    print("                                                              ")

    show_welcome_menu(0)


def show_welcome_menu(incorrect_attempts):
    print("Please select one of the options below:")
    print("1. Sign in to your wallet")
    print("2. Create a new wallet")
    print("3. Exit the program")
    user_choice = input("Please enter 1, 2, or 3, and press enter: ")

    if (user_choice == "1"):
        print("Input your login details:")
        input_user = input("Please enter your username: ")
        input_pass = input("Please enter your password: ")
        if (gsheets.sheet.find(input_user)):
            # gets the row number of the found username
            # for checking the corresponding password
            row_ID = gsheets.sheet.find(input_user, in_column=1).row
            # finds the corresponding password
            found_pass = gsheets.sheet.cell(row_ID, 2).value
            print("Found wallet, checking password")
            if (input_pass == found_pass):
                print("Password Matches, logging in")
                show_wallet_menu(row_ID)
            else:
                if (incorrect_attempts >= 2):
                    print("\n Too many incorrect guesses, exiting \n")
                    SystemExit(0)
                else:
                    print("\n Incorrect password, try again \n")
                    incorrect_attempts += 1
                    show_welcome_menu(incorrect_attempts)
        else:
            print("User doesn't exist, please create a wallet")

        # If user is in google sheet check column + 1 if password matches
        # elif user isn't in google sheet, give error message
    elif (user_choice == "2"):
        new_user = input("Please choose a username: ")
        new_pass = input("Please choose a password: ")
        if gsheets.sheet.find(new_user):
            print("\nUser already exists. Please log in")
            show_welcome_menu(incorrect_attempts)
        else:
            next_empty_cell = gsheets.next_empty_row_wallets()
            gsheets.sheet.update_cell(next_empty_cell, 1, new_user)
            gsheets.sheet.update_cell(next_empty_cell, 2, new_pass)
            gsheets.sheet.update_cell(next_empty_cell, 3, 10000)
            show_wallet_menu(next_empty_cell)
        # Find the next available username cell, and enter the user
        # plus enter the pass in the user column + 1
    elif (user_choice == "3"):
        # Do this
        SystemExit(0)
    else:
        print("Please enter one of the options")
        show_welcome_menu(incorrect_attempts)


def show_wallet_menu(row_ID):
    blockchain.check_balance(row_ID)
    print("\nWhat would you like to do?")
    print("\n1. Check your balance")
    print("\n2. Send coins to another user")
    print("\n3. Mine a block")
    print("\n4. Delete your wallet")
    print("\n5. Exit the program")
    user_choice = input("\nPlease enter 1, 2, 3, 4, or 5 and press enter: ")

    if (user_choice == "1"):
        blockchain.check_balance(row_ID)
        show_wallet_menu(row_ID)
    elif (user_choice == "2"):
        sender_row_ID = row_ID
        receiver_wallet = input("Please choose a user to send coins to: ")
        amount_to_send = int(input("Please choose an amount of coins: "))
        # Check if receiver_wallet is null
        if (gsheets.sheet.find(receiver_wallet)):
            receiver_row_ID = gsheets.sheet.find(
                receiver_wallet, in_column=1).row
            blockchain.send_coins(
                sender_row_ID, receiver_row_ID, amount_to_send)
            next_empty_cell = gsheets.next_empty_row_transactions()
            # Updating the transactions sheet
            sender_wallet = gsheets.sheet.acell('A'+str(row_ID)).value
            gsheets.transactions.update_cell(
                next_empty_cell, 1, sender_wallet)
            gsheets.transactions.update_cell(
                next_empty_cell, 2, receiver_wallet)
            gsheets.transactions.update_cell(
                next_empty_cell, 3, amount_to_send)
            show_wallet_menu(row_ID)
        else:
            print("\nCannot find reciever wallet")
            show_wallet_menu(row_ID)
    # elif (user_choice == 3):
        # Do this
    # elif (user_choice == 4):
        # Do this
    elif (user_choice == "5"):
        SystemExit(0)
    else:
        print("\nPlease enter one of the options")
        show_wallet_menu(row_ID)


show_start_menu()
