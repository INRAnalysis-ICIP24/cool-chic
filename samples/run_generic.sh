#!/bin/bash
date

IMAGE_PATH=$1
LAMBDA=$2
OUTPUT_FOLDER=$3
DIST_FN=$4

mkdir -p $OUTPUT_FOLDER

BITSTREAM_PATH=$OUTPUT_FOLDER/compressed.cc1
MODEL_SAVE_PATH=$OUTPUT_FOLDER/model.pt
ENCODER_RESULTS_PATH=$OUTPUT_FOLDER/encoder_results.txt

DECODED_PATH=$OUTPUT_FOLDER/decoded.png
STATS_PATH=$OUTPUT_FOLDER/stats.json

python3 src/encode.py --device=${CC_DEVICE} \
    --input=${IMAGE_PATH} \
    --output=${BITSTREAM_PATH} \
    --model_save_path=${MODEL_SAVE_PATH} \
    --enc_results_path=${ENCODER_RESULTS_PATH} \
    --lmbda=$LAMBDA \
    --start_lr=1e-2 \
    --recipe=faster \
    --layers_synthesis=40-1-linear-relu,3-1-linear-relu,3-3-residual-relu,3-3-residual-none \
    --layers_arm=24,24                              \
    --n_ctx_rowcol=3 \
    --latent_n_grids=7 \
    --dist_fn="${DIST_FN}"

python3 src/decode.py                               \
    --input=${BITSTREAM_PATH}                       \
    --device=${CC_DEVICE} \
    --output=${DECODED_PATH} \
    --image_path=${IMAGE_PATH} \
    --stats_path=${STATS_PATH}

date