from dotshow.experiment.movie import movshow
from dotshow.matching import __stdshow__
from sys import stdout
import numpy as np
from PIL import Image


__stdshow__(np.array(Image.open("대표최성.png")), gray=False, size=5)

# movshow("hello.mov", gray=True, size=5, limit=5)