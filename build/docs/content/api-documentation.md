<a name="__init__"></a>
# \_\_init\_\_

<a name="__main__"></a>
# \_\_main\_\_

<a name="better_imshow"></a>
# better\_imshow

<a name="better_imshow.better_imshow"></a>
# better\_imshow.better\_imshow

<a name="better_imshow.better_imshow.wait_space"></a>
#### wait\_space

```python
wait_space(image, title="Output") -> None
```

**Arguments**:

- `image`: image to show
- `title`: frame title

**Returns**:

show image until space press

<a name="visualextract"></a>
# visualextract

cvrecon module - Computer Vision for Reconnaissance applications

<a name="visualextract.ocr"></a>
# visualextract.ocr

ocr module - extract text from images

<a name="visualextract.ocr.extract_text"></a>
# visualextract.ocr.extract\_text

SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
extract_text.py: extract text from preprocessed images

<a name="visualextract.ocr.extract_text.from_roi"></a>
#### from\_roi

```python
from_roi(roi)
```

**Arguments**:

- `roi`: grayscale rectangular cut with text

**Returns**:



<a name="visualextract.__main__"></a>
# visualextract.\_\_main\_\_

<a name="visualextract.write_data"></a>
# visualextract.write\_data

write_data module - format and write extracted data

<a name="visualextract.roi"></a>
# visualextract.roi

roi module - detect relevant quads and preprocess them before ocr

<a name="visualextract.roi.rectification"></a>
# visualextract.roi.rectification

SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
rectification.py: warp perspective of quads to rectangles

<a name="visualextract.roi.rectification.swap_y"></a>
#### swap\_y

```python
swap_y(p0, p1) -> list
```

**Arguments**:

- `p0`: first point
- `p1`: second point

**Returns**:

[minarg_{p0, p1}(p.y), maxarg_{p0, p1}(p.y)]

<a name="visualextract.roi.rectification.rectified_roi"></a>
#### rectified\_roi

```python
rectified_roi(image: np.ndarray, quad: np.ndarray) -> np.ndarray
```

**Arguments**:

- `image`: base image of the contour
- `quad`: contour to rectify

**Returns**:

a cropped ROI for the rectified quad

<a name="visualextract.roi.quad_detection"></a>
# visualextract.roi.quad\_detection

SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
quad_detection.py: detect quads

<a name="visualextract.roi.quad_detection.resize"></a>
#### resize

```python
resize(image, width, inter=cv.INTER_AREA) -> Tuple[ndarray, float]
```

**Arguments**:

- `image`: image
- `width`: output width
- `inter`: interpolation method, INTER_AREA by default

**Returns**:

(resized image, input/output ratio)

<a name="visualextract.roi.quad_detection.get_quads_approx_poly"></a>
#### get\_quads\_approx\_poly

```python
get_quads_approx_poly(gray, resize_width=250, area_thresh=999, rect_thresh=.5) -> List[Tuple[ndarray, ndarray]]
```

not so robust, approxPolyDP implementation - see get_quads_hough_lines

**Arguments**:

- `resize_width`: smaller width for intermediate calculations
- `area_thresh`: area threshold for chosen quads
- `gray`: grayscale image
- `rect_thresh`: threshold for bounding-rect-like-area score
e.i. quads with area/bounding rect area ratio greater than the threshold
will be considered "good" for further processing

**Returns**:

quads

<a name="visualextract.roi.quad_detection.get_quads_hough_lines"></a>
#### get\_quads\_hough\_lines

```python
get_quads_hough_lines()
```

More robust than approxPolyDP

**Returns**:



<a name="visualextract.context"></a>
# visualextract.context

<a name="visualextract.extract"></a>
# visualextract.extract

SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
extract.py: user frontend for the module

<a name="visualextract.extract.extract_data"></a>
#### extract\_data

```python
extract_data(image_path)
```

**Arguments**:

- `image_path`: path to image

**Returns**:

data

