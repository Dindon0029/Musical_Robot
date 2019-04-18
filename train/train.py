# Musical Robot Project led by Professor Steven Kemper
# Author: Zetao Yu

# Train the model

import subprocess

# Generate NoteSequence Buffer, NoteSequence Examples and train the model
subprocess.call(['./CreateSequence.sh'])

# Currently we only call the script from this python file, but it might be added more functions in the future.

