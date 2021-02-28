from pylibdmtx.pylibdmtx import decode
from PIL import Image
import os
import cv2


def decode_image(image, timeout=3000, max_count=1) -> list:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return decode(thresh, timeout=timeout, max_count=max_count)


if __name__ == "__main__":
    for image in os.listdir("example"):
        frame = cv2.imread(os.path.join("example", image), cv2.IMREAD_UNCHANGED)
        code = decode_image(frame)
        print(image, code)