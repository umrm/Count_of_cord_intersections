import re
import ast
import numpy as np
from math import pi
from itertools import combinations

def get_intersections(input_val):
    chords = {}

    for radian, identifier in zip(input_val[0], input_val[1]):
        chord_no = int (re.findall ('\\d+', identifier ) [0])
        if chord_no in chords:
            chords[chord_no].append(radian % (2 * pi))
            chords[chord_no].sort()
        else:
            chords[chord_no] = [radian % (2 * pi)]

    num_intrsc = 0
    chord_list = list(chords.values())
    for chord_1, chord_2 in combinations(chord_list, 2):
        s_1, e_1 = chord_1
        s_2, e_2 = chord_2
        if (s_1 < s_2 < e_1) ^ (s_1 < e_2 < e_1):
            num_intrsc += 1
    return num_intrsc
    
user_input = input("Enter the input: ")
input_val = ast.literal_eval(user_input)
no_of_intersections = get_intersections(input_val)

print(f"The number of cord intersection inside the circle is {no_of_intersections}")

