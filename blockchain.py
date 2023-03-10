import gsheets


def send_coins(sending_user, receiving_user, amount):
    # sending_user wallet balance - amount
    sending_user.value -= amount
    # receiving_user wallet balance + amount
    receiving_user.value += amount
    # creates a new block


def check_balance(row_ID):
    wallet_user = gsheets.sheet.cell(row_ID, 1).value
    wallet_balance = gsheets.sheet.cell(row_ID, 3).value
    print("\nWelcome", wallet_user, "Your balance is:", wallet_balance)
