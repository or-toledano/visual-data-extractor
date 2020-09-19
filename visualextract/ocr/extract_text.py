"""
SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
extract_text.py: extract text from preprocessed images
"""
import cv2 as cv
import pytesseract
from ..context import wait_space


def from_roi(roi):
    """
    :param roi: grayscale rectangular cut with text
    :return:
    """
    # blur = cv.bilateralFilter(roi, 0, 5, 5)
    # thresh = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv.THRESH_BINARY, 11, 2)
    thresh = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    # OCR engine mode 2 is for Legacy + LSTM engines.
    # Page segmentation mode 6 is for a single uniform block of text
    text = pytesseract.image_to_string(thresh, config="-l eng --oem 3 --psm 6")
    return text
