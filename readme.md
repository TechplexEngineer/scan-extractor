Scan Extractor
==============

This repo documents the process to extract strucutred data from images of textual data.



## Step 1
Convert HEIC to JPG images
one_two.sh

If your images are already in JPG format. You can skip this step.
If your images are not in HEIC, you may be able to use ImageMagick's Convert program.

## Step 2
Straighten, Dewarp, remove paper, and convert to Black & White
I reccommend using [Scan Tailor](https://scantailor.org/)

If your images are really good. You might be able to use a vairation on
`two_three.sh` which uses [textcleaner by Fred Weinhaus](http://www.fmwconcepts.com/imagemagick/textcleaner/)

## Step 3
Use Tesseract OCR to extract text from the images.
`three_four.sh`

# If you know your input has a limited character set, I have found that using
`tessedit_char_whitelist` eliminates post processing work needed.

## Step 4
Post process the OCR output and generate a CSV.
`process.py`

