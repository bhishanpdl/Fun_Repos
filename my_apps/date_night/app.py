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
WHAT_TO_EAT = [
    "Sushi",
    "Pizza",
    "Indian Curry",
    "Tacos",
    "Vegan Delight"
            ]

WHAT_TO_DO = [
    "Watch a Movie: Rollers gets to choose the genre",
    "Go to Bowling",
    "Read a romantic poetry/song.",
    "Cook something interesting",
    "Attempt a virtual escape room", 
    "Board Games",
    "Join a trivia night",
    "Relive your First Date: Recreate your first dinner or kiss.",
    "Plant a new flower",
    "Sit by the water and enjoy the flow",
    "Explore a neighborhood you have never visited",
    "Watch a sunset together",
    "Tour the New York Public Library",
    "Kayak on The Hudson",
    "Go Ice Skating",
    "Bake together",
    "Plant a tree together",
    "Have a Candlelit Dinner at Home",
    "Eat your breakfast in the bed",
    "Create mocktails together",
    "Spend the day at a museum",
    "Taka coastal walk together",
    "Get Tickets to a Stand-up Comedy Show",
    "Ride a Ferris Wheel or Carnival Ride",
    "Listen to Live Music at a Bar",
    "Have Fun at Topgolf",
    "Buy matching dress together",
    "Do a BBQ",
    "Bake and Decorate Cupcakes",
    "Do a Puzzle Night",
    "Go Hiking",
    "Visit a State Park or National Park",

    ]

AFTER_THAT = [
    "Dessert Shop",
    "Night Walk",
    "Karaoke",
    "Hot Chocolate at Home",
    "Eat Ice-cream",
    "Focus on small romantic gestures like compliments or sharing favorite memories.",
    "Play truth or dare",
    "Learn about yourselves with tarot cards",
    "Take a virtual tour of your favorite city, museum. eg. Louvre or Wadsworth",
    "Go on Zillow and look for your dream home",
    "Watch a TedTalk together",
    "Guess the snack blindfolded",
    "Do yoga together",
    "Make a paper airplane/kite and compete who can fly higher/longer",
    "Paint nail polish on your wife's nails"


            ]

COUPLE_TIME = [
    "Amazon Dice: Try New Positions",
    "Massage Each Other",
    "Bubble Bath", 
    "Role Play",
    "Romantic Dance"
          ]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/roll/{section}", response_class=JSONResponse)
async def roll(section: str):
    ideas = {
        "What to Eat": WHAT_TO_EAT,
        "What to Do": WHAT_TO_DO,
        "After That": AFTER_THAT,
        "Sexy Time": COUPLE_TIME,
    }
    if section not in ideas:
        return JSONResponse({"error": "Invalid section"}, status_code=400)

    result = random.choice(ideas[section])
    return {"section": section, "result": result}
