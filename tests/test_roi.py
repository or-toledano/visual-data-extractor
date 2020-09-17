import unittest
from better_imshow import wait_space
from visualextract.roi.quad_detection import get_quads_approx_poly
from visualextract.roi.rectification import rectified_roi
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
        image = cv.imread('./test_images/text.png', cv.IMREAD_GRAYSCALE)
        wait_space(image)
        qb = get_quads_approx_poly(image)
        for quad, box in qb:
            cv.drawContours(image, [quad], 0, 50, 3)
            cv.imshow("Output", image)
            if (roi := rectified_roi(image, quad)) is not None:
                m = cv.moments(roi)
                centroid = (
                    int((m["m10"] / m["m00"])), int((m["m01"] / m["m00"])))
                cv.putText(roi, f"{rec_similarity(quad):.2f}", centroid,
                           cv.FONT_HERSHEY_DUPLEX,
                           1, 0, thickness=1)
                wait_space(roi, "ROI detected")
                print(f"{from_roi(roi)=}")
                wait_space(roi, "ROI detected")

        # self.assertTrue(int(input("Enter satisfaction from [0,1]")),
        #                 "Not satisfied") # Annoying a bit


if __name__ == '__main__':
    unittest.main()
