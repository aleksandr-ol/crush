import websocket
import requests
import json
try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(ws)
    print(error)
    print('wer')


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print('open')


# session = requests.Session()
# resp = session.get("http://rustchance.com/feed",
#                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'})
# print(resp.headers)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url="wss://rustchance.com/feed/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
                                        'Accept': '*/*',
                                        'Accept-Encoding': 'gzip, deflate, br',
                                        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                                        'Cache-Control': 'no-cache',
                                        'Connection': 'keep-alive, Upgrade',
                                        'Pragma': 'no-cache',
                                        'Upgrade': 'websocket',
                                        'Cookie': '__cfduid=dc7cc995ea3851dbdd96a37f1e1a65a5b1583355066; cf_clearance=e417c288ec5d9a32420862b2de820de53e1e3794-1584370553-0-150',
                                        })
    ws.on_open = on_open
    ws.run_forever()
