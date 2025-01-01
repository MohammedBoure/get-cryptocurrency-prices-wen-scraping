import re

def GetIndexesInSTR(htmldata, value='"symbol":'):
    return [match.start() for match in re.finditer(value, htmldata)]

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

data = '"id":33841,"dataType":2,"name":"EYWA","symbol":"EYWA","slug":"eywa","rank":3008,"status":"active","marketCap":0,"selfReportedMarketCap":6926228.730695369,"priceChange":{'

print(getsymbol(data, len(data) - 1))
