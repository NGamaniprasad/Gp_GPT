import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_ID = "18bt8r5DZzFIz8UiETCrE1QpcUWLTvN2MC3jlsdJ-So8"

def save_to_sheet(row):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "direct-sale-485906-ba6e8854dba4.json",
        scope
    )

    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
    sheet.append_row(row)
