# transaudio
# automatically generate audio transcripts

import speech_recognition as sr
r = sr.Recognizer()
af = sr.AudioFile(input('Enter audio file name: '))
with af as src:
  a = r.record(src)
print(r.recognize_google(a))