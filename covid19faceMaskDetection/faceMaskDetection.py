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
# @URL: https://github.com/johnmelodyme/Machine-Learning-Porn-detection
#https://aistudio.baidu.com/aistudio/projectdetail/267322
import sys
import subprocess
import pkg_resources

# 檢查 [] 是否已經安裝:
required_modules = {"paddlehub", "matplotlib"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
else:
    print("Dependencies Already Installed", required_modules, "\n")

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
# import paddlehub as hub

# 獲取輸入進行分析 :: 待預測圖片
input_data = ["assets/image/covid1.jpg", "assets/image/covid2.jpg"]
image = mpimg.imread(input_data[1])
# 展示待預測圖片
plt.figure(figsize=(10,10))
plt.imshow(image) 
plt.axis('off') 
plt.show()

with open("covid19faceMaskDetection/output.txt", "r") as f:
    input_data = []
    for line in f:
        input_data.append(line.strip())
print(input_data)


# module = hub.Module(name="pyramidbox_lite_mobile_mask")