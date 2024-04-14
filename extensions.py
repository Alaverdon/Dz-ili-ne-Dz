import requests
import json

from dz.config import keys


class ConvertionException(Exception):
    pass


class CryproConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Нельзя перевести одно и то же, Бе! {base}!')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Пиши правильно, Бе! {quote}!')

        try:
            base_ticker = keys[base]
        except ValueError:
            raise ConvertionException(f'Пиши правильно, Бе! {base}!')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Число не правильное, Бе! {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base
# Я уеду в Комарово....
