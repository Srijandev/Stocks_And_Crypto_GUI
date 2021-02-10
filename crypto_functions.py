from pycoingecko import CoinGeckoAPI
import json

cg = CoinGeckoAPI()
with open('crypto_abbrevs.json') as f:
    crypto_abbrevs = json.load(f)

def capitalize(word):
    lower_word = word.lower()
    new_word = f'{lower_word[0].upper()}{lower_word[1:]}'
    return new_word

coin = input('Coin: ')
currency = input('Currency: ')

raw_data = dict(cg.get_price(ids=f'{coin}', vs_currencies=f'{currency}'))

coin_name = list(raw_data.keys())[0]
coin_value = raw_data[coin_name]
returned_currency = list(coin_value.keys())[0].upper()
coin_value_in_currency = list(coin_value.values())[0]

print(f'{capitalize(coin_name)}:\n{returned_currency}: ${coin_value_in_currency}')


