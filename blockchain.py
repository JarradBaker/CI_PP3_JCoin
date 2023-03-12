import gsheets


def send_coins(sending_user, receiving_user, amount):
    # sending_user wallet balance - amount
    sender_balance = int(gsheets.sheet.cell(sending_user, 3).value)
    receiver_balance = int(gsheets.sheet.cell(receiving_user, 3).value)

    if (sender_balance - amount < 0):
        # Exit the function and output error not enough balance
        print("\nBalance is lower than amount to send ")
        print("\nPlease send a smaller amount")
        return
    else:
        gsheets.sheet.update_cell(sending_user, 3, sender_balance - amount)
        gsheets.sheet.update_cell(receiving_user, 3, receiver_balance + amount)
        print("\nCoins have been sent successfully")
    # creates a new block


def check_balance(row_ID):
    wallet_user = gsheets.sheet.cell(row_ID, 1).value
    wallet_balance = gsheets.sheet.cell(row_ID, 3).value
    print("\nWelcome", wallet_user, "Your balance is:", wallet_balance)
