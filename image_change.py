
'''
Plan!

load image 1 and 2
store both images dimensions and the list of pixel colors

create new image
fill new with background image

check each pixel in green image 1

if pixel is green
    replace new pixel with image 2 rgb
else
    replace new pixel with image 1 rgb

save new image
display new image

green can be generally detected at 86, 196, 61
'''

from PIL import Image

image1 = Image.open("images/harvester.jpg")
image2 = Image.open("images/forest.jpg")
width2, height2 = image2.size
pixels1 = image1.load()
pixels2 = image2.load()

newimg = Image.new("RGB", image2.size)
newpix = newimg.load()

for x in range (0, width2):
    for y in range (0, height2):
        r, g, b = pixels1[x,y]
        # Allow some green detection range, as jpg compression messes with the rbg values a lot
        if ((83 < r < 89) and (193 < g < 199) and (58 < b < 64)):
            newpix[x,y] = pixels2[x,y]
        else:
            newpix[x,y] = pixels1[x,y]

newimg.show()
# Optionally save the image
ask = input("Save image? (y/n)")
if ask.lower() == "y":
    imgname = input("Filename (no extension): ")
    newimg.save(imgname + ".png")