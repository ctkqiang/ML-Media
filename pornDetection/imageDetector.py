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
import sys
import subprocess
import pkg_resources

# 檢查 "pillow" 和 "sightengine"" 是否已經安裝:
required_modules = {"pillow", "sightengine", "requests"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
else:
    print("Dependencies Already Installed", required_modules, "\n")

import PIL
from PIL import Image
import numpy as np
import json
import os
import platform as p
# os.system("pip3 install sightengine")
from sightengine.client import SightengineClient

# 色情照片和視頻探測器:
class porn_image_detector:
    def main():
        # 我使用的是 SightengineApi(“用戶api”，“秘密api”）:
        client = SightengineClient('1069852127', 'tLNDZxAArCRND5p8qt7A')
        # 特別整數: 
        theSpecialInteger = 18
        # 獲取用戶輸入:
        dataLocation = input("Please input the data:  \n")
        # 打開用戶輸入數據
        __image = Image.open(dataLocation)
        # 使用 Numpy 將圖像轉換為數組
        np__image = np.array(__image)
        # 打印出數組的結果
        print("Converted Image to Array " , np__image)
        # 得到十八和以前結果的差別
        np__image = np__image - theSpecialInteger
        # 從數組創建新圖像
        new_image = Image.fromarray(np__image)
        # 保存圖片
        #new_image.save("output.png")

        # 基於操作系統打開圖像或視頻
        computer_platform = p.system()
        if computer_platform == "Windows": 
            __image.show()
            print("The Following Image is Explicit and inappropriate")
        elif computer_platform == "Darwin":
            __image.show()
            os.system("say The Following Image is Explicit and inappropriate")
            print("The Following Image is Explicit and inappropriate")
        elif computer_platform == "Linux":
            __image.show()
            os.system("mplayer The Following Image is Explicit and inappropriate")
            print("The Following Image is Explicit and inappropriate")
        else:
            print("can't open image")

        # 聲明 SightengineApi 檢測功能
        output = client.check("nudity","wad","offensive","faces","face-attributes", "celebrities").set_file(dataLocation)
        # 將輸出和結果打印為 <<json>> 格式

    if __name__ == "__main__":
        main()
        