from PIL import Image, ImageDraw, ImageOps
import random

im = Image.new('RGB', (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(im)
colors = [(255,0,255), (0,0,255), (0,255,255)]
random.shuffle(colors)
length = len(colors)
amount = 1000 / length
x1 = 0
y1 = 0
x2 = 1000
y2 = 0
for color in colors:
    shape = [(x1, y1 + amount // 2), (x2, y2 + amount // 2)]
    draw.line(shape, fill=color, width=int(amount))
    y1 += amount
    y2 += amount
color = "black"
border = (10,10,10,10)

im.save("pre_diagonal.png")
colorimage = Image.open('pre_diagonal.png')
out = colorimage.rotate(-45)
test = ImageOps.expand(out, border=border, fill=color)
test.save('diagonal.png')

