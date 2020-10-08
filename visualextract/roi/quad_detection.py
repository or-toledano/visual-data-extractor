"""
SPDX-License-Identifier: GPLv3-or-later

Copyright © 2020 Or Toledano

quad_detection.py: detect quads
"""

import sys
from typing import List, Tuple

import cv2 as cv
from numpy import ndarray


def get_quads_approx_poly(gray, area_thresh=999,
                          rect_thresh=.6, epsilon=.025) -> \
        List[Tuple[ndarray, ndarray]]:
    """
    not so robust, approxPolyDP implementation - see get_quads_hough_lines
    :param area_thresh: area threshold for chosen quads
    :param gray: grayscale image
    :param rect_thresh: threshold for bounding-rect-like-area score
    e.i. quads with area/bounding rect area ratio greater than the threshold
    will be considered "good" for further processing
    :param epsilon: epsilon*perimeter -> approxPolyDP's epsilon
    :return: List[(quad, minRectArea around the quad)]
    """
    # blur = cv.GaussianBlur(gray, (5, 5), 0)
    # thresh = cv.threshold(blur, 0, 255,
    #                       cv.THRESH_OTSU + cv.THRESH_BINARY)[1]
    blur = cv.Canny(gray, 30, 200)
    contours = cv.findContours(blur, cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)[0]
    quads = []
    small_quads = 0
    for contour in contours:
        perimeter = cv.arcLength(contour, closed=True)
        poly = cv.approxPolyDP(contour, epsilon=epsilon * perimeter,
                               closed=True)
        if len(poly) != 4:  # quads only!
            continue
        area = cv.contourArea(poly)
        rect = cv.minAreaRect(poly)  # (x, y), (w, h), rot
        rect_area = rect[1][0] * rect[1][1]
        if area < area_thresh or area / rect_area < rect_thresh:
            small_quads += 1
            continue
        quads.append((poly, rect))
    print(f"{small_quads=}", file=sys.stderr)
    return quads


def get_quads_hough_lines() -> List[Tuple[ndarray, ndarray]]:
    """
    More robust than approxPolyDP
    :return: quads
    """
    raise NotImplementedError
