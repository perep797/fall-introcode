import os
from os import listdir, path
import random
from PIL import Image
import fnmatch
#I originally wanted to use numpy to turn imgs into arrays and then switch the columns around individually (so I wouldn't manually need to make masks), but I was unable to get the library to work on my computer

folder_list = [] # empty list of folders to choose from

for folder in os.listdir('.'): #searches within cd
    if fnmatch.fnmatch(folder, '*_imgs'): #checks what in cd ends in _imgs
        folder_list.append(folder) #adds all folders ending in _imgs to list 

mask_files = listdir("masks") #directory for mask types to chose from

random_folder1 = random.choice(folder_list) #chooses name of one random folder from list 
random_folder2 = random.choice(folder_list) #chooses name of another random folder from list

folder1_dir = listdir(random_folder1) #directory for chosen folder 1
folder2_dir = listdir(random_folder2) #directory for chosen folder 2

random_file1 = random.choice(folder1_dir) #chooses first image from random directory 1
random_file2 = random.choice(folder2_dir) #chooses second image from random directory 2
random_mask = random.choice(mask_files) #chooses what mask type to use

#names variables and makes sure all are in RGBA so the transparency mask works
img1 = Image.open( path.join(random_folder1, random_file1) ).convert('RGBA') 
img2 = Image.open( path.join(random_folder2, random_file2) ).convert('RGBA')
mask_img = Image.open( path.join("masks", random_mask) ).convert('RGBA') #need to clean up the masks

img_shred_base = Image.alpha_composite(img1, mask_img) #composites the mask onto image 1

pixeldata = img_shred_base.load() #loads pixel data from composite image

width, height = img_shred_base.size #calculates size of composite image
for y in range(height):
    for x in range(width):
        if pixeldata[x, y] == (0, 0, 0, 255): 
            pixeldata[x, y] = (0, 0, 0, 0) #detects all black pixels from composite image and replaces them with transparent pixels, working code for mask route


img_shred_final = Image.alpha_composite (img2, img_shred_base) #composites image 1 shred and image 2
img_shred_final.save("shredded-" + random_file1 + random_file2 ) #saves final 'shredded' image, creates unique name based on img input

#////NOTES/////
#maybe write loop that detects numbers divisible by 40, and for that number the next 40 pixels are deleted?
#if pixel in x is divisible by 40, delete the next 40 pixels after it

#for every x value divisible by 40 in the width rage, replace the next 40 pixels with transparency
#need a value that stores every 40th x axis pixel, then have 40 added onto

#///TO DO////
#clean up masks 
#add user input: depending on number inputted the shredding will be at varying levels 
#2 inputs: level of shredding and grid/no grid
#figure out how to do wildcard filepath

#list = ["nature", buildings, man-made]
#choose random from list, set to variable