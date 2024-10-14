import random
from os import listdir, path
from PIL import Image, ExifTags


files = listdir("images")
random_file = random.choice(files)
img = Image.open(path.join("images", random_file))

exifData = img.getexif()
exifDict = {}

# print(type(exifData))
# says the above is <class 'PIL.Image.Exif'>? Not sure what that means but I was trying to figure out if its a list/object/str/int/dictionary already to see how I couldmanipulate the data?

# print(exifData)
for value in img.getexif().keys():
    print(value, ExifTags.TAGS[value])

#I tried putting the specific number of a key but I got errors about the numberof arguments or int being uncallable


# replacing value with key in the for loop
# 322 TileWidth
# 323 TileLength
# 296 ResolutionUnit
# 34665 ExifOffset
# 271 Make
# 272 Model
# 305 Software
# 274 Orientation
# 306 DateTime
# 282 XResolution
# 283 YResolution
# 316 HostComputer

#I'm kinda confused about what you want us to do here? Is it to call on specific key value pairs within the data? It looks like all the exif data is already printed with the code snippet so I'm not sure what else there is to find