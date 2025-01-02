import re

def GetIndexesInSTR(htmldata,value='"price":'):
    #Search all indexes containing value
    return [match.start() for match in re.finditer(value, htmldata)]

def getprice(hrmlfile:str,index:int):
    price = hrmlfile[index:index+30].split(":")[1]
    price = price.split(",")[0]
    return price

def getsymbol(hrmlfile: str, indexprice: int):
    if len(hrmlfile) > 200:
        name = hrmlfile[indexprice - 200:indexprice]
    else:
        name = hrmlfile
        
    symbols = GetIndexesInSTR(name, '"symbol":')

    if len(symbols) == 1:
        start_index = symbols[0] + len('"symbol":"')
        end_index = name[start_index:].index('"')
        return name[start_index:start_index + end_index]
    else:
        return None
    
def GetCurrencyPrices(hrmlfile:str,indexs:tuple):
    prices = {}
    for index in indexs:
      price = getprice(hrmlfile,index) 
      name = getsymbol(hrmlfile,index) 
      if name and price:
          prices.update({name:float(price)})
    
    return prices
