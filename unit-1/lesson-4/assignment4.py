import sys
from PIL import Image 


if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

#test 1
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 60
#         b = 40
#         if x % 50 == 0:
#             b = 100
            
#         if y % 40 == 0:
#             r = 50

#         if y % 30 == 0:
#             r = 50
#             b = 100

#         pixel = (r, 0, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1] + '.jpg')
# For whatever reason my images won't save unless I also specify the file extension

#test idk what number, I just wanted to have weird stripey gradients, I think the math needs to be tweaked bc I can only get gradients with blue/red
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 2
        g = 255
        b = 150

        if x % 100 > 25:
            if r % 100 < 25:
                pixel = (x % r, 0, y % r)
                img.putpixel( (x,y), pixel )

        if y % 50 > 25:
            if b % 50 < 25:
                pixel = (x % b, 0, y % b)
                img.putpixel( (x,y), pixel )

        if x % 100 > 25 and y % 50 > 25:
            if g % 100 < 25:
                pixel = (x % g, 0, y % g)
                img.putpixel( (x,y), pixel )
            

img.save(sys.argv[1] + '.jpg')