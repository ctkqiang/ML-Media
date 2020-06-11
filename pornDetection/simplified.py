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
required_modules = {"nudity"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
else:
    print("Dependencies Already Installed", required_modules, "\n")

from nudity import Nudity

__data = input("Enter a Data for analysis:  \n")
__nude = Nudity()
print(nudity.has(__data))