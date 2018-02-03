# -*- coding: utf-8 -*-
from PIL import Image
#im = Image.open("01_white.png")
im = Image.open("transform.png")
rgb_im = im.convert('RGB')
size = rgb_im.size
im2 = Image.new('RGBA',size)
#loop
#x
for x in range(size[0]):
    #y
    for y in range(size[1]):
        r,g,b = rgb_im.getpixel((x,y))
        #print(str(r) + "," + str(g) + "," + str(b))
        if r!=10:
            #print(str(r) + "," + str(g) + "," + str(b))
            r,g,b = 255,255,255
        im2.putpixel((x,y),(r,g,b,0))

im2.show()
