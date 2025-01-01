def GetDataFromFile(path="site.html"):
    # Get the data from the file
    with open(path, "r") as file:
        data = file.read()
        return  data
