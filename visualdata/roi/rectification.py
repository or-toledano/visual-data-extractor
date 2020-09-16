"""
rectification.py: warp perspective of quads to rectangles
"""
import cv2 as cv
import numpy as np


def swap_y(p0, p1) -> list:
    """
    :param p0: first point
    :param p1: second point
    :return: [minarg_{p0, p1}(p.y), maxarg_{p0, p1}(p.y)]
    """
    return [p0, p1][::(-1) ** (p0[0] > p1[0])]


def rectified_roi(image: np.ndarray, quad: np.ndarray) -> np.ndarray:
    """
    :param image: base image of the contour
    :param quad: contour to rectify
    :return: a cropped ROI for the rectified quad
    """
    x, y, w, h = cv.boundingRect(quad)
    l0, l1, r0, r1 = sorted(np.squeeze(quad), key=lambda yx: yx[1])
    lt, lb = swap_y(l0, l1)
    rt, rb = swap_y(r0, r1)
    reordered_quad = np.array([lt, rt, rb, lb], dtype=np.float32)
    box = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]],
                   dtype=np.float32)
    m = cv.getPerspectiveTransform(reordered_quad, box)
    return cv.warpPerspective(image, m, (w, h))
