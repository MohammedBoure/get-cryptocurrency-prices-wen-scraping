def GetDataFromFile(path="site.html"):
    # Get the data from the file
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
        return  data
    