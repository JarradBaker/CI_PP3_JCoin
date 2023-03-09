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


def next_empty_row():
    for i in range(1, 1000):
        if not sheet.cell(i, 1).value:
            return i
