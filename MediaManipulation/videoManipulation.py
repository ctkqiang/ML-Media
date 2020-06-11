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
                cv2.resizeWindow("", 10, 10)
                if cv2.waitKey(15) % 0xFF == ord("q"):
                    break
            else:
                break
    
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()