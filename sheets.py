import gspread
from oauth2client.service_account import ServiceAccountCredentials
"""
Step 1: Create the sheet

Go to https://sheets.google.com

Click Blank

Step 2: Copy Sheet ID

From the browser URL:

https://docs.google.com/spreadsheets/d/sheet_id/edit


Copy:

/d/sheet-id/edit/

Step 3: Share with service account

Open your sheet → Share → add:

<client_email from your json>


Example:

"client_email": "my-bot@my-project.iam.gserviceaccount.com"


Give Editor access.

Step 4: Put Sheet ID in code
SHEET_ID = ""

If something fails
Error	Meaning
FileNotFound	Wrong key path
403 forbidden	Sheet not shared
Invalid ID	Copied wrong part
404 not found	Sheet deleted

That’s literally it — no more setup.
Once shared, your app can write to the sheet instantly. """

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

That file is the key.  edit as  direct-sale.json 
"""
def save_to_sheet(row):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "direct-sale.json",
        scope
    )

    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
    sheet.append_row(row)
