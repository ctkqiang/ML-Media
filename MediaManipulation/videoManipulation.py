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
import cv2

def main():
    video = input("Input Video Directory ==> ")
    capture = cv2.VideoCapture(video)
    cv2.namedWindow("", cv2.WINDOW_NORMAL)
    # frame = capture.read()
    if (capture.isOpened == False):
        print("Video Can\'t Play")
    else:
        while (capture.isOpened()):
            ret, frame = capture.read()
            if ret == True:
                capture.set(3, 100)
                capture.set(4, 100)
                cv2.imshow("The Video", frame)
                # cv2.resizeWindow("", 10, 10)
                if cv2.waitKey(15) % 0xFF == ord("q"):
                    break
            else:
                break
    
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()