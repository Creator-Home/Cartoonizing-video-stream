import argparse
import cv2

def argument_parser():
    parser = argparse.ArgumentParser(description="Change color space of the \
             input video stream using keyboard controls. The control keys are: \
             Grayscale -'g', YUV -'y', HSV -'h'")
    return parser

if __name__=='__main__':
    args = argument_parser().parse_args()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    cur_char = -1
    pre_char = -1

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(1)

        if c==27:
            break;

        if c>-1 and c != pre_char:
            cur_char = c
        pre_char = c

        if cur_char == ord('g'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif cur_char == ord('y'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        elif cur_char == ord('h'):
            output = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        else:
            output = frame
        cv2.imshow('Webcame', output)

    cap.release()
    cv2.destroyAllWindows()