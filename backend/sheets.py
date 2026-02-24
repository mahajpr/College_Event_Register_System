import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet():
    creds_json = os.getenv("GOOGLE_CREDENTIALS")
    creds_dict = json.loads(creds_json)

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet = client.open("College Event Registrations").sheet1
    return sheet

def save_to_sheet(row):
    sheet = get_sheet()
    sheet.append_row(row)
