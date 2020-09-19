"""
SPDX-License-Identifier: GPLv3-or-later

Copyright © 2020 Or Toledano

extract.py: user frontend for the module
"""

from typing import List

import cv2 as cv

from visualextract.ocr.extract_text import from_roi
from visualextract.roi.quad_detection import get_quads_approx_poly
from visualextract.roi.rectification import rectified_roi_manual_roll, \
    rectified_roi


def extract_data(image_path, rotate=False) -> List[str]:
    """
    :param image_path: image_path
    :param rotate: try all rotations+rolls
    :return: all texts extracted (including garbage)
    """
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    texts = extract_data_once(image, rotate)
    if rotate:
        for _ in range(3):
            image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
            texts.extend(extract_data_once(image, rotate))
    return texts


def extract_data_once(image, roll) -> List[str]:
    """
    :param image: image
    :param roll: roll so we can try all rolls
    :return: all texts extracted (including garbage)
    """
    texts = []
    qr = get_quads_approx_poly(image)

    if roll:
        for quad, rect in qr:
            for roll in range(4):
                if (roi := rectified_roi_manual_roll(image, quad, rect,
                                                     roll)) is not None:
                    texts.append(from_roi(roi))
    else:
        for quad, rect in qr:
            if (roi := rectified_roi(image, quad)) is not None:
                texts.append(from_roi(roi))

    return texts
