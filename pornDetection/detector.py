#!/usr/bin/env python
# 版權2020©John Melody Me
# 根據Apache許可版本2.0（“許可”）許可；
# 除非遵守許可，否則不得使用此文件。
# 您可以在以下位置獲得許可的副本：
# http://www.apache.org/licenses/LICENSE-2.0
# 除非適用法律要求或書面同意，否則軟件
# 根據許可分發的內容按“原樣”分發，
# 沒有任何明示或暗示的保證或條件。
# 有關特定語言的管理權限，請參閱許可證。
# 許可中的限制。
# @作者：John Melody Me

import PIL
from PIL import Image
import numpy as np
import json
import os
os.system("pip install sightengine")
from sightengine.client import SightengineClient

class porn_detector:
    def main():
        client = SightengineClient('1069852127', 'tLNDZxAArCRND5p8qt7A')
        theSpecialInteger = 18
        dataLocation = input("Please input the data:  \n")
        __image = Image.open(dataLocation)
        np__image = np.array(__image)
        print("Converted Image to Array " , np__image)
        np__image = np__image - theSpecialInteger
        new_image = Image.fromarray(np__image)
        #new_image.save("output.png")
        output = client.check("nudity","wad","offensive","faces","face-attributes", "celebrities").set_file(dataLocation)
        print(json.dumps(output, indent=4, sort_keys=True))

    if __name__ == "__main__":
        main()