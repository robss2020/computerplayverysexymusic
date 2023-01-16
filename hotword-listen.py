# Copyright (c) 2023 Robert Viragh under MIT license.

import subprocess
import re
import os
import time

highfidelitymode = False; #set to true to only trigger if it is the recognized phrase (not any of the candidate phrases).

# Put your commands below this line in dictionary format with a command to run in the form of system command.
# to encourage you to automate more of your own system, a complete program must be given as each command, which will be opened as a subprocess.
 
# For best results use sentences consisting of simple unambiguous words
# in a long enough phrase that it will not be said accidentally.

# I have made the program look at all candidates, even ones with low confidence, so don't put short commands here since they could
# be triggered by accident.

#--------Edit this part

commands = {
    "computer play very sexy music": "playmusic.bat",
    "computer test apocalypse": "playtestapocalypse.bat",
    "computer shut down now": "shutdown.bat"
    }


#-----------------------




# ---------
# set the following line to True to be more verbose
PrintAllSpeechEngineOutput = True;


print("-----  Welcome!!  Below you will see the continous output of speech recognition.")
print("-----  When we recognize one of the following hotwords we will take the indicated action")

print(" -------------------------- LIST OF RECOGNIZED COMMANDS ------------------------- ")
for command in commands:
   print("----- When we recognize '", command, "', we will execute: '", commands[command], "'.")

newcommands = {}


# the following would replace each command with "You said " + that command.
# it works because then it would onyl consider the recognized phrase with highest confidence.

# (pop the old key and insert it including the "You said " portion for each key, then replace the commands dictionary with the higher-fidelity version).
if highfidelitymode:
   for command in commands:
       newcommands["You said " + command] = commands[command]
   commands = newcommands
    

# Start speech recognition engine
proc = subprocess.Popen(["python", "-u", "-m", "speech_recognition"], stdout=subprocess.PIPE)


# Iterate through each line of output
timelastdone = {} #the last time we did each action. If it is not set to highfidelitymode then we might see it several times in a row like this:

"""
{   'alternative': [   {   'confidence': 0.97199839,
'transcript': 'computer play very sexy music'},
{'transcript': 'computer plays very sexy music'},
{'transcript': 'computer played very sexy music'}],
'final': True}
You said computer play very sexy music

Which would show 3 canddiate guesses.

In ordinary mode we are interested in whether any one of the alternatives (not just the final recognized alternative)
is the command hotstring, so for this reason we don't want to trip it in case the match regex appears in several candidates since the command
could appear several times in a row as candidates.
"""

for line in iter(proc.stdout.readline, b''):

    if PrintAllSpeechEngineOutput:
        print(line.decode().strip())

    # find all non-overlapping commands
    matches = set()

    todo = [];

    for command in commands:
        for match in re.finditer(command, line.decode()):
            if match.group(0) not in matches:
                matches.add(match.group(0))
                if commands[command] not in todo:
                    todo.append(commands[command])
    
    for item in todo:
       now = time.time()
       if item not in timelastdone or item in timelastdone and (now - timelastdone[item] > 5):
          timelastdone[item] = now
          print("-------- keyword detected so will perform: ", item)
          subprocess.Popen(item)






