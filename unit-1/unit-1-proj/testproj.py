from os import listdir, path
import random
from PIL import Image
import numpy as np

files = listdir("images")

random_file1 = random.choice(files)
random_file2 = random.choice(files)

# img = print( path.join("images",random_file) )
#this was just me making sure that the random image pickers was working

# need to have two random images chosen from the dir
# then have it remove every toher 40 pixels column in img 1 
# blend with img2 or use cut and paste method?

img1 = Image.open( path.join("images",random_file1) ).convert('RGBA') #1st image + makes sure it's in RGBA for transparency

img_arr = np.array(img1) #extracts img into numpy array

img_arr[0 : 400, 0 : 400] = (0, 0, 0, 0) #replaces chosen pixels w transparent pixels

img1_shred = Image.fromarray(img_arr) #creates shredded img from modified array

img2 = Image.open( path.join("images",random_file2) ).convert('RGBA') #2nd image + makes sure it's in RGBA for transparency

blend_img = Image.blend(img1_shred, img2, 0) #blends the two images together
blend_img.save("shredded-" + random_file1 + random_file2 )

# img = print( path.join("images",random_file) )
# cat.paste(mouse, (140, 625), mouse)

# cat.show() #Shows Image
# cat.save('Cat and Mouse.png') #Saves Image