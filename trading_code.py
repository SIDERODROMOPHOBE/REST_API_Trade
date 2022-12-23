import urllib.request as ur
import json
def getAllTokenPrice():
    print(str(ur.urlopen("https://api.binance.com/api/v3/ticker/price").read()))



def getBid(symbol):
    print(str(ur.urlopen("https://api.binance.com/api/v3/depth?symbol="+str(symbol)+"&limit=1").read()))

def getDepth(direction,asset):
    url="https://api.binance.com/api/v3/ticker/bookTicker?symbol="+str(asset)
    jason=ur.urlopen(url).read()
    jason2=jason.decode('utf-8')
    datas=json.loads(jason2)

    print(asset,' current ',direction,' price is : ',datas[direction+'Price'])
    

