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

<a name="visualextract.roi.rectification.sort_y"></a>
#### sort\_y

```python
sort_y(p0, p1) -> list
```

**Arguments**:

- `p0`: first point
- `p1`: second point

**Returns**:

[minarg_{p0, p1}(p.y), maxarg_{p0, p1}(p.y)]

<a name="visualextract.roi.rectification.sort_quad"></a>
#### sort\_quad

```python
sort_quad(quad: ndarray) -> ndarray
```

**Arguments**:

- `quad`: four points

**Returns**:

four points, starting from the top left, counter clockwise
(positive orientation)

<a name="visualextract.roi.rectification.tup"></a>
#### tup

```python
tup(arr: ndarray) -> tuple
```

**Arguments**:

- `arr`: 1d array

**Returns**:

tuple version of the ndarray

<a name="visualextract.roi.rectification.rect_angle"></a>
#### rect\_angle

```python
rect_angle(rotated_rect)
```

**Arguments**:

- `rotated_rect`: minRectArea output
:return the angle that is required to rotate the rotated_rect back

<a name="visualextract.roi.rectification.centroid"></a>
#### centroid

```python
centroid(contour: ndarray) -> Tuple[int, int]
```

**Arguments**:

- `contour`: contour

**Returns**:

centroid of the contour

<a name="visualextract.roi.rectification.rectified_roi"></a>
#### rectified\_roi

```python
rectified_roi(image: ndarray, quad: ndarray) -> ndarray
```

**Arguments**:

- `image`: base image of the contour
- `quad`: contour to rectify

**Returns**:

a cropped ROI for the rectified quad

<a name="visualextract.roi.rectification.rectified_roi_manual_roll"></a>
#### rectified\_roi\_manual\_roll

```python
rectified_roi_manual_roll(image: ndarray, quad: ndarray, rect: ndarray, roll: int = 0) -> ndarray
```

**Arguments**:

- `image`: base image of the contour
- `quad`: contour to rectify
- `roll`: TODO: figure out why aligned_box needs roll sometimes
roll is in range(4), like a 90 degree fix for the box
- `rect`: pre computed minAreaRect

**Returns**:

a cropped ROI for the rectified quad, but u

<a name="visualextract.roi.rectification.rectified_roi_worst"></a>
#### rectified\_roi\_worst

```python
rectified_roi_worst(image: ndarray, quad: ndarray, rect: ndarray) -> ndarray
```

**Arguments**:

- `image`: base image of the contour
- `quad`: contour to rectify
- `rect`: pre computed minAreaRect

**Returns**:

a cropped ROI for the rectified quad

<a name="visualextract.roi.rectification.rectified_roi_good_no_rotate"></a>
#### rectified\_roi\_good\_no\_rotate

```python
rectified_roi_good_no_rotate(image: ndarray, quad: ndarray, rect: ndarray) -> ndarray
```

**Arguments**:

- `image`: base image of the contour
- `quad`: contour to rectify
- `rect`: pre computed minAreaRect

**Returns**:

a cropped ROI for the rectified quad
IMPORTANT NOTE: the ROI is warped to a plane, but not rotated yet!

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
get_quads_approx_poly(gray, resize_width=500, area_thresh=999, rect_thresh=.6, epsilon=.025) -> List[Tuple[ndarray, ndarray]]
```

not so robust, approxPolyDP implementation - see get_quads_hough_lines

**Arguments**:

- `resize_width`: smaller width for intermediate calculations
- `area_thresh`: area threshold for chosen quads
- `gray`: grayscale image
- `rect_thresh`: threshold for bounding-rect-like-area score
e.i. quads with area/bounding rect area ratio greater than the threshold
will be considered "good" for further processing
- `epsilon`: epsilon*perimeter -> approxPolyDP's epsilon

**Returns**:

List[(quad, minRectArea around the quad)]

<a name="visualextract.roi.quad_detection.get_quads_hough_lines"></a>
#### get\_quads\_hough\_lines

```python
get_quads_hough_lines() -> List[Tuple[ndarray, ndarray]]
```

More robust than approxPolyDP

**Returns**:

quads

<a name="visualextract.roi.edges"></a>
# visualextract.roi.edges

SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
quad_detection.py: detect quads

<a name="visualextract.roi.edges.resize"></a>
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

<a name="visualextract.roi.edges.get_quads_approx_poly"></a>
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

<a name="visualextract.roi.edges.get_quads_hough_lines"></a>
#### get\_quads\_hough\_lines

```python
get_quads_hough_lines()
```

More robust than approxPolyDP

**Returns**:



<a name="visualextract.extract"></a>
# visualextract.extract

SPDX-License-Identifier: GPLv3-or-later
Copyright © 2020 Or Toledano
extract.py: user frontend for the module

<a name="visualextract.extract.extract_data"></a>
#### extract\_data

```python
extract_data(image_path, rotate=False) -> List[str]
```

**Arguments**:

- `image_path`: image_path
- `rotate`: try all rotations+rolls

**Returns**:

all texts extracted (including garbage)

<a name="visualextract.extract.extract_data_once"></a>
#### extract\_data\_once

```python
extract_data_once(image, roll) -> List[str]
```

**Arguments**:

- `image`: image
- `roll`: roll so we can try all rolls

**Returns**:

all texts extracted (including garbage)

