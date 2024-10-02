import os
from os import listdir, path
import random
from PIL import Image
import fnmatch

print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") #silly decoration
print("Please note that all input image folders must end in '_imgs', and all images must be the same size.") #the user can use any folder of images they want, as long as the folder name ends in '_img'
print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") 
mode_input = input("Type desired color output (RGB or CMYK):") #takes input as string


if mode_input == "RGB" or "rgb" == True:
                print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸")
                sim_input = input("Type desired level of image similarity from 1-3:") #takes the string input from user
else:
        if mode_input == "CMYK" or "cmyk" == True:
                print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸")
                sim_input = input("Type desired level of image similarity from 1-4:") #takes the string input from user
        else:
                exit("This command requires the inputs RGB or CMYK, maybe you mistyped?")

sim_lvl = int(sim_input) #converts string into integer so math can be done using inputs

#error handling
# if (sim_lvl < 1 or sim_lvl > 3) and (mode_input == "RGB" or "rgb") == True: 
#         exit("This command requires a number between 1 and 3!")
# if (sim_lvl < 1 or sim_lvl > 4) and (mode_input == "CMYK" or "cmyk") == True: 
#         exit("This command requires a number between 1 and 4!")
# else:
#         exit("This command requires a number!")

folder_list = [] # empty list of folders to choose from
for folder in os.listdir('.'): #searches within cd
    if fnmatch.fnmatch(folder, '*_imgs'): #checks what in cd ends in _imgs
        folder_list.append(folder) #adds all folders ending in _imgs to folder_list

#chooses random folder from folder_list
random_folder1 = random.choice(folder_list) 
random_folder2 = random.choice(folder_list) 
random_folder3 = random.choice(folder_list) 
random_folder4 = random.choice(folder_list)

#Directories for folders
folder1_dir = listdir(random_folder1) 
folder2_dir = listdir(random_folder2) 
folder3_dir = listdir(random_folder3)
folder4_dir = listdir(random_folder4)

#//////For input based level of image similarity//////
#chooses images from the same directory
if sim_lvl == 1:
            random_file1 = random.choice(folder1_dir) 
            random_file2 = random.choice(folder1_dir) 
            random_file3 = random.choice(folder1_dir)

            img1 = Image.open( path.join(random_folder1, random_file1) )
            img2 = Image.open( path.join(random_folder1, random_file2) )
            img3 = Image.open( path.join(random_folder1, random_file3) )
#chooses images from 2 different directories
if sim_lvl == 2:
            random_file1 = random.choice(folder1_dir) 
            random_file2 = random.choice(folder2_dir) 
            random_file3 = random.choice(folder2_dir) 

            img1 = Image.open( path.join(random_folder1, random_file1) )
            img2 = Image.open( path.join(random_folder2, random_file2) )
            img3 = Image.open( path.join(random_folder2, random_file3) )
#chooses images from 3 different directories
if sim_lvl == 3:
            random_file1 = random.choice(folder1_dir) 
            random_file2 = random.choice(folder2_dir) 
            random_file3 = random.choice(folder3_dir) 

            img1 = Image.open( path.join(random_folder1, random_file1) )
            img2 = Image.open( path.join(random_folder2, random_file2) )
            img3 = Image.open( path.join(random_folder3, random_file3) )
#only for cmyk since it requires 4 directories
if sim_lvl == 4 and mode_input == "CMYK" or "cmyk":
            random_file1 = random.choice(folder1_dir) 
            random_file2 = random.choice(folder2_dir) 
            random_file3 = random.choice(folder3_dir)
            random_file4 = random.choice(folder4_dir)

            img1 = Image.open( path.join(random_folder1, random_file1) )
            img2 = Image.open( path.join(random_folder2, random_file2) )
            img3 = Image.open( path.join(random_folder3, random_file3) )
            img4 = Image.open( path.join(random_folder4, random_file4) ) 


if mode_input == "RGB" or "rgb" == True:
        img1.convert("RGB")
        img2.convert("RGB")
        img3.convert("RGB")

        red_channel = img1.getchannel('R') #extracts the red channel from image 1
        green_channel = img2.getchannel('G') #extracts the green channel from image 2
        blue_channel = img3.getchannel('B') #extracts the blue channel from image 3

        img_shuffle = Image.merge("RGB", (red_channel, green_channel, blue_channel)) #merges all 3 images nack into a multiband image in RGB mode
        img_shuffle.save("shuffled-" + random_file1 + random_file2 + random_file3 ) #saves image with unique name based off of inputs
        print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") 
        print("Your image has been shuffled! It has been named shuffled-"+ random_file1 + random_file2 + random_file3) #lets user know command was successful/filename for ease of locating
        print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") 

#same principles as RGB
if mode_input == "CMYK" or "cmyk" == True:
        img1.convert("CMYK")
        img2.convert("CMYK")
        img3.convert("CMYK")
        img4.convert("CMYK")

        cyan_channel = img1.getchannel('C')
        magenta_channel = img2.getchannel('M')
        yellow_channel = img3.getchannel('Y')
        black_channel = img4.getchannel('K')

        img_shuffle = Image.merge("CMYK", (cyan_channel, magenta_channel, yellow_channel, black_channel))
        img_shuffle.save("shuffled-" + random_file1 + random_file2 + random_file3 + random_file4)
        print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") 
        print("Your image has been shuffled! It has been named shuffled-"+ random_file1 + random_file2 + random_file3 + random_file4) 
        print("¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸") 

# ok so basically this doesn't work bc pngs cannots be converted into CMYK mode, and I'm too sleepy to figure out how to convert pngs to jpgs without saving them bc that'll mess with my files too much


