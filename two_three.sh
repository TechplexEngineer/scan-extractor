#! /bin/bash

echo "Use Scan Tailor unless your images are all very very good"


exit 1;

set -e

SRCDIR="2_jpg"
OUTDIR="3_cleaned"

mkdir -p "$OUTDIR"

for file in "$SRCDIR"/*.jpg; do
	echo "$file"

	args=(
		# convert document to grayscale before enhancing
	    -g
	    # enhance image brightness before cleaning
	    # choices are: none, stretch or normalize;
	    # default=none
	    #-e stretch
	    # size of filter used to clean background;
	    # integer>0; default=15
	    #-f 12
	    # offset of filter in percent used to reduce noise;
		# integer>=0; default=5
	    #-o 20
	    # text smoothing threshold; 0<=threshold<=100;
		# nominal value is about 50; default is no smoothing
	    #-t 30
	    # unrotate image; cannot unrotate more than about 5 degrees
	    #-u
	    # sharpening amount in pixels; float>=0;
		# nominal about 1; default=0
	    #-s 1
	    # trim background around outer part of image
	    #-T
	    # border pad amount around outer part of image;
		# integer>=0; default=0
	    #-p 20
	    "$SRCDIR/`basename \"$file\"`" 
	    "$OUTDIR/`basename \"$file\"`"
	)

	./lib/textcleaner "${args[@]}"
	break

done
