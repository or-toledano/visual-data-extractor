"""
SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
rectification.py: warp perspective of quads to rectangles
"""
import cv2 as cv
import numpy as np
from ..context import wait_space
from math import ceil


def sort_y(p0, p1) -> list:
    """
    :param p0: first point
    :param p1: second point
    :return: [minarg_{p0, p1}(p.y), maxarg_{p0, p1}(p.y)]
    """
    return [p0, p1][::(-1) ** (p0[0] > p1[0])]


def sort_quad(quad: np.ndarray) -> np.ndarray:
    """
    :param quad: four points
    :return: four points, starting from the top left, counter clockwise
    (positive orientation)
    """
    l0, l1, r0, r1 = sorted(np.squeeze(quad), key=lambda yx: yx[1])
    tl, bl = sort_y(l0, l1)
    tr, br = sort_y(r0, r1)
    return np.array([tl, tr, br, bl], dtype=np.float32)


def tup(arr: np.ndarray) -> tuple:
    return tuple(d for d in arr)


def rect_angle(rotated_rect):
    """
    :param rotated_rect: minRectArea output
    :return the angle that is required to rotate the rotated_rect back
    """
    (_x, _y), (w, h), theta = rotated_rect
    if w < h:
        return theta - 90
    return theta


def centroid(contour: np.ndarray):
    """
    :param contour: contour
    :return: centroid of the contour
    """
    m = cv.moments(contour)
    return int((m["m10"] / m["m00"])), int((m["m01"] / m["m00"]))


def rectified_roi(image: np.ndarray, quad: np.ndarray) -> np.ndarray:
    """
    :param image: base image of the contour
    :param quad: contour to rectify
    :return: a cropped ROI for the rectified quad
    """
    reordered_quad = sort_quad(quad)
    _x, _y, w, h = cv.boundingRect(quad)
    box = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]],
                   dtype=np.float32)
    m = cv.getPerspectiveTransform(reordered_quad, box)
    return cv.warpPerspective(image, m, (w, h))


def rectified_roi_bad(image: np.ndarray, quad: np.ndarray,
                      roll: int = 0) -> np.ndarray:
    """
    :param image: base image of the contour
    :param quad: contour to rectify
    :param roll: TODO: figure out why aligned_box needs roll sometimes
    :return: a cropped ROI for the rectified quad
    """
    rect = cv.minAreaRect(quad)
    rect_box = cv.boxPoints(rect)
    quad, rect_box = sort_quad(quad), sort_quad(rect_box)
    rect_box -= rect_box.min(axis=0, initial=None)  # translation to 0
    m0 = cv.getPerspectiveTransform(quad.astype(np.float32),
                                    rect_box)
    w, h = (ceil(size_cord) for size_cord in rect[1])
    aligned_box = np.roll(
        np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]],
                 dtype=np.float32), roll, axis=0)
    m1 = cv.getPerspectiveTransform(rect_box, aligned_box)

    pers = cv.warpPerspective(image, m1 @ m0, (w, h))

    return pers


def rectified_roi_worst(image: np.ndarray, quad: np.ndarray) -> np.ndarray:
    """
    :param image: base image of the contour
    :param quad: contour to rectify
    :return: a cropped ROI for the rectified quad
    """
    rect = cv.minAreaRect(quad)
    box = cv.boxPoints(rect)
    quad, box = sort_quad(quad), sort_quad(box)
    obox = box.copy()
    box -= box.min(axis=0, initial=None)  # translation to 0
    m0 = cv.getPerspectiveTransform(quad.astype(np.float32), box)
    pers = cv.warpPerspective(image, m0, tup(box.max(axis=0, initial=None)))
    # wait_space(pers)
    nobox = obox.reshape(1, *obox.shape)
    nbox = np.squeeze(cv.perspectiveTransform(nobox, m0))
    cv.drawContours(pers, [obox.astype(np.intp)], 0, 255, 2)
    # wait_space(pers)
    center = centroid(nbox)
    rot = cv.getRotationMatrix2D(center, angle=rect_angle(rect), scale=1)
    w, h = (ceil(1 * size_cord) for size_cord in rect[1])
    return cv.warpAffine(src=pers, M=rot, dsize=(w, h))


def rectified_roi_good_no_rotate(image: np.ndarray, quad: np.ndarray,
                                 ) -> np.ndarray:
    """
    :param image: base image of the contour
    :param quad: contour to rectify
    :return: a cropped ROI for the rectified quad
    IMPORTANT NOTE: the ROI is warped to a plane, but not rotated yet!
    """
    mask = np.zeros_like(image)
    cv.drawContours(mask, [quad], 0, 255, -1)
    image = cv.bitwise_and(image, mask)
    rect = cv.minAreaRect(quad)
    box = cv.boxPoints(rect)
    quad, box = sort_quad(quad), sort_quad(box)
    box -= box.min(axis=0, initial=None)  # translation to 0
    m = cv.getPerspectiveTransform(quad.astype(np.float32), box)
    pers = cv.warpPerspective(image, m, tup(box.max(axis=0, initial=None)))
    return pers
