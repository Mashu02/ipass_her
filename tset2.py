import pandas as pd
import numpy as np
from collections import Counter
from itertools import chain

hsb = [120,100,100]
hsb2 = [240,75,80]
colors_in_hsv = [[0, 0.0, 0.0], [0, 0.0, 50.2], [0, 0.0, 75.3], [0, 0.0, 100.0], [25, 86.3, 54.5], [0, 100.0, 100.0]
          , [35, 100.0, 100.0], [51, 100.0, 100.0], [60, 10.2, 96.1], [60, 100.0, 100.0], [120, 100.0, 50.2], [174, 71.4, 87.8], [180, 100.0, 50.2]
          , [240, 100.0, 100.0], [300, 45.4, 93.3], [300, 1000, 50.2], [330, 58.8, 100]]


df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()

input_GUI_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def top_votes(input_GUI_list):
    lst = []
    full_list_combo_sorted = []
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
    y = (count.most_common())
    for x in y:
        full_list_combo_sorted.append(x[0])
    return full_list_combo_sorted

print(top_votes(input_GUI_list))

def rgb_to_hsb(lijst_van_rgb):
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

#print(rgb_to_hsb([255,27,53]))


def calc_angle(lijst_van_hsv_values):
    lst = []
    counter = 1

    main = np.array(lijst_van_hsv_values[0])
    while counter != len(lijst_van_hsv_values):
        y = abs(main - np.array(lijst_van_hsv_values[counter]))
        lst.append(y)
        counter += 1
    return np.array(lst)

#print(calc_angle([[60, 10.2, 96.1], [60, 100.0, 100.0]]))

#aan input werken
#gui veradneren
#MOET NOG MET 3 KLEUREN

#voor complementary -180 of +180
#triad +150 en dan -150, je hebt dan 3




