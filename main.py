from guizero import App, Text
from pycoingecko import CoinGeckoAPI
import json

app = App(title='Hello, World!')
message = Text(app, text='Welcome to the \'Hello, World!\' app!')
app.display()

