import pandas as pd
from math import sqrt
from collections import Counter
import pygame
import colors as c
import pyperclip
import numpy as np
from PIL import Image
import random
import colorsys

#kleuren van algoritme naar rgb codes
colors = [(0, 0, 0), (128, 128, 128), (192, 192, 192), (255, 255, 255), (139, 69, 19), (255, 0, 0)
          , (255, 150, 0), (255, 215, 0), (245, 245, 220), (255, 255, 0), (0, 128, 0), (64, 224, 208), (0, 128, 128)
          , (0, 0, 255), (238, 130, 238), (128, 0, 128), (255, 105, 180)]

colors_in_hsv = [[0, 0.0, 0.0], [0, 0.0, 50.2], [0, 0.0, 75.3], [0, 0.0, 100.0], [25, 86.3, 54.5], [0, 100.0, 100.0]
          , [35, 100.0, 100.0], [51, 100.0, 100.0], [60, 10.2, 96.1], [60, 100.0, 100.0], [120, 100.0, 50.2], [174, 71.4, 87.8], [180, 100.0, 50.2]
          , [240, 100.0, 100.0], [300, 45.4, 93.3], [300, 1000, 50.2], [330, 58.8, 100]]

df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()



def get_key(val):
    """voor rbg value naar text uit dictionary colors.py

    Args:
        val (tuple): value in rbg value waarde

    Returns:
        key (str): de key van de gegeven value
    """
    for key, value in c.color_with_rgb.items():
        if val == value:
            return key

def create_image(colors, size):
    """om een size x size image te genereren met gegeven kleuren maar random plek

    Args:
        colors (list): list van value in rbg value waarde
        size (int): width en heigt in pixel van de generated kleuren

    Returns:
        image (image): een image die gesaved word
    """
    image = Image.new('RGB', (size, size))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image.png')

def create_image2(colors, size):
    """om een size x size image te genereren met gegeven kleuren maar random plek

    Args:
        colors (list): list van value in rbg value waarde
        size (int): width en heigt in pixel van de generated kleuren

    Returns:
        image (image): een image die gesaved word
    """
    image = Image.new('RGB', (size, size))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), random.choice(colors))
    image.save('image2.png')

def list_to_color(tuple):
    """om van de keys uit dictionary naar rgb code in list

    Args:
        tuple (tuple): combinatie van 0 en 1 in een tuple

    Returns:
        list (list): een lijst met waardes van rgb value
    """
    return [color for keep, color in zip(tuple, colors) if keep]



def list_to_color_hsv(tuple):
    """om van de keys uit dictionary naar hsv code in list

    Args:
        tuple (tuple): combinatie van 0 en 1 in een tuple

    Returns:
        list (list): een lijst met waardes van hsv value
    """
    return [color for keep, color in zip(tuple, colors_in_hsv) if keep]

def pilImageToSurface(pilImage):
    """voor PIL image naar pygame

    Args:
        pilImage (png file): PIL image

    Returns:
        image (pygame.image.fromstring): image om te kunnen gebruiken in pygame
    """
    return pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

def data_check():
    """kijkt of de dataset wel echt werkt

    Args:
        None

    Returns:
        True (bool): als er geen [0,0,...] in zit en als die niet leeg is
        False (bool): als er wel [0,0,...] en of leeg is
    """
    if [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] not in df_list and len(df_list) >= 1:
        return True
    else:
        return False

def list_to_clipboard(output_list):
    """copy de gelikte combinations in clip board

    Args:
        output_list (list): lijst die je wilt kopiëren

    Returns:
        None
    """
    if len(output_list) > 0:
        pyperclip.copy('\n'.join(output_list))

def most_picks(combination_nummer):
    """telt hoevaak kleur combinatie is voorgekomen

    Args:
        combination_nummer (str): de combinatie met 0 en 1 in een tuple als string

    Returns:
        c[combination_nummer] (int): hoevaak het voorkomt
    """
    c = Counter()
    for combination in df_list:
        c[str(combination)] += 1
    return (c[combination_nummer])


