import os

# Install fastapi and uvicorn modules if not already installed
os.system("pip install fastapi uvicorn")

from fastapi import FastAPI
import asyncio
from random import randrange

app = FastAPI()

score = 0
lives_remaining = 3
eggs = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Egg Catcher Game!"}

@app.get("/score")
def get_score():
    return {"score": score}

@app.get("/lives")
def get_lives():
    return {"lives": lives_remaining}

@app.post("/start_game")
async def start_game():
    global eggs, score, lives_remaining
    score = 0
    lives_remaining = 3
    eggs = []
    await create_egg()
    await move_eggs()
    return {"message": "Game started!"}

async def create_egg():
    while True:
        await asyncio.sleep(4)  # Egg interval of 4 seconds
        x = randrange(10, 740)
        eggs.append({"x": x, "y": 40})
        
@app.get("/catch_egg/{catcher_x}")
def catch_egg(catcher_x: int):
    global score
    for egg in eggs:
        if egg["x"] < catcher_x < egg["x"] + 45 and egg["y"] + 55 > 300:
            score += 10
            eggs.remove(egg)
            break
    return {"score": score}

async def move_eggs():
    while True:
        await asyncio.sleep(0.5)  # Egg speed of 0.5 seconds per move
        for egg in eggs:
            egg["y"] += 10
            if egg["y"] > 400:
                eggs.remove(egg)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("egg:app", host="0.0.0.0", port=8080, log_level="info")
