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
# https://github.com/johnmelodyme/nude.py
#
# 目前僅適用於 Windows vista, 7 , 10
# 支持應用程序將成為蘋果 Macosx

import sys
import subprocess
import pkg_resources

# 檢查 "pillow" 和 "sightengine"" 是否已經安裝:
required_modules = {"nudepy"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
else:
    print("Dependencies Already Installed", required_modules, "\n")

import nude
from nude import Nude

def main():
    # 請插入媒體文件進行分析
    __media_data = input("Please insert a media file for analysis: ")
    __isNude = Nude(__media_data)
    __isNude.parse()
    __isNudeInspection = __isNude.inspect()
    __isNudeResult = __isNude.result
    if "Nude!!" in __isNudeInspection:
        #print("result  ", __isNude.result, __isNude.inspect())
        # 結果: 該圖片包含色情數據
        output = """
        { 
            "nude" = "true";
        }; 
        """
        print(output)
    else:
        # 結果: 該圖片不包含色情數據
        output = """
        { 
            "nude" = "false";
        }; """
        print(output)
    

if __name__ == "__main__":
    main()