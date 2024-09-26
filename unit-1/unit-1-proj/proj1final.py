from os import listdir, path
import random
from PIL import Image
import numpy as np

files = listdir("images")

random_file1 = random.choice(files)
random_file2 = random.choice(files)

img1 = Image.open( path.join("images",random_file1) ).convert('RGBA')
img2 = Image.open( path.join("images",random_file2) ).convert('RGBA')

img1 = print( path.join("images",random_file1) )
img2 = print( path.join("images",random_file2) )