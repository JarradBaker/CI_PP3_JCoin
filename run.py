import gsheets as gsheets
import blockchain

row_ID = 0
incorrect_attempts = 0


def show_start_menu():
    """
    A function to show the start menu. This
    shows the logo for the coin and then opens
    the welcome menu.
    """
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
    """
    A function to show the welcome menu. This
    takes input from the user allowing them to
    select which operations to perform.
    """
    print("Please select one of the options below:\n")
    print("1. Sign in to your wallet")
    print("2. Create a new wallet")
    print("3. Exit the program")
    user_choice = input("\nPlease enter 1, 2, or 3, and press enter: \n")

    try:
        if (user_choice == "1"):
            print("\nInput your login details: \n")
            input_user = input("Please enter your username: \n")
            input_pass = input("Please enter your password: \n")
            if (gsheets.sheet.find(input_user)):
                # gets the row number of the found username
                # for checking the corresponding password
                row_ID = gsheets.sheet.find(input_user, in_column=1).row
                # finds the corresponding password
                found_pass = gsheets.sheet.cell(row_ID, 2).value
                print("\nFound wallet, checking password")
                if (input_pass == found_pass):
                    print("\nPassword Matches, logging in")
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
                print("\nUser doesn't exist, please create a wallet")

            # If user is in google sheet check column + 1 if password matches
            # elif user isn't in google sheet, give error message
        elif (user_choice == "2"):
            new_user = input("Please choose a username: \n")
            new_pass = input("Please choose a password: \n")
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
            if not user_choice:
                raise ValueError('\nNothing was entered\n')
            else:
                raise ValueError('\nInput didn\'t match a choice\n')
    except ValueError as e:
        print(e)
        show_welcome_menu(incorrect_attempts)


def show_wallet_menu(row_ID):
    """
    A function to show the wallet menu. This
    takes input from the user allowing them to
    select which wallet operations to perform.
    """
    blockchain.check_balance(row_ID)
    print("\nWhat would you like to do?\n")
    print("1. Check your balance")
    print("2. Send coins to another user")
    print("3. Mine a block")
    print("4. Delete your wallet")
    print("5. Exit the program")
    user_choice = input("\nPlease enter 1, 2, 3, 4, or 5 and press enter: \n")

    try:
        if (user_choice == "1"):
            blockchain.check_balance(row_ID)
            show_wallet_menu(row_ID)
        elif (user_choice == "2"):
            sender_row_ID = row_ID
            receiver_wallet = input("\nPlease choose a user to send to: \n")
            amount_to_send = int(
                input("\nPlease choose an amount of coins:\n"))
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
                transaction = {
                    'sender': gsheets.sheet.acell('A'+str(row_ID)).value,
                    'receiver': receiver_wallet,
                    'amount': amount_to_send
                }
                blockchain.open_transactions.append(transaction)
                show_wallet_menu(row_ID)
            else:
                print("\nCannot find reciever wallet")
                show_wallet_menu(row_ID)
        elif (user_choice == "3"):
            print("\nBelow are the open transactions")
            print(blockchain.open_transactions)
            print("\nBelow is the blockchain")
            print(blockchain.actual_blockchain)
            blockchain.mine_block()
            show_wallet_menu(row_ID)
        elif (user_choice == "4"):
            confirm_choice = input("\nAre you sure? Type y or n: \n").lower()
            try:
                if (confirm_choice == "y"):
                    blockchain.delete_wallet(row_ID)
                    print("\nWallet deleted, returning to start menu\n")
                    show_welcome_menu(0)
                elif (confirm_choice == "n"):
                    print("\nWallet not deleted, returning to start menu\n")
                    show_welcome_menu(0)
                else:
                    if not user_choice:
                        raise ValueError('\nNothing was entered\n')
                    else:
                        raise ValueError('\nInput didn\'t match a choice\n')
            except ValueError as e:
                print(e)
                show_wallet_menu(row_ID)
        elif (user_choice == "5"):
            SystemExit(0)
        else:
            if not user_choice:
                raise ValueError('\nNothing was entered\n')
            else:
                raise ValueError('\nInput didn\'t match a choice\n')
    except ValueError as e:
        print(e)
        show_wallet_menu(row_ID)


show_start_menu()
