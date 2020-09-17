"""
quad_detection.py: detect quads
"""

import cv2 as cv
import numpy as np
from numpy import ndarray
from typing import List, Tuple
from better_imshow import wait_space
import sys


def resize(image, width, inter=cv.INTER_AREA) -> Tuple[ndarray, float]:
    """
    :param image: image
    :param width: output width
    :param inter: interpolation method, INTER_AREA by default
    :return: (resized image, input/output ratio)
    """
    h, w = image.shape[:2]
    ratio = width / w
    ratio = min(ratio, 1)
    dim = (int(w * ratio), int(h * ratio))
    return cv.resize(image, dim, interpolation=inter), 1 / ratio


def get_quads_approx_poly(gray, resize_width=250, area_thresh=999,
                          rect_thresh=.5) -> List[Tuple[ndarray, ndarray]]:
    """
    not so robust, approxPolyDP implementation - see get_quads_hough_lines
    :param resize_width: smaller width for intermediate calculations
    :param area_thresh: area threshold for chosen quads
    :param gray: grayscale image
    :param rect_thresh: threshold for bounding-rect-like-area score
    e.i. quads with area/bounding rect area ratio greater than the threshold
    will be considered "good" for further processing
    :return: quads
    """
    resized, ratio = resize(gray, width=resize_width)
    blur = cv.GaussianBlur(resized, (5, 5), 0)
    ret, thresh = cv.threshold(blur, 0, 255,
                               cv.THRESH_OTSU + cv.THRESH_BINARY)
    # kernel = np.ones((5, 5), np.uint8)
    # thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
    wait_space(thresh)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL,
                                          cv.CHAIN_APPROX_SIMPLE)
    quads = []
    small_quads = 0
    for contour in contours:
        perimeter = cv.arcLength(contour, closed=True)
        poly = cv.approxPolyDP(contour, epsilon=.1 * perimeter, closed=True)
        if len(poly) != 4:
            continue
        poly = poly.astype(np.float32)
        poly *= ratio
        poly = poly.astype(np.intp)
        area = cv.contourArea(poly)
        rect = cv.minAreaRect(poly)  # (x, y), (w, h), rot
        rect_area = rect[1][0] * rect[1][1]
        if area < area_thresh or area / rect_area < rect_thresh:
            small_quads += 1
            continue
        box = cv.boxPoints(rect)
        quads.append((poly, box))
    print(f"{small_quads=}", file=sys.stderr)
    return quads


def get_quads_hough_lines():
    """
    More robust than approxPolyDP
    :return:
    """
    pass
