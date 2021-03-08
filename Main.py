import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import time


class Trade:
    def __init__(self, ballence, danger):
        self.b = ballence
        self.wallet = 0
        self.mIn = 0
        self.risk = danger
        self.memory = [0,0]

    def Buy(self, price):
        if self.b > 20:
            self.b -= 20
            self.wallet += 17/price
            self.mIn += 20
        else:
            print("You cannot buy with no money")

    def Sell(self, price):
        if self.mIn < (self.wallet * 0.85 * price) and np.random.randint(0,100) > self.risk:
            self.b += self.wallet * 0.85 * price
            self.wallet = 0
            self.mIn = 0

    def Guess(self, price):
        self.memory.append(price)
        self.memory.pop(0)
        return self.memory[1] > self.memory[0]

pablo = Trade(200,0)
print("Pablo started")


BotRunning = True
while BotRunning:
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-EUR/spot")
    data = response.json()
    price = float(data["data"]["amount"])
    guess = pablo.Guess(price)
    if 0 in pablo.memory:
        #time.sleep(60)
        continue
    if guess == True:
        pablo.Buy(price)
    else:
        pablo.Sell(price)
    print(pablo.b, '€||',pablo.wallet * price, "{")
    time.sleep(60)

print("We earn :", pablo.b + (pablo.wallet * pablo.memory[-1]) - 200, "€")