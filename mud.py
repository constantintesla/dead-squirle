# -*- coding: utf-8 -*-
from gtts import gTTS
from pydub import AudioSegment
from random import randint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
name = randint(0, 2000)
url = "https://www.newsvl.ru/vlad/2020/05/07/189889#comments"
driver.get(url)
driver.implicitly_wait(10)
comments = driver.find_element_by_class_name("leave-comment-link").text
print(comments)
# ctext = driver.find_element_by_class_name("comment-body")
ctext1 = driver.find_elements_by_class_name("comment-text")

commentscount = len(ctext1)
print('количество коментов = '+ str(commentscount))


commenttxt = ''

for i in ctext1:
    commenttxt += i.text + '\n'  # or whatever the way you want to concatenate your text
print(commenttxt)

choosecomment = randint(0, commentscount)
textts = ctext1[choosecomment].text



with open("db.txt", "w",encoding="utf-8") as text_file:
    text_file.write(commenttxt)
    text_file.close()

print('Выбранный коменнт  = ' + str(textts))
tts = gTTS(text=textts, lang='ru')
filename = str(name) + '.mp3'
print('Название файла = ' + filename)
tts.save(filename)

#velocidad_X = 1.5 # No puede estar por debajo de 1.0
#sound = AudioSegment.from_file(filename)
#so = sound.speedup(velocidad_X, 150, 25)
#so.export(filename[:-4] + '_speed.mp3', format = 'mp3')
driver.close()