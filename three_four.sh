#! /bin/bash
################################################################################
# Use GNU Parallel to run Tesseract
#################################################################################

# Number of simutaneous tesseract processes to run
THREADS=4

SRCDIR=./3_cleaned
OUTDIR=./4_text

mkdir -p ${OUTDIR}

echo "========="
echo "THIS WILL TAKE A LONG TIME. JUST WAIT!"
echo "========="

time find ${SRCDIR} -maxdepth 1 -iname '*.tif'  | parallel --citation -j${THREADS} \
tesseract {} ${OUTDIR}/{/.} \
	--oem 1 \
	txt


	# -c tessedit_char_whitelist=abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.- \
