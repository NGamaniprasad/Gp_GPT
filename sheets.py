import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_ID = ""
"""
Where to find Google Cloud service account key

This is found in Google Cloud Console, not in Sheets.

Steps:

Go to: https://console.cloud.google.com

Select your project (top left)

IAM & Admin → Service Accounts

Click your service account

Go to Keys tab

Add Key → Create new key → JSON

It will download a file to your computer.

That file is the key.  edir direct-sale.json 
"""
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
