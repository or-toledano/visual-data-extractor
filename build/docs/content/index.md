# visual-data-extractor - Computer Vision for Data Extraction
## [Read the docs here](build/docs/content/api-documentation.md)
## Phone screens/documents (rectangles) data extraction
My attempt on ROI for rectangular text boxes, "deterministically" (no ML).\
This was made primarily for learning OpenCV purposes;
Use some DL model like OpenCV's EAST for a fast and robust method in real life.\
## The pipeline
Detect quads (blur, threshold), warp the perspective, \
OCR preprocess (threshold), run OCR, output.
## TODO: 
serialize output, save the contour tree structure in a JSON 
(switch to RETR_TREE from RETR_EXTERNAL)), implement HoughLines method for quad 
detection as an alternative.
## Installation
```
git clone https://github.com/or-toledano/visual-data-extractor.git
pip install visual-data-extractor/
```
System dependencies: tesseract, tesseract-ocr-eng
## Usage
```
python -m visualextract <path to image>
```
Or:
```
from visualextract.extract import extract_data
data = extract_data("/path/to/image/", rotate=<Do we need rotations?>)
for text in data:
    print(text)
```
---------------
SPDX-License-Identifier: GPLv3-or-later \
Copyright © 2020 Or Toledano 