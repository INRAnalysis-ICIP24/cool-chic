date

#!/bin/bash
IMAGE_PATH=$1
LAMBDA=$2
OUTPUT_FOLDER=$3
DIST_FN=$4

mkdir -p "${OUTPUT_FOLDER}"

BITSTREAM_PATH="${OUTPUT_FOLDER}"/compressed.cc1
DECODED_PATH="${OUTPUT_FOLDER}"/decoded.png
MODEL_SAVE_PATH="${OUTPUT_FOLDER}"/model.pt
ENCODER_RESULTS_PATH="${OUTPUT_FOLDER}"/encoder_results.txt
STATS_PATH="${OUTPUT_FOLDER}"/stats.json

python3 src/encode.py --device=${CC_DEVICE} --input="${IMAGE_PATH}" --output="${BITSTREAM_PATH}" --decoded_img_path="${DECODED_PATH}" --model_save_path="${MODEL_SAVE_PATH}" --enc_results_path="${ENCODER_RESULTS_PATH}" --lmbda=$LAMBDA --start_lr=1e-2 --n_itr=1000 --layers_synthesis=12,12 --layers_arm=12,12 --n_ctx_rowcol=2 --latent_n_grids=7 --n_trial_warmup=5 --stats_path="${STATS_PATH}" --dist_fn="${DIST_FN}"

date
