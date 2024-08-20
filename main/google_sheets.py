import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load the service account credentials from the JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'sheets.json')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Function to append data to Google Sheets
def append_to_sheet(spreadsheet_id, range_name, values):
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    body = {
        'values': values
    }
    result = sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()
    return result
