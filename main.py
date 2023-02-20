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


show_start_menu()
