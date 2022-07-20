from PIL import Image, ImageDraw, ImageOps
import random
from math import hypot

import algo


def random_circle(colors):
    """random circle generate

    Args:
        colors (list): list met rgb tuple erin

    Returns:
        image : circle.png
    """
    im = Image.new('RGB', (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    n = 0
    while n != 65:
        color = random.choice(colors)
        x = random.randint(-300, 900)
        y = random.randint(-1, 1)
        zz = x * y
        size = random.randint(-300, 1200)
        shape = [(x, zz), size, size]
        draw.ellipse(shape, fill=color)
        n += 1
    color = "black"
    border = (12, 12, 12, 12)
    test = ImageOps.expand(im, border=border, fill=color)
    test.save('circle.png')


def random_rect(colors):
    """random rectangle generate

    Args:
        colors (list): list met rgb tuple erin

    Returns:
        image : rect.png
    """
    im = Image.new('RGB', (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    n = 0
    while n != 65:
        color = random.choice(colors)
        x = random.randint(-300, 900)
        y = random.randint(-1, 1)
        zz = x * y
        size = random.randint(-300, 1200)
        shape = [(x, zz), size, size]
        draw.rectangle(shape, fill=color)
        n += 1

    color = "black"
    border = (12, 12, 12, 12)
    test = ImageOps.expand(im, border=border, fill=color)
    test.save('rect.png')

def random_horizontal(colors):
    im = Image.new('RGB', (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
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
    border = (12, 12, 12, 12)
    test = ImageOps.expand(im, border=border, fill=color)
    test.save('horizontal.png')


def random_diagonal(colors):
    IMG_WIDTH, IMG_HEIGHT = 1000, 1000
    DIAG = round(hypot(IMG_WIDTH, IMG_HEIGHT))

    img = Image.new('RGB', (DIAG, DIAG), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    random.shuffle(colors)

    length = len(colors)  # Number of lines.
    line_width = DIAG / length  # Width of each.
    difx = line_width / 2
    x1, y1 = difx, 0
    x2, y2 = difx, DIAG

    for color in colors:
        endpoints = (x1, y1), (x2, y2)
        draw.line(endpoints, fill=color, width=round(line_width))
        x1 += line_width
        x2 += line_width

    color = "black"
    border = (12, 12, 12, 12)
    img = img.rotate(-45, resample=Image.Resampling.BICUBIC)
    img2 = img.rotate(90, resample=Image.Resampling.BICUBIC)
    difx, dify = (DIAG - IMG_WIDTH) // 2, (DIAG - IMG_HEIGHT) // 2
    img = img.crop((difx, dify, difx + IMG_WIDTH, dify + IMG_HEIGHT))
    img2 = img2.crop((difx, dify, difx + IMG_WIDTH, dify + IMG_HEIGHT))
    test = ImageOps.expand(img, border=border, fill=color)
    test2 = ImageOps.expand(img2, border=border, fill=color)
    test.save('diagonal.png')
    test2.save('diagonal2.png')

def random_vertical(colors):
    IMG_WIDTH, IMG_HEIGHT = 1000, 1000

    img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    random.shuffle(colors)

    length = len(colors)
    amount = IMG_WIDTH / length
    offset = amount / 2
    x1, y1 = offset, 0
    x2, y2 = offset, IMG_HEIGHT

    for color in colors:
        endpoints = (x1, y1), (x2, y2)
        draw.line(endpoints, fill=color, width=int(amount))
        x1 += amount
        x2 += amount

    color = "black"
    border = (12, 12, 12, 12)
    test = ImageOps.expand(img, border=border, fill=color)
    test.save('vertical.png')

#werkt met 1,2,3 input
def complementary(hsv_colors_list):
    lst = []
    lst2 = []
    for x in hsv_colors_list:
        comp = (x[0] + 180)
        if comp > 360:
            comp -= 360
        lst.append(x)
        lst.append([comp,x[1],x[2]])
    for x in lst:
        lst2.append((algo.hsb_to_rgb(x)))

    return lst2

#print(complementary([[320, 100.0, 100.0]]))


def monocromatic(hsv_colors_list):
    lst = []
    lst2 = []
    for x in hsv_colors_list:
        saturation = x[1]
        if saturation <= 50:
            saturation += 25
        else:
            saturation -= 25
    lst.append(x)
    lst.append([hsv_colors_list[0][0],saturation,hsv_colors_list[0][2]])
    for x in lst:
        lst2.append((algo.hsb_to_rgb(x)))
    return lst2

#print(monocromatic([[320, 49.0, 100.0]]))

def analogous(hsv_colors_list):
    lst = []
    lst2 = []
    for x in hsv_colors_list:
        if len(hsv_colors_list) == 1:
            l = x[0] - 30
            r = x[0] + 30
            if l < 0:
                l += 360
            if r > 360:
                r -= 360
            lst.append([l,x[1],x[2]])
            lst.append(x)
            lst.append([r,x[1],x[2]])
            for hsv in lst:
                rgb = algo.hsb_to_rgb(hsv)
                lst2.append(rgb)
        return lst2
#print(analogous([[330, 49.0, 100.0]]))

def analogous_2(hsv_colors_list):
    lst = []
    lst2 = []
    input1 = hsv_colors_list[0]
    input2 = (hsv_colors_list[1])

    average = [(x + y) / 2 for x, y in zip(*hsv_colors_list)]
    lst.append(input1)
    lst.append(average)
    lst.append(input2)

    for hsv in lst:
        rgb = algo.hsb_to_rgb(hsv)
        lst2.append(rgb)
    return lst2

#print(analogous_2([[330, 49.0, 100.0],[100, 49.0, 100.0]]))


#+complementary en dan +30 -30
def split_complementary(hsv_colors_list):
    lst = []
    lst2 = []
    for x in hsv_colors_list:
        comp = (x[0] + 180)
        if comp > 360:
            comp -= 360
        r_comp = comp + 30
        l_comp = comp - 30

        if l_comp <= 0:
            l_comp += 360

        if r_comp > 360:
            r_comp -= 360

        lst.append([r_comp,x[1],x[2]])
        lst.append(x)
        lst.append([l_comp,x[1],x[2]])

    for x in lst:
        lst2.append((algo.hsb_to_rgb(x)))

    return lst2

#print(split_complementary([[200,100,100]]))


def triadic(hsv_colors_list):
    lst = []
    lst2 = []
    for x in hsv_colors_list:
        comp = (x[0] + 180)
        if comp > 360:
            comp -= 360
        r_comp = comp + 60
        l_comp = comp - 60

        if l_comp <= 0:
            l_comp += 360

        if r_comp > 360:
            r_comp -= 360

        lst.append([r_comp,x[1],x[2]])
        lst.append(x)
        lst.append([l_comp,x[1],x[2]])

    for x in lst:
        lst2.append((algo.hsb_to_rgb(x)))
    return lst2

#print(triadic([[200,100,100]]))

def triadic_2(hsv_colors_list):
    lst = []
    lst2 = []
    input1 = hsv_colors_list[0]
    input2 = (hsv_colors_list[1])

    average = [(x + y) / 2 for x, y in zip(*hsv_colors_list)]
    average[0] += 180
    if average[0] > 360:
        average[0] -= 360
    lst.append(input1)
    lst.append(average)
    lst.append(input2)

    for hsv in lst:
        rgb = algo.hsb_to_rgb(hsv)
        lst2.append(rgb)
    return lst2

print(triadic_2([[180,100,100],[1,100,100]]))