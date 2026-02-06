import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from scraper import scrape_comments
from sheets import save_to_sheet, SHEET_ID

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="my-super-secret")

PASSWORD = "Gamani123"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"

@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, password: str = Form(...)):
    if password == PASSWORD:
        request.session["user"] = "logged"
        return RedirectResponse("/home", status_code=302)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "❌ Wrong password"}
    )

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    if not request.session.get("user"):
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/scrape", response_class=HTMLResponse)
def scrape(request: Request, url: str = Form(...)):
    if not request.session.get("user"):
        return RedirectResponse("/", status_code=302)

    leads = scrape_comments(url)

    # comment this if Google API is slow
    for lead in leads:
        save_to_sheet(lead)

    if leads:
        message = f"✅ Success! {len(leads)} emails saved"
    else:
        message = "❌ Failed! No emails found"

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "message": message,
            "sheet_url": SHEET_URL,
            "total": len(leads)
        }
    )

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=302)
