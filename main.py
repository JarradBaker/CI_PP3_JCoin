import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("/workspace/CI_PP3_JCoin/secret_key/secret_key.json", scopes=scopes)


def show_main_menu():
    print("  _________      ______    ________    _______    ___      _  ")
    print(" |___   ___|    /  ____|  |  ____  |  |__   __|  |   \    | | ")
    print("     | |       |  /       | |    | |     | |     | |\ \   | | ")
    print("     | |       | |        | |    | |     | |     | | \ \  | | ")
    print("     | |       | |        | |    | |     | |     | |  \ \ | | ")
    print("  ___| |       | \_____   | |____| |   __| |__   | |   \ \| | ")
    print(" |_____|       \ ______|  |________|  |_______|  |_|    \___| ")
