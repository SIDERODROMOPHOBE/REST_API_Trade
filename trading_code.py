import urllib.request as ur

def getAllTokenPrice():
    url=ur.urlopen("https://api.binance.com/api/v3/ticker/price")
    print(str(url.read()))



def getBid(symbol):
    print(str(ur.urlopen("https://api.binance.com/api/v3/depth?symbol="+str(symbol)+"&limit=1").read()))
#SUUUUUUUUUUUUUUUUUUUU
getBid("BNBBTC")