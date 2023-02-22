import cv2
import numpy as np
from PIL import Image


def resize_image(img, size=(28, 28)):

    h, w = img.shape[:2]
    size = (max(h, w)+20, max(h, w)+20)
    c = img.shape[2] if len(img.shape) > 2 else 1

    if h == w:
        return cv2.resize(img, size, cv2.INTER_AREA)

    dif = h if h > w else w

    interpolation = cv2.INTER_AREA if dif > (
        size[0]+size[1])//2 else cv2.INTER_CUBIC

    x_pos = (dif - w)//2
    y_pos = (dif - h)//2

    if len(img.shape) == 2:
        mask = np.full((dif, dif), 255, dtype=img.dtype)
        # mask.fill(255)
        mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]
    else:
        mask = np.full((dif, dif, c), 255, dtype=img.dtype)
        # mask.fill(255)
        mask[y_pos:y_pos+h, x_pos:x_pos+w, :] = img[:h, :w, :]

    # mask = np.full(size, 255)

    # cv2.imshow('3 Channel Window', mask)
    # print("image shape: ", mask.shape)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return cv2.resize(mask, size, interpolation)


if __name__ == "__main__":
    name = 'birght-lemon-snowdrop.jpg'
    img = cv2.imread(
        f'bad_images/{name}')
    bg = resize_image(img)
    cv2.imwrite(f'bad_images/{name}', bg)
