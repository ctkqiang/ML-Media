#!/usr/bin/env python
import PIL
from PIL import Image
import numpy as np

dataLocation = input("Please input the data:  \n")
image = Image.open(dataLocation)
np__image = np.array(image)
print(np__image) 