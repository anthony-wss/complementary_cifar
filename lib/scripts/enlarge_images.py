import os, sys
from PIL import Image

size = 300, 300

# print(sys.argv[1:])
# exit()

for infile in sys.argv[1:]:
    outfile = "./large_images/" + os.path.splitext(infile)[0] + ".jpg"
    infile = "images/" + infile
    if infile != outfile:
        try:
            im = Image.open(infile)
            im = im.resize(size)
            im.save(outfile)
        except IOError:
            print(f"cannot create thumbnail for {infile}")

# basewidth = 300
# img = Image.open('somepic.jpg')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save('somepic.jpg')