def cosine_sim(lijst, top_hoeveel, input_user, whole_data_in_list):
    """algoritme cosine similarity met de combinatie van kleuren

    Args:
        lijst (list): input van de gebruiker in lijst van 1 en 0
        top_hoeveel (int): de top hoeveel je wilt in combinatie
        input_user (tuple): de gebruiker input in een tuple om te verwijderen
        whole_data_in_list (list): de hele dataset in een lijst waarmee je wilt vergelijken

    Returns:
        top_dic_keys (list): return de top combinaties van kleuren[0 en 1]en in een list
    """
    combination_with_cosim = {}
    #elke combinatie in de hele dataset
    for x in whole_data_in_list:
        sum = 0
        sumA = 0
        sumB = 0
        for i, j in zip(x, lijst):

            #dot product, doet alle elementen in de gegeven lijst * alle andere elementen in de dataframe
            sum += i * j

            #magnitude, doet elk van de elementen in kwadraat en telt alles op dan pak je de wortel ervan
            sumA += i * i
            sumB += j * j

        cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
        combination_with_cosim[tuple(x)] = cossim

    # remove de input
    if input_user not in combination_with_cosim:
        pass
    else:
        del combination_with_cosim[input_user]

    # de top waardes in een dictionary
    top_dic = dict(Counter(combination_with_cosim).most_common(top_hoeveel))
    top_dic_keys = list(top_dic.keys())
    return top_dic_keys

def cosine_sim_score(lijst, top_hoeveel, input_user, whole_data_in_list):
    """algoritme cosine similarity met de percentage van kleuren

    Args:
        lijst (list): input van de gebruiker in lijst van 1 en 0
        top_hoeveel (int): de top hoeveel je wilt in combinatie
        input_user (tuple): de gebruiker input in een tuple om te verwijderen
        whole_data_in_list (list): de hele dataset in een lijst waarmee je wilt vergelijken

    Returns:
        top_dic_values (list): return de top combinaties met percentage van kleuren
    """
    combination_with_cosim = {}
    for x in whole_data_in_list:
        sum = 0
        sumA = 0
        sumB = 0
        for i, j in zip(x, lijst):
            sum += i * j
            sumA += i * i
            sumB += j * j
        cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
        combination_with_cosim[tuple(x)] = cossim

    # remove de input
    if input_user not in combination_with_cosim:
        pass
    else:
        del combination_with_cosim[input_user]

    # de top waardes in een dictionary
    top_dic = dict(Counter(combination_with_cosim).most_common(top_hoeveel))
    top_dic_values = list(top_dic.values())
    # return list met top 5 als string
    return top_dic_values

def place_button(button, button_color, waar):
    """Om de buttons op het scherm te plaatsen

    Args:
        button (tuple): een rbg value van kleur
        button_color (pygame.Rect): een pygame rect met x,y waarde en width height waarde

    Returns:
        pygame.draw.rect: tekent de button op het scherm met de kleur en button
    """
    return pygame.draw.rect(waar, button, button_color)

