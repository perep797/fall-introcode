from os import listdir, path
import random
from PIL import Image
#I originally wanted to us numpy to turn imgs into arrays and then switch the columns around individually (so I wouldn't manually need to make masks), but I was unable to get the library to work on my computer

files = listdir("images") #directory of images to choose from
mask_files = listdir("masks") #directory for mask types to chose from

random_file1 = random.choice(files) #chooses first image 
random_file2 = random.choice(files) #chooses second image
random_mask = random.choice(mask_files) #chooses what mask type to use

#names variables and makes sure all are in RGBA so the transparency mask works
img1 = Image.open( path.join("images", random_file1) ).convert('RGBA') 
img2 = Image.open( path.join("images", random_file2) ).convert('RGBA')
# mask_img = Image.open( path.join("masks", random_mask) ).convert('RGBA') #need to clean up the masks

# img_shred_base = Image.alpha_composite(img1, mask_img) #composites the mask onto image 1

# pixeldata = img_shred_base.load() #loads pixel data from composite image
pixeldata = img1.load() #loads pixel data from image 1


# width, height = img_shred_base.size #calculates size of composite image
# for y in range(height):
#     for x in range(width):
#         if pixeldata[x, y] == (0, 0, 0, 255): 
#             pixeldata[x, y] = (0, 0, 0, 0) #detects all black pixels from composite image and replaces them with transparent pixels, working code for mask route

width, height = img1.size #calculates size of composite image
# r = range(i, i+40) #all pixels in a column of 40
# for y in range(height):
#         for x in range(i, width, 40): 
#             pixeldata[x + 40, y] = (0, 0, 0, 0) #detects all pixels in a range from composite image and replaces them with transparent pixels
# i = 0

for y in range(height):
        for x in range(width): 
            if x%40 > 0:
                
                pixeldata[x, y] = (0, 0, 0, 0) #detects all pixels in a range from composite image and replaces them with transparent pixels

img_shred = Image.alpha_composite (img2, img1) #composites image 1 shred and image 2
img_shred.save("shredded-" + random_file1 + random_file2 ) #saves final 'shredded' image, creates unique name based on img input

#////NOTES/////
#maybe write loop that detects numbers divisible by 40, and for that number the next 40 pixels are deleted?
#if pixel in x is divisible by 40, delete the next 40 pixels after it

#for every x value divisible by 40 in the width rage, replace the next 40 pixels with transparency
#need a value that stores every 40th x axis pixel, then have 40 added onto