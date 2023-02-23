import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "secret_key/secret_key.json", scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("blockchain")
sheet = workbook.sheet1


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


def show_welcome_menu():
    print("Please select one of the options below:")
    print("1. Sign in to your wallet")
    print("2. Create a new wallet")
    print("3. Exit the program")
    user_choice = input("Please enter 1, 2, or 3, and press enter: ")

    if (user_choice == "1"):
        print("Input your login details:")
        input_user = input("Please enter your username: ")
        input_pass = input("Please enter your password: ")
        # If user is in google sheet check column + 1 if password matches
        # elif user isn't in google sheet, give error message
    elif (user_choice == "2"):
        new_user = input("Please choose a username: ")
        new_pass = input("Please choose a password: ")
        # Find the next available username cell, and enter the user
        # plus enter the pass in the user column + 1
    elif (user_choice == "3"):
        # Do this
        SystemExit(0)
    else:
        print("Please enter one of the options")
        show_welcome_menu()


show_start_menu()
show_welcome_menu()
