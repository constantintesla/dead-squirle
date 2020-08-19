# -*- coding: utf-8 -*-
from random import randint
from gtts import gTTS
import playsound

import random

s = open("C:\\Users\\khlystov.ka\\coms.txt", "r", encoding="utf-8")
m = s.readlines()
l = []
for i in range(0, len(m) - 1):
    x = m[i]
    z = len(x)
    a = x[:z - 1]
    l.append(a)
l.append(m[i + 1])
o = random.choice(l)
print(o)
s.close()
tts = gTTS(text=o, lang='ru')
filename = 'comment' + '.mp3'
print('Название файла = ' + filename)
tts.save(filename)
playsound.playsound(filename, True)