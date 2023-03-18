import gsheets
import run


def send_coins(sending_user, receiving_user, amount):
    """
    A function for sending coins to another user. It takes
    the sending amount off of the senders balance, and adds
    it to the receivers balance.
    """
    # sending_user wallet balance - amount
    sender_balance = int(gsheets.sheet.cell(sending_user, 3).value)
    receiver_balance = int(gsheets.sheet.cell(receiving_user, 3).value)

    try:
        if (sender_balance - amount < 0):
            # Exit the function and output error not enough balance
            raise ValueError('\nBalance is lower than amount to send\
                \nPlease send a smaller amount\n')
        else:
            gsheets.sheet.update_cell(
                sending_user, 3, sender_balance - amount)
            gsheets.sheet.update_cell(
                receiving_user, 3, receiver_balance + amount)
            print("\nCoins have been sent successfully")
    except ValueError as e:
        print(e)
        return
    # creates a new block


def check_balance(row_ID):
    """
    A function to check the users wallet balance.
    it takes in the row of the users details pulls
    their data from the google sheet.
    """
    wallet_user = gsheets.sheet.cell(row_ID, 1).value
    wallet_balance = gsheets.sheet.cell(row_ID, 3).value
    print("\nWelcome", wallet_user, "Your balance is:", wallet_balance)


def delete_wallet(row_ID):
    """
    A function that deletes the users wallet by
    taking the user's row_ID and deletes the
    values in their wallet, password, and
    amount cells.
    """
    gsheets.sheet.update_cell(row_ID, 1, "")
    gsheets.sheet.update_cell(row_ID, 2, "")
    gsheets.sheet.update_cell(row_ID, 3, "")


def mine_block():
    last_block = run.actual_blockchain[-1]
    block = {
        'previous_block_index': last_block[index],
        'index': len(run.actual_blockchain),
        'transactions': run.open_transactions
    }
    run.actual_blockchain.append(block)
