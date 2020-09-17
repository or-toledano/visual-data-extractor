import cv2 as cv
import pytesseract


def from_roi(roi):
    """
    :param roi: grayscale rectangular cut with text
    :return:
    """
    thresh = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    # OCR engine mode 2 is for Legacy + LSTM engines.
    # Page segmentation mode 6 is for a single uniform block of text
    text = pytesseract.image_to_string(thresh, config="-l eng --oem 3 --psm 6")
    return text
