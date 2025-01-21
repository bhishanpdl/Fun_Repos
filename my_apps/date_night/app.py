from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random
from fastapi.responses import JSONResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Options for each section
WHAT_TO_EAT = ["Sushi", "Pizza", "Steak", "Indian Curry", "Tacos", "Vegan Delight"]
WHAT_TO_DO = ["Movie Night", "Bowling", "Stargazing", "Cooking Class", "Escape Room", "Board Games"]
AFTER_THAT = ["Dessert Shop", "Night Walk", "Karaoke", "Hot Chocolate at Home", "Drinks at a Bar"]
SEXY_TIME = ["Amazon Dice: Try New Positions", "Massage Each Other", "Bubble Bath", "Role Play", "Romantic Dance"]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/roll/{section}", response_class=JSONResponse)
async def roll(section: str):
    ideas = {
        "What to Eat": WHAT_TO_EAT,
        "What to Do": WHAT_TO_DO,
        "After That": AFTER_THAT,
        "Sexy Time": SEXY_TIME,
    }
    if section not in ideas:
        return JSONResponse({"error": "Invalid section"}, status_code=400)

    result = random.choice(ideas[section])
    return {"section": section, "result": result}
