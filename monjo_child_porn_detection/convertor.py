#!/usr/bin/env python
import PIL
from PIL import Image
import numpy as np

__dataLocation = input()
__image = Image.open(__dataLocation)
np__image = np.array(__image)
print(np__image)