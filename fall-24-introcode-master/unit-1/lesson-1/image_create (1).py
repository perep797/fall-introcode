
from PIL import Image

# Print a blank line
print("\n")

# Prompt the user for some info
name = input("Please enter a filename: ")
size = int(input("Type a number between 10 and 1000: "))
color = input("Type any color: ")

img = Image.new("RGB",(size,size),color)
img.save(name + ".png")

#this code will not run on my computer for some reason, it says there's 2 erroes in ln 2. Says that the imports could not be resolved from source (Pylance), however I have checked if I have it installed and I do. Not sure what the issue is.
