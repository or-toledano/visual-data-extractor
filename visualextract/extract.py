"""
SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
extract.py: user frontend for the module
"""

from visualextract.roi.quad_detection import get_quads_approx_poly
from visualextract.roi.rectification import rectified_roi_bad, rectified_roi
from visualextract.ocr.extract_text import from_roi
import cv2 as cv


def extract_data(image_path, rotate=False):
    """
    :param image_path: image_path
    :param rotate: try all rotations+rolls
    :return: data
    """
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    texts = extract_data_once(image, rotate)
    if rotate:
        for _ in range(3):
            image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
            texts.extend(extract_data_once(image, rotate))
    return texts


def extract_data_once(image, roll):
    """
    :param image: image
    :param roll: try all rolls
    :return: data
    """
    texts = []
    qb = get_quads_approx_poly(image)

    if roll:
        for quad, box in qb:
            for roll in range(4):
                if (roi := rectified_roi_bad(image, quad, roll)) is not None:
                    texts.append(from_roi(roi))
    else:
        for quad, box in qb:
            if (roi := rectified_roi(image, quad)) is not None:
                texts.append(from_roi(roi))

    return texts
