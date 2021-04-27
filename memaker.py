import sys,os
from PIL import Image, ImageFont, ImageDraw

image = Image.open(sys.argv[1])
W, H = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('impact.ttf', int(sys.argv[4]))
w, h = draw.textsize(sys.argv[2], font=font)
draw.text(((W-w)/2,0), sys.argv[2], (int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])), font=font)
wx, hx = draw.textsize(sys.argv[3], font=font)
draw.text(((W-wx)/2,H - int(sys.argv[4]) - 15), sys.argv[3], (int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])), font=font)
image.show()
image.save('memeresult.jpg')