def draw_text(text, font, color, surface, x, y):
    """Om de text te plaatsen op het scherm

    Args:
        text (str): text op scherm
        font (pygame.font.SysFont): font en size
        color (tuple): een rbg value van kleur
        surface (pygame.display.set_mode): x en y voor resolutie scherm
        x (int): x waarde van text
        y (int): x waarde van text

    Returns:
        None
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def place_liked_buttons(button_x, button_y,size, waar):
    """voor de green button in feedback

    Args:
        button_x (int): x waarde van button
        button_y (int): y waarde van button
        size (int): width height waarde van button

    Returns:
        None
    """
    green_button = pygame.Rect(button_x, button_y, size, size)
    green_button_black_border = pygame.Rect(button_x - 3, button_y - 3, size + 6, size + 6)
    pygame.draw.rect(waar, c.black, green_button_black_border)
    pygame.draw.rect(waar, (102, 255, 0), green_button)

def rgb_to_hsb(lijst_van_rgb):
    """voor de rgb values te veranderen naar hsv

    Args:
        lijst_van_rgb (list): lijst van rgb values

    Returns:
        hsv (list): hsv waardes in een lijst
    """
    lst = []
    for s_color in lijst_van_rgb:
        lst.append(s_color/255)

    mx = max(lst)
    mn = min(lst)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == lst[0]:
        h = (60 * ((lst[1]-lst[2])/df) + 360) % 360
    elif mx == lst[1]:
        h = (60 * ((lst[2]-lst[0])/df) + 120) % 360
    elif mx == lst[2]:
        h = (60 * ((lst[0]-lst[2])/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return [h, s, v]


def hsb_to_rgb(lijst_van_hsv):
    h = lijst_van_hsv[0] / 360
    s = lijst_van_hsv[1] / 100
    v = lijst_van_hsv[2] / 100
    z = colorsys.hsv_to_rgb(h,s,v)
    h1 = round(z[0] * 255)
    s1 = round(z[1] * 255)
    v1 = round(z[2] * 255)
    return h1,s1,v1

#print(hsb_to_rgb([120,90,46]))

def calc_angle(lijst_van_hsv_values):
    """om de hoek te berekenen met verschillende hsv waardes

    Args:
        lijst_van_hsv_values (list): lijst van hsv values

    Returns:
        lst (list): hsv waardes in een lijst
    """
    lst = []
    counter = 1

    main = (lijst_van_hsv_values[0])
    while counter != len(lijst_van_hsv_values):
        y = [abs(a_i - b_i) for a_i, b_i in zip(main, lijst_van_hsv_values[counter])]
        lst.append(y)
        counter += 1
    return lst



def top_votes(input_GUI_list):
    lst = []
    how_many_1 = input_GUI_list.count(1)
    for single_combo in df_list:
        check_2 = [x + y for x, y in zip(input_GUI_list, single_combo)]
        if int(2) in check_2 and how_many_1 == check_2.count(2):
            lst.append(single_combo)
    for dupe in lst:
        if dupe == input_GUI_list:
            lst.remove(dupe)
    if how_many_1 == 1:
        pass
    else:
        lst.remove(input_GUI_list)
    count = Counter(tuple(item) for item in lst)
    return list(count.keys())


def whole_data_in_hsv():
    lst = []
    for nul_one_combo in df_list:
        z = tuple(nul_one_combo)
        y = list_to_color_hsv(z)
        lst.append(y)
    return lst

def angle_whole_data(lst):
    lsta = []
    for single_hsv_combo in lst:
        z = calc_angle(single_hsv_combo)
        lsta.append(z)
    return lsta


def data_clean(input, whole_data_angles):
    lst = []
    for x in whole_data_angles:
        if len(input) == len(x):
            lst.append(x)
        else:
            pass
    return lst

def data_index_check(input, whole_data_angles):
    lst = []
    for x in whole_data_angles:
        if len(input) + 1 == len(x):
            lst.append(x)
        else:
            pass
    return lst

def cosine_2(v1,v2):
    combination_with_cosim = {}
    c = 0
    while c != len(v2):
        for x in v2[c]:
            sum = 0
            sumA = 0
            sumB = 0
            for i, j in zip(x, v1):
                sum += i * j
                sumA += i * i
                sumB += j * j
            cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
            combination_with_cosim[tuple(x)] = cossim
            c += 1
    return combination_with_cosim

def cosine_3(v1,v2):
    combination_with_cosim = {}
    for x in v2:
        sum = 0
        sumA = 0
        sumB = 0
        for i, j in zip(x, v1):
            sum += i * j
            sumA += i * i
            sumB += j * j
        cossim = sum / ((sqrt(sumA)) * (sqrt(sumB)))
        combination_with_cosim[tuple(x)] = cossim
    return combination_with_cosim

def dict_highest(dict):
    find_max = list(max(dict,key=dict.get))
    return [find_max]

def dict_high(dict):
    find_max = list(max(dict,key=dict.get))
    return find_max

def get_higest_sim_in_hsv(angle):
    lst = whole_data_in_hsv()
    whole_data_angles = angle_whole_data(lst)
    data = data_clean(angle,whole_data_angles)
    data2 = data_index_check(angle, lst)
    dictionary = (cosine_2(angle[0],data))
    index = data.index(dict_highest(dictionary))
    return data2[index]

#print(get_higest_sim_in_hsv([[120, 89.8, 45.89999999999999]]))

def get_higest_sim_in_hsv_2(angle):
    combos = []
    input2 = angle[0] + angle[1]
    lst = whole_data_in_hsv()
    whole_data_angles = angle_whole_data(lst)
    data = data_clean(angle, whole_data_angles)
    data2 = data_index_check(angle, lst)
    for combo in data:
        combos.append(combo[0] + combo[1])
    dictionary = cosine_3(input2, combos)
    index = combos.index(dict_high(dictionary))
    return data2[index]

#print(get_higest_sim_in_hsv_2(calc_angle([[0,100,100],[120,80,80],[240,80,80]])))

def get_higest_sim_in_hsv_3(angle):
    combos = []
    input2 = angle[0] + angle[1] + angle[2]
    lst = whole_data_in_hsv()
    whole_data_angles = angle_whole_data(lst)
    data = data_clean(angle, whole_data_angles)
    data2 = data_index_check(angle, lst)
    for combo in data:
        combos.append(combo[0] + combo[1]+ combo[2])
    dictionary = cosine_3(input2, combos)
    index = combos.index(dict_high(dictionary))
    return data2[index]

print(get_higest_sim_in_hsv_3(calc_angle([[0,100,100],[120,80,80],[240,80,80],[0,80,80]])))