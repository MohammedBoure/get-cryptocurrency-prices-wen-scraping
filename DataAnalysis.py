import re

htmldata = "azezaeaezbazeazeazeaezebazeazeazezab"

def GetIndexesInSTR(htmldata,value='"name":'):
    #Search all indexes containing value
    return [match.start() for match in re.finditer(value, htmldata)]

print(GetIndexesInSTR(htmldata,"az"))
