from os import listdir, path
import random
from PIL import Image

files = listdir("images") #directory of images to choose from

random_file1 = random.choice(files) #chooses first image 
random_file2 = random.choice(files) #chooses second image
random_file3 = random.choice(files) #chooses third image

#just setting the variable names up, makes sure all are in the same format
img1 = Image.open( path.join("images", random_file1) ).convert('RGB')
img2 = Image.open( path.join("images", random_file2) ).convert('RGB')
img3 = Image.open( path.join("images", random_file3) ).convert('RGB')
#could try to randomly select for cmyk too?

red_channel = img1.getchannel('R') #extracts the red channel from image 1
green_channel = img2.getchannel('G') #extracts the green channel from image 2
blue_channel = img3.getchannel('B') #extracts the blue channel from image 3

img_shuffle = Image.merge("RGB", (red_channel, green_channel, blue_channel)) #merges all 3 images nack into a multiband image in RBG mode
img_shuffle.save("shuffled-" + random_file1 + random_file2 + random_file3 ) #saves image with unique name based off of inputs

