"""
SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
test_roi.py: test file for ROI
"""
import unittest
from .context import wait_space
from visualextract.roi.quad_detection import get_quads_approx_poly
from visualextract.roi.rectification import rectified_roi, rectified_roi_bad
from visualextract.ocr.extract_text import from_roi
import cv2 as cv


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
        qb = get_quads_approx_poly(image)
        for quad, box in qb:
            # cv.drawContours(image, [quad], 0, 50, 3)
            # cv.imshow("Output", image)
            if (roi := rectified_roi_bad(image, quad, 1)) is not None:
                print(from_roi(roi))

        # self.assertTrue(int(input("Enter satisfaction from [0,1]")),
        #                 "Not satisfied") # Annoying a bit


if __name__ == '__main__':
    unittest.main()
