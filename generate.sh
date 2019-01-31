#!/bin/sh  
#generate.bash
# shell script used to use pretrained model, to use primer.mid as primer, and generate new midi file as response

# set permission to be executable
chmod a+x generate.sh

# Absolute path this script is in
BASEDIR=$(dirname "$0")

# Concatenate with the model buddle's path
BUNDLEDIR='/model/run1_rnn.mag'
BUNDLE_PATH="$BASEDIR$BUNDLEDIR"

# Concatenate with the output folder's path
OUTPUTDIR='/output'
OUTPUT_PATH="$BASEDIR$OUTPUTDIR"

# Concatenate with the primer midi's path
PRIMERDIR='/primer/primer.mid'
PRIMER_PATH="$BASEDIR$PRIMERDIR"

# Configration
CONFIG=basic_rnn

# Make call and use pretrained model
melody_rnn_generate \
--config="$CONFIG" \
--bundle_file=${BUNDLE_PATH} \
--output_dir=${OUTPUT_PATH} \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60]" \
--primer_midi=${PRIMER_PATH}


