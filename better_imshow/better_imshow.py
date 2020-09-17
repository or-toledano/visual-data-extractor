import cv2 as cv


def wait_space(image, title="Output") -> None:
    """
    :param image: image to show
    :param title: frame title
    :return: show image until space press
    """
    if title not in wait_space.titles:
        wait_space.titles.add(title)
        cv.namedWindow(title, cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL)

    while True:
        cv.imshow(title, image)
        if cv.waitKey(0) == ord(' '):
            break


wait_space.titles = set()
