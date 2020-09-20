# visual-data-extractor - Computer Vision for Data Extraction
## [Read the docs here](build/docs/content/api-documentation.md)
## Phone screens/documents (rectangles) data extraction
![demo](resources/demo.gif)

My attempt on ROI for rectangular text boxes, "deterministically" (no ML).\
This was made primarily for learning OpenCV purposes;
Use some DL model like OpenCV's EAST for a fast and robust method in real life.
## The pipeline
Detect quads (blur, threshold, approxPolyDP), warp the perspective, \
OCR preprocess (threshold), run OCR, output.
## TODO:
serialize output, save the contour tree structure in a JSON
(switch to RETR_TREE from RETR_EXTERNAL), implement HoughLines method for quad
detection as an alternative.
## Installation
```
git clone https://github.com/or-toledano/visual-data-extractor.git
pip install visual-data-extractor/
```
System dependencies: tesseract, tesseract-ocr-eng
## Usage
The rotate flag is for rotation of the image and each individual roi.
The roi orientation can be estimated but might not always be correct,
so use the --rotate flag to get the results for all of the rotations.
I didn't get much luck with
``` pytesseract.image_to_osd ```
and still need to figure out minAreaRect rotation fix; With the current --rotate
flag the code is trying all 4 rolls for each roi using
```rectified_roi_manual_roll```, which isn't really optimal...\
TL;DR:
```
python -m visualextract --rotate --path <path to image>
```
Or:
```
from visualextract.extract import extract_data
data = extract_data("/image/path/", rotate=<True for now, False in future fix>)
for text in data:
    print(text)
```
---------------
SPDX-License-Identifier: GPLv3-or-later \
Copyright © 2020 Or Toledano
