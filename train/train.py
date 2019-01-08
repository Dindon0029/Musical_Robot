import subprocess

# Generate NoteSequence Buffer, NoteSequence Examples and train the model
subprocess.call(['./train/CreateSequence.sh'])

# Currently we only call the script from this python file, but it might be added more functions in the future.

