from fastapi import FastAPI
from random import randint
from asyncio import sleep
from pydantic import BaseModel
# create app

app = FastAPI()

# create endpoints for dice game

@app.get('/')
def main():
    return {'message': 'welcome to dice game'}


@app.get('/dice/{num_sides}')
async def diceSimulator(num_sides:int):
    '''Simulate a number obtained for a dice of
    num_sides sides.
    '''
    # simulate time to wait simulation
    await sleep(0.2)
    # create value
    rnd = randint(0,num_sides)
    return {'value': rnd}


# create new bet

class Bet(BaseModel):
    player_name: str
    bet_money: int
    dice_number: int
    bet: int

@app.post('/bet/')
def bet_to_number(bet: Bet):
    """
    Bet certain money to a number given player name and number
    of sides of a dice.
    """
    dice = randint(0, bet.dice_number)
    if dice == bet.bet:
        return {'state': 'winner', 'num': dice, 'earnings': 10*bet.bet_money}
    else:
        return {'state': 'looser', 'num': dice, 'earnings': 0}