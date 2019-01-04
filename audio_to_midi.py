# Support converting any audio source into MIDI

import audio_to_midi_melodia as atmm
from stream_to_audio import stream_to_audio
import argparse
import pyaudio
import os

def audio_to_midi(mode, outfile, bpm, smooth=0.25, minduration=0.1, savejams=False):
	if mode == 0: # audio stream
		stream_to_audio()
		infile = "./output.wav"
		atmm.audio_to_midi_melodia(infile, outfile, bpm,
                          smooth=smooth, minduration=minduration,
                          savejams=savejams)
	elif mode == 1:
		infile = raw_input("Please provide your audio file address: ")
		atmm.audio_to_midi_melodia(infile, outfile, bpm,
                          smooth=smooth, minduration=minduration,
                          savejams=savejams)


if __name__ == "__main__":

	# passing arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("mode", type=int, help="Choose the mode of audio source; either an audio file or a real time audio inputstream such as microphone.")
	parser.add_argument("outfile", help="Path for saving output MIDI file.")
	parser.add_argument("bpm", type=int, help="Tempo of the track in BPM.")
	parser.add_argument("--smooth", type=float, default=0.25, help="Smooth the pitch sequence with a median filter of the provided duration (in seconds).")
	parser.add_argument("--minduration", type=float, default=0.1, help="Minimum allowed duration for note (in seconds).Shorter notes will be removed.")
	parser.add_argument("--jams", action="store_const", const=True, default=False, help="Also save output in JAMS format.")

	args = parser.parse_args()

	print args

	# turn audio files/ input stream to midi files
	audio_to_midi(args.mode, args.outfile, args.bpm, smooth=args.smooth, minduration=args.minduration, savejams=args.jams)

	# use the pretrained model to generate a melody
	BUNDLE_PATH = os.path.dirname(os.path.abspath(__file__))+ '/model/basic_rnn.mag'
	CONFIG='basic_rnn'

	# write BUNDLE_PATH and CONFIG into a file as a record, in order to use in the future
	
	# make a system call to generate a melody as a response
	os.system('melody_rnn_generate \
		--config=basic_rnn \
		--bundle_file=${current_path} \
		--output_dir=/Users/stevenyu0029/Desktop/audio_to_midi_melodia/output \
		--num_outputs=10 \
		--num_steps=128 \
		--primer_melody="[60]"')

	# train the model


