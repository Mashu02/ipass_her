from PIL import Image, ImageDraw, ImageOps
import random
from math import hypot

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