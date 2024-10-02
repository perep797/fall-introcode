import os
from os import listdir, path
import random
from PIL import Image
import fnmatch

print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration
print("Please note that all input image folders must end in '_imgs', and all images must be the same size.") #the user can use any folder of images they want, as long as the folder name ends in '_img'
print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration
shred_input = input("Type desired level of shredding from 1-3, type 0 for random:") #takes the string input from user
shred_lvl = int(shred_input) #converts string into integer so math can be done using inputs

folder_list = [] # empty list of folders to choose from
for folder in os.listdir('.'): #searches within cd
    if fnmatch.fnmatch(folder, '*_imgs'): #checks what in cd ends in _imgs
        folder_list.append(folder) #adds all folders ending in _imgs to folder_list 

mask_files = listdir("masks") #directory for mask types to chose from

#choosing names from folder list
random_folder1 = random.choice(folder_list) 
random_folder2 = random.choice(folder_list) 

#folder directories
folder1_dir = listdir(random_folder1) 
folder2_dir = listdir(random_folder2) 

random_file1 = random.choice(folder1_dir) #chooses first image from random directory 1
random_file2 = random.choice(folder2_dir) #chooses second image from random directory 2
random_mask = random.choice(mask_files) #chooses what mask type to use

#names variables and makes sure all are in RGBA so the transparency mask works
img1 = Image.open( path.join(random_folder1, random_file1) ).convert('RGBA') 
img2 = Image.open( path.join(random_folder2, random_file2) ).convert('RGBA')

#checks value of user input and selects mask accordingly
if shred_lvl == 0:
            mask_img = Image.open( path.join("masks", random_mask) ).convert('RGBA') 
if shred_lvl == 1: 
            mask_img = Image.open( path.join("masks", "mask_1.png") ).convert('RGBA') 
if shred_lvl == 2:
            mask_img = Image.open( path.join("masks", "mask_2.png") ).convert('RGBA') 
if shred_lvl == 3:
            mask_img = Image.open( path.join("masks", "mask_3.png") ).convert('RGBA') 
        
if shred_lvl < 0 or shred_lvl > 3: 
        exit("This command requires a number between 0 and 3!") #exits program if any other input is given

img_shred_base = Image.alpha_composite(img1, mask_img) #composites the mask onto image 1

pixeldata = img_shred_base.load() #loads pixel data from composite image

width, height = img_shred_base.size #calculates size of composite image
for y in range(height):
    for x in range(width):
        if pixeldata[x, y] == (0, 0, 0, 255): 
            pixeldata[x, y] = (0, 0, 0, 0) #detects all black pixels from composite image and replaces them with transparent pixels, working code for mask route


img_shred_final = Image.alpha_composite (img2, img_shred_base) #composites image 1 shred and image 2
img_shred_final.save("shredded-" + random_file1 + random_file2 ) #saves final 'shredded' image, creates unique name based on img input

print("\n")
print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration
print("Your image has been shredded! It has been named shredded-"+ random_file1 + random_file2) #lets user know command was successful/filename for ease of locating
print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration

#////NOTES/////
#I originally wanted to use numpy to turn imgs into arrays and then switch the columns around individually (so I wouldn't manually need to make masks), but I was unable to get the library to work on my computer


 

