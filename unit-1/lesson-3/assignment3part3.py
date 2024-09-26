import sys
from PIL import Image

# if len(sys.argv) != 3:
#     exit("This command requires two arguments: the filenames of two images")

# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# blended = Image.blend(img1, img2, .4)
# blended.save("blended-" + sys.argv[1] + sys.argv[2])
#I kept getting weird errors until I remembered that someone mentioned the imgs have to be the same dimensions, though I did edit the code so a new name is generated with each save

if len(sys.argv) != 4:
    exit("This command requires three arguments: the filenames of three images")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )

blended = Image.blend(img1, img2, .5)
blended2 = Image.blend(blended, img3, .33)
blended2.save("blended-" + sys.argv[1] + sys.argv[2] + sys.argv[3])
#This is my way of blending 3 or more images, more can be added using the same format as above

