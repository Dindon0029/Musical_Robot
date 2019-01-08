#!/bin/sh  
#CreateSequence.bash

#-----------------------------------------------------------------------#

# set permission to be executable
chmod a+x CreateSequence.sh

# Configuration
CONFIG=basic_rnn

# Absolute path this script is in
BASEDIR=$(dirname "$0")
PARENTDIR=$(dirname "$BASEDIR")

# Absolute path of input midi file
TRAIN_FILE='/train_data'
INPUT_DIRECTORY="$BASEDIR$TRAIN_FILE"

# Absolute path of output TFRecord file
TF_FILE='/notesequences.tfrecord'
SEQUENCES_TFRECORD="$BASEDIR$TF_FILE"

# Generate TFRecord file that will contain NoteSequence protocol buffers
convert_dir_to_note_sequences \
  --input_dir=$INPUT_DIRECTORY \
  --output_file=$SEQUENCES_TFRECORD \
  --recursive

#-----------------------------------------------------------------------#

# Absolute path of output sequence examples
EXAMPLE_FILE='/train_data/sequence_examples'
EXAMPLE_DIRECTORY="$BASEDIR$EXAMPLE_FILE"

# Generate examples
melody_rnn_create_dataset \
--config="$CONFIG" \
--input=$SEQUENCES_TFRECORD \
--output_dir=EXAMPLE_DIRECTORY \
--eval_ratio=0.10

#-----------------------------------------------------------------------#
# Absolute path of running directory
RUN='/checkpoints'
RUN_DIR="$BASEDIR$RUN"

# Train and evaluate
melody_rnn_train \
--config="$CONFIG" \
--run_dir=$RUN_DIR \
--sequence_example_file=$EXAMPLE_DIRECTORY \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--num_training_steps=20000 \
--eval

#-----------------------------------------------------------------------#
# Absolute path of model directory
MODEL='/model/run1.mag'
BUNDLE_FILE="$PARENTDIR$MODEL"

# Create a bundle file
melody_rnn_generate \
--config="$CONFIG" \
--run_dir=$RUN_DIR \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--bundle_file=$BUNDLE_FILE \
--save_generator_bundle



