"""
SPDX-License-Identifier: GPLv3-or-later

Copyright © 2020 Or Toledano

test_roi.py: test file for ROI
"""
import unittest

import cv2 as cv

from visualextract.ocr.extract_text import from_roi
from visualextract.roi.quad_detection import get_quads_approx_poly
from visualextract.roi.rectification import rectified_roi_manual_roll, \
    centroid
from .context import wait_space


def rec_similarity(contour) -> float:
    """
    :param contour: contour
    :return: area/minAreaRect area (not really the extent, because minAreaRect
    isn't necessarily axes-aligned)
    """
    area = cv.contourArea(contour)
    (_x, _y), (w, h), rot = cv.minAreaRect(contour)
    rect_area = w * h
    return area / rect_area


class TestROI(unittest.TestCase):
    def test_roi(self):
        image = cv.imread('./tests/test_images/facebook.jpg')
        wait_space(image)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        wait_space(image)
        qr = get_quads_approx_poly(image)
        for quad, rect in qr:
            im = image.copy()
            cv.drawContours(im, [quad], 0, 50, 3)
            wait_space(im)
            if (roi := rectified_roi_manual_roll(image, quad, 1)) is not None:
                print((txt := from_roi(roi)))
                w = 1300
                h = 100
                c = centroid(quad)
                cv.rectangle(image, (c[0], c[1] - h), (c[0] + w, c[1] + h),
                             (255, 255, 255), -1)
                cv.putText(image, "OCR: " + txt,
                           c,
                           cv.FONT_HERSHEY_SIMPLEX,
                           2,
                           0,
                           5)
                wait_space(image)
                self.assertTrue("Email" in txt)


if __name__ == '__main__':
    unittest.main()
