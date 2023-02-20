import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "/workspace/CI_PP3_JCoin/secret_key/secret_key.json", scopes=scopes)


def show_main_menu():
    print(" _________     _______    ________    _______    _______   __ ")
    print("|___   ___|   |  _____|  |  ____  |  |__   __|  |   _   | |  |")
    print("    | |       | |        | |    | |     | |     |  | |  | |  |")
    print("    | |       | |        | |    | |     | |     |  | |  | |  |")
    print("    | |       | |        | |    | |     | |     |  | |  | |  |")
    print(" ___| |       | |_____   | |____| |   __| |__   |  | |  |_|  |")
    print("|_____|       |_______|  |________|  |_______|  |__| |_______|")
