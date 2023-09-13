import os
import time
import playsound
from gtts import gTTS

os.chdir(r'C:\Users\adminwaan\Documents\git\Dictation MP3 Generator\MP3')

def toMP3(itext):
    tts = gTTS(text=itext, lang="en")
    filename = itext + ".mp3"
    tts.save(filename)

# User https://arraythis.com/ to generate the array
Words = ["GATHER", "LID", "DAMPEN", "NUTRIENTS", "SUITABLE", "HEALTHIER", "POTTING", "CONTENTS", "MIXTURE", "RICH"]

for word in Words:
    toMP3(word)