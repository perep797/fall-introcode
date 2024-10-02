import os
from os import listdir, path
import random
from PIL import Image
import fnmatch

print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration
print("Please note that all input image folders must end in '_imgs'") #the user can use any folder of images they want, as long as the folder name ends in '_img'
print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration
sim_input = input("Type desired level of image similarity from 1-3, type 0 for random:") #takes the string input from user
sim_lvl = int(sim_input) #converts string into integer so math can be done using inputs

folder_list = [] # empty list of folders to choose from
for folder in os.listdir('.'): #searches within cd
    if fnmatch.fnmatch(folder, '*_imgs'): #checks what in cd ends in _imgs
        folder_list.append(folder) #adds all folders ending in _imgs to folder_list

random_folder1 = random.choice(folder_list) #chooses name of one random folder from list 
random_folder2 = random.choice(folder_list) #chooses name of another random folder from list
random_folder3 = random.choice(folder_list) 

folder1_dir = listdir(random_folder1) #directory for chosen folder 1
folder2_dir = listdir(random_folder2) #directory for chosen folder 2
folder3_dir = listdir(random_folder3) #directory for chosen folder 3
random_file1 = random.choice(folder1_dir)
img = Image.open( path.join(random_folder1, random_file1) ) 

img = img.convert("CMYK")
img.getbands()
('C', 'M', 'Y', 'K')
img.save("cmyk"+random_file1)