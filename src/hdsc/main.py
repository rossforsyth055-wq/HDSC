import secrets
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pathlib import Path

app = FastAPI(title="Hearts Disabled Supporters Club")
security = HTTPBasic()

USERNAME = "marypoppins"
PASSWORD = "hmfc1963"


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


base_path = Path(__file__).parent
app.mount("/static", StaticFiles(directory=base_path / "static"), name="static")
templates = Jinja2Templates(directory=base_path / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/membership", response_class=HTMLResponse)
async def membership(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("membership.html", {"request": request})


@app.get("/events", response_class=HTMLResponse)
async def events(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("events.html", {"request": request})


@app.get("/news", response_class=HTMLResponse)
async def news(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("news.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.get("/donate", response_class=HTMLResponse)
async def donate(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("donate.html", {"request": request})
