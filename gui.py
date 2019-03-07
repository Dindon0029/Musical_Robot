from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, StringVar, END, W, E, N, S, ttk, messagebox
from tkinter.filedialog import askopenfilename
# from sqlalchemy.sql.expression import column
import tkMessageBox
from tkMessageBox import showerror

import stream_to_audio as sta
import audio_to_midi_melodia as atmm
import os
import subprocess
import shutil

class GUI:

    def __init__(self, master):
        self.infile = ""    # path for input wav/mp3
        self.outfile = os.path.dirname(os.path.abspath(__file__))+'/primer/primer.mid'   # path for output MIDI
        self.model = ""   # path for pre-trained model
        self.bpm = StringVar()       # beats per minute
        self.smooth = StringVar()  # smooth the pitch sequence with a median filter of the provided duration (in seconds)
        self.mindura = StringVar()  # minimum allowed duration for note
        self.seconds = 0    # time length for recording

        self.playable = False   # flag for whether to play the generated MIDI files

        self.master = master
        master.title("Musical Robot GUI")

        # text definitions
        self.label = Label(master, text="Musical Robot GUI", font='Helvetica 18 bold')
        self.record_text = Label(master, text="Record your voice here! Please type in seconds: ")
        self.or_text = Label(master, text="OR", font='Helvetica 12 bold')
        self.input_browse_text = Label(master, text="Open an audio file from local: ")
        self.config_text = Label(master, text="How would you like your melody?", font='Helvetica 16 bold')
        self.checkmark1 = Label(master, text=u'\u2713', fg='green')
        self.checkmark2 = Label(master, text=u'\u2713', fg='green')
        # self.saving_text = Label(master, text="Saving path: ")
        self.bpm_text = Label(master, text="Tempo of the track in BPM(beats per min): ")
        self.smooth_text = Label(master, text="Smoothness of pitch sequence: ")
        self.mindura_text = Label(master, text="Minimum duration of each note: ")
        self.model_text = Label(master, text="Choose a pre-trained model: ")

        # button definitions
        self.record_button = Button(master, text="Record", command=lambda: self.record(self.seconds))
        self.browse_music_button = Button(master, text="Browse...", command=lambda: self.browse("music"))
        # self.browse_saving_button = Button(master, text="browse...", command=lambda: self.browse("saving"))
        self.browse_model_button = Button(master, text="Browse...", command=lambda: self.browse("model"))
        self.generate_button = Button(master, text="Generate your own melody", command=lambda: self.generate())
        self.quit_button = Button(master, text="Quit", command=lambda: self.quit())

        # entry and combobox definitions
        vcmd = master.register(self.validate) # we have to wrap the command
        self.recording_seconds_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))    # entry for recording seconds
        self.bpm_combo = ttk.Combobox(master, textvariable=self.bpm,      # bpm combo box
                            values=(
                                    "50(very slow)", 
                                    "63(less slow)",
                                    "70(moderately slow)",
                                    "92(walking speed)",
                                    "114(moderate)",
                                    "144(fast)",
                                    "184(faster)",
                                    "210(even faster)"))
        self.bpm_combo.current(1)
        self.smooth_combo = ttk.Combobox(master, textvariable=self.smooth,    # smoothness combo box
                            values=[
                                    "0.25(default)"])
        self.smooth_combo.current(0)
        self.mindura_combo = ttk.Combobox(master, textvariable=self.mindura,    # minduration combo box
                            values=[
                                    "0.1(default)",
                                    "0.2",
                                    "0.3",
                                    "0.4",
                                    "0.5"])
        self.mindura_combo.current(0)

        # Layouts
        self.label.grid(columnspan=3, sticky=N)
        
        self.record_text.grid(row = 1)
        self.recording_seconds_entry.grid(row = 1, column = 1)
        self.record_button.grid(row = 1, column = 2)
        
        self.or_text.grid(row = 2)
        
        self.input_browse_text.grid(row = 3)
        self.browse_music_button.grid(row = 3, column = 1)
        
        self.checkmark1.grid(row = 3, column = 2)
        self.checkmark1.grid_remove()
        
        self.config_text.grid(row = 4, columnspan=3)
        
        self.bpm_text.grid(row = 5)
        self.bpm_combo.grid(row = 5, column = 1)
        self.smooth_text.grid(row = 6)
        self.smooth_combo.grid(row = 6, column = 1)
        self.mindura_text.grid(row = 7)
        self.mindura_combo.grid(row = 7, column = 1)
        
        self.model_text.grid(row = 8)
        self.browse_model_button.grid(row = 8, column = 1)
        self.checkmark2.grid(row = 8, column = 2)
        self.checkmark2.grid_remove()
        
        self.generate_button.grid(row = 10)
        self.quit_button.grid(row = 10, column = 1)

        root.grid_rowconfigure(9, minsize=30) 
        root.grid_rowconfigure(11, minsize=30) 


    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.seconds = 0
            return True

        try:
            self.seconds = float(new_text)
            return True
        except ValueError:
            return False

    # functionality of record button
    def record(self, seconds):
        if self.infile != "":
            answer = messagebox.askyesno("Warning!","You already have a input file. Would you like to change it?")
            if not answer:
                return
            elif answer == False:
                return
        if seconds > 5 or seconds < 1:    # invalid input
            showerror("Error", "Please type the recording time (1.0s ~ 5.0s) in blank")
            return
        else:
            sta.stream_to_audio(seconds) # record voice in .wav format
            self.infile = "./stream_input.wav" # set up input music file path
            self.seconds = 0
            self.checkmark.grid(row = 3, column = 2)
            return

    def browse(self, sort):
        # if already done recording
        if self.seconds != 0:
            answer = messagebox.askyesno("Warning!","You have already done recording. Would you like to discard the previous recording file?")
            if not answer:
                return
            elif answer == False:
                return

        if sort == "music":
            fname = askopenfilename(filetypes=(("Wav files", "*.wav"),("MP3 files", "*.mp3")))
            if fname:
                try:
                    self.infile = fname
                    print self.infile
                    self.checkmark1.grid(row = 3, column = 2)
                except:                     
                    showerror("Open Source File", "Failed to read file\n'%s'" % fname)
                return
        # elif sort == "saving"
        #     fname = askdirectory()
        #     if fname:
        #         try:
        #             self.outfile = fname+'/primer.mid'
        #         except:                     
        #             showerror("Open Source Directory", "Failed to read directory\n'%s'" % fname)
        #         return
        elif sort == "model":
            fname = askopenfilename(filetypes=(("Model files", "*.mag"),))
            if fname:
                try:
                    self.model = fname
                    print self.model
                    self.checkmark2.grid(row = 8, column = 2)
                except:                    
                    showerror("Open Source File", "Failed to read file\n'%s'" % fname)
                return

    # generate melody according to the information
    def generate(self):
        if not self.infile:
            showerror("Error", "Please choose the audio source first, either by recording or feeding in an audio file.")
            return
        if not self.model:
            showerror("Error", "Please provide model address.")
            return
        bpm1 = self.extractNum(self.bpm.get())
        smooth1 = self.extractNum(self.smooth.get())
        mindura1 = self.extractNum(self.mindura.get())
        atmm.audio_to_midi_melodia(self.infile, self.outfile, bpm1,
                          smooth=smooth1, minduration=mindura1,
                          savejams=False)
        try:
            generate_script_path = os.path.dirname(os.path.abspath(__file__))+'/generate.sh'
            subprocess.call(['chmod', 'a+x', generate_script_path])           # set write and read permission
            subprocess.call(['./generate.sh', self.model])              # call bash script
            self.playable = True                                    # flag to show the play function can be called
        except:
            showerror("Error", "Failed to execute generate.sh")
        return
        # play out the generated files

    # extract float number from a string
    def extractNum(self, str):
        s = str.split("(")
        print s
        try:
            ret = int(s[0])
        except ValueError:
            #Try float.
            ret = float(s[0])

        return ret # return the first float number

    def play(self):
        return

    def quit(self):
        folder = os.path.dirname(os.path.abspath(__file__))+'/output'   # default folder to store all generated MIDI files
        
        answer = messagebox.askyesno("Quit?","Do you want to save your melodies?")
        if not answer:  # user clicks "cancel"
            return
        elif answer == True:    # user clicks "yes"
            messagebox.showinfo("Info", "Your generated MIDI files have been saved in '%s'." % folder)
            global root
            root.destroy()  # exit the program
        elif answer == False:    # user clicks "no"   
            # delete all files and sub-folders under the directory
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path): 
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            # exit the program
            global root
            root.destroy()  # exit the program



root = Tk()
root.protocol("WM_DELETE_WINDOW", quit)     # handle closing event
# root.geometry("600 * 800 + 20 + 20")
my_gui = GUI(root)
root.mainloop()