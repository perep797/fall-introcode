import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This command requires two arguments: the name of an image file and amount of rotation")

img = Image.open( sys.argv[1] )
rotated_img = img.rotate( int(sys.argv[2]) )
rotated_img.save("rotated-" + sys.argv[1])
#had no problems running this 