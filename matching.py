import numpy as np
from .under import under_sampling
from .weight import weight_match

def change_img(arr, gray, size):
    d_arr, real = under_sampling(arr, size=size)
    print("__"*real[0])
    for line in d_arr:
        print("|", end="")
        for var in line:
            val = weight_match(var, gray)
            print(val, end=" ")
        print("|")
    print("__"*real[0])