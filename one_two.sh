#! /bin/bash


################################################################################
# Convert HEIC images to JPG
################################################################################

set -e

indir=1_source
outdir=2_jpg

mkdir -p ${outdir}

for file in ${indir}/*.heic; do
	out=`basename $file`
	echo "Convert $out"
	heif-convert $file ${outdir}/${out/%.heic/.jpg}
done
