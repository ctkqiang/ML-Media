#!/usr/bin/env python
import PIL
from PIL import Image
import numpy as np
#pip install sightengine
from sightengine.client import SightengineClient

client = SightengineClient('1069852127', 'tLNDZxAArCRND5p8qt7A')
theSpecialInteger = 18
dataLocation = input("Please input the data:  \n")
__image = Image.open(dataLocation)
np__image = np.array(__image)
print("Converted Image to Array " , np__image)
np__image = np__image - theSpecialInteger
new_image = Image.fromarray(np__image)
#new_image.save("output.png")

output = client.check("nudity","wad","offensive","face-attributes").set_file(dataLocation)
print(output)