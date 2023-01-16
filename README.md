![ Picture of representation of AI voice recognizers](https://raw.githubusercontent.com/robss2020/computerplayverysexymusic/main/DALLE%202023-01-15-Two%20alluring%20beautiful%20futuristic%20voice%20recognition%20realistic%20robots%2C%20one%20male%20one%20female.%20Ultra%20chic%2C%20ultra%20high%20definition%2C%20ultrarealistic%2C%20romantic.png "Voice recognizers")

## A home automation tool from the Gods

# Ever wish things would just work? Why not do it yourself?

Sometimes you just want to play some sexy music.

Download and install the prerequisites including VLC and you can just say:

"computer play very sexy music" and have it play very sexy music.  No training of the model is required.

This is a demonstration project for hotword listening, you will need to run it whenever you want it running. It is based on the fully offline SpeechRecognition library.

# Installation:

This was tested on Windows. Install anaconda from https://www.anaconda.com/

There are many package managers for Python but this one works well for me.

For best results, from the anaconda prompt run (optional):

conda update pip  
conda update python  
conda update conda

Then from the anaconda prompt run:

pip install SpeechRecognition  
pip install pyaudio

Install VLC: https://www.videolan.org/  
This is not strictly necessary, you can just modify playmusic.bat to do whatever you want rather than start VLC.

The example comes with "Jazz at Mladost Club.mp3" but you can replace this file with whatever file you want.  It is best to choose a music file that is a few hours long.

## Usage

Run `python hotword-listen.py` from anaconda.


## Resources:

https://pypi.org/project/SpeechRecognition/