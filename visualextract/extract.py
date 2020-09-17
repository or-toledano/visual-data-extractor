from visualextract.roi.quad_detection import get_quads_approx_poly
from visualextract.roi.rectification import rectified_roi
from visualextract.ocr.extract_text import from_roi
import cv2 as cv


def extract_data(image_path):
    """
    :param image_path: path to image
    :return: data
    """
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    qb = get_quads_approx_poly(image)
    texts = []
    for quad, box in qb:
        if (roi := rectified_roi(image, quad)) is not None:
            texts.append(from_roi(roi))
    return texts
