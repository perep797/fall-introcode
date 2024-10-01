import fnmatch
import os

for folder in os.listdir('.'):
    if fnmatch.fnmatch(folder, '*_imgs'):
        print(folder)

#I just wanted to test out the fn module to see if I could use it for choosing what folders to draw images from.