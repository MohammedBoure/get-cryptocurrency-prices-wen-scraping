from DataAnalysis import GetIndexesInSTR,GetCurrencyPrices
from HandlingFiles import GetDataFromFile
from GetDataFromSite import GetHTMLGage

GetHTMLGage("site")
htmldata = GetDataFromFile("site.html")
indexs = (GetIndexesInSTR(htmldata))

print(GetCurrencyPrices(htmldata,indexs))