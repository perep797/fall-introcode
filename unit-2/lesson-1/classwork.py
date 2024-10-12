from os import listdir, path
from PIL import Image, ExifTags
import random

# myList =  ["pau","is","coding"]

# print(myList)

# myList.append("today")

# print(myList)

# isPauInList = "pau" in myList

# print(isPauInList)

#dictionaries, pairs of data
university = {}
university["subject"] = "theory"
university["course"] = "LCOD"
university["department"] = "Lang"
# university["students"] = ["1", "2","3"]
students = ["name1", "name2","name3"]

university["roster"] = students

university["total"] = 0

for item in university.items():
    print(item)
    for x in item:
        if(type(x) is list):
            print("This is not a string, but there are", len(x), "items in list.")

            for i in x:
                university["total"] = university["total"] + 1
        
        if(type(x) is str):
            print("There are",len(x), "characters in this string", x)
        
    


# files= listdir("images")
# image = random.choice(files)
# img = Image.open(path.join("images", image))

