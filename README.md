# Email Scraper with FastAPI and Google Sheets

## Description

This project is a web application built using **FastAPI** that allows users to log in, scrape comments from a given URL, extract email leads, and save the collected data into a Google Sheet.

## Features

- Password-based login
- User session management
- URL-based comment scraping
- Email lead extraction
- Save leads to Google Sheets
- View scraping results
- Logout functionality

## Technologies Used

- Python
- FastAPI
- Jinja2 Templates
- HTML/CSS
- Google Sheets API
- Session Middleware

## Project Structure

```
Email-Scraper/
│
├── main.py
├── scraper.py
├── sheets.py
│
├── templates/
│   ├── login.html
│   ├── home.html
│   └── result.html
│
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/email-scraper.git
```

### 2. Open Project Folder

```bash
cd email-scraper
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Google Sheets Setup

1. Create a Google Sheet.
2. Enable Google Sheets API.
3. Download Google API credentials.
4. Configure the credentials in `sheets.py`.
5. Add your Sheet ID.

Example:

```python
SHEET_ID = "your_google_sheet_id"
```

## Run the Application

Start FastAPI server:

```bash
uvicorn main:app --reload
```

## Open Browser

Visit:

```
http://127.0.0.1:8000
```

## Application Flow

1. Open login page.
2. Enter password.
3. Access home page.
4. Enter a URL.
5. Scrape comments.
6. Extract email leads.
7. Save emails into Google Sheet.
8. View result.

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Login page |
| `/login` | POST | User authentication |
| `/home` | GET | Main dashboard |
| `/scrape` | POST | Scrape URL comments |
| `/logout` | GET | Logout user |

## Configuration

Update the password in `main.py`:

```python
PASSWORD = "your-password"
```

Update Google Sheet URL:

```python
SHEET_ID = "your-sheet-id"
```

## Future Enhancements

- User registration
- Multiple users
- Better authentication
- Background scraping jobs
- Export CSV files
- Advanced email validation

## License

This project is created for educational purposes.

## Author
N Gamani prasad
