# transaudio
# automatically generate audio transcripts

import speech_recognition as sr
r = sr.Recognizer()
afn = input('Enter audio file name: ')
af = sr.AudioFile(afn)
with af as src:
  a = r.record(src)
res = r.recognize_sphinx(a)
print(res)
with open(afn + '.txt', 'w') as f:
  f.write(res)
print('Output saved to', afn + '.txt')