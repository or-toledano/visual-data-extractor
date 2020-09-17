# visual-data-extractor - Computer Vision for Data Extraction
## [Read the docs here](build/docs/content/api-documentation.md)

## Phone screens/documents (rectangles) data extraction
My attempt on ROI for rectangular text boxes, "deterministically" (no ML).\
Use some ML model like OpenCV's EAST in real life for a fast and robust method.\
## The pipeline
Detect quads (blur, threshold), warp the perspective, \
OCR preprocess (threshold), run OCR, output (TODO: serialize output, save 
the contour tree structure in a JSON).
## Installation
```
git clone https://github.com/or-toledano/visual-data-extractor.git
pip install visual-data-extractor/
```
## Usage
```
from visualextract import extract

```
---------------
Made mainly to learn about OpenCV image processing capabilities, EAST should
perform better for the ROI functionality