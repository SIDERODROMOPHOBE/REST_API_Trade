import urllib.request as ur

def getAllTokenPrice():
    url=ur.urlopen("https://api.binance.com/api/v3/ticker/price")
    print(str(url.read()))
