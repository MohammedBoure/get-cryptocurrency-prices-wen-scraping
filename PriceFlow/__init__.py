from .DataAnalysis import GetIndexesInSTR,GetCurrencyPrices
from .HandlingFiles import GetDataFromFile
from .GetDataFromSite import GetHTMLGage

GetHTMLGage("site")
htmldata = GetDataFromFile("site.html")
indexs = (GetIndexesInSTR(htmldata))

def fetch_rates(name = "ALL"):
    all_data = GetCurrencyPrices(htmldata,indexs)
    if name == "ALL":
        return all_data
    else:
        if name in all_data:
            return all_data[name]
        else:
            return None

