from os import listdir, path
import random
from PIL import Image

nature = listdir("nature") #directory of nature images to choose from
man_made = listdir("man-made") #directory of man made images to choose from
buildings = listdir("buildings") #directory of building images to choose from

random_file1 = random.choice(nature) #chooses first image 
random_file2 = random.choice(man_made) #chooses second image
random_file3 = random.choice(buildings) #chooses third image

#just setting the variable names up, makes sure all are in the same format
img1 = Image.open( path.join("nature", random_file1) ).convert('RGB')
img2 = Image.open( path.join("man-made", random_file2) ).convert('RGB')
img3 = Image.open( path.join("buildings", random_file3) ).convert('RGB')
#could try to randomly select for cmyk too?

red_channel = img1.getchannel('R') #extracts the red channel from image 1
green_channel = img2.getchannel('G') #extracts the green channel from image 2
blue_channel = img3.getchannel('B') #extracts the blue channel from image 3

img_shuffle_RGB = Image.merge("RGB", (red_channel, green_channel, blue_channel)) #merges all 3 images nack into a multiband image in RGB mode
img_shuffle_RGB.save("shuffled-" + random_file1 + random_file2 + random_file3 ) #saves image with unique name based off of inputs

#to do: have a path were you choose whether you want the images to be similar(same folder) or different (3 folders), then based on number inputted the channels will either be split into RGB or CMYK

#////TO DO////
#print: Please enter  2 arguments: The desired level of similarity in photo inputs (a number between 1-3), and desired colormode (RGB or CMYK)