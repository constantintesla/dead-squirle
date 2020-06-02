# -*- coding: utf-8 -*-
from random import randint

from gtts import gTTS
from pydub import AudioSegment
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
name = randint(0, 2000)
url = "https://www.newsvl.ru/vlad/2020/05/28/190445/#comments"
dbname = url.replace('https://www.newsvl.ru/', '').replace('/','-')
print('Название базы = ' + dbname)
driver.get(url)
driver.implicitly_wait(2)
ctext1 = driver.find_elements_by_class_name("comment-text")
commentscount = len(ctext1)-1
print('количество коментов = ' + str(commentscount))

commenttxt = ''

for i in ctext1:
    if i.text != '':
        commenttxt += i.text + '\n'  # or whatever the way you want to concatenate your text
print(commenttxt)

choosecomment = randint(0, commentscount)
print("Выбраный номер комента = " + str(choosecomment))

textts = ctext1[choosecomment].text
print('Выбранный коменнт  = ' + str(textts))
if not textts:
    print("Пустой комент")
    choosecomment = randint(0, commentscount)
    textts = ctext1[choosecomment].text

tts = gTTS(text=textts, lang='ru')
filename = str(name) + '.mp3'
print('Название файла = ' + filename)
tts.save(filename)

dbname = dbname + ".txt"
with open(dbname, "w", encoding="utf-8") as text_file:
    text_file.write(commenttxt)
    text_file.close()

velocidad_X = 1.5  # No puede estar por debajo de 1.0
sound = AudioSegment.from_file(filename)
so = sound.speedup(velocidad_X, 150, 25)
so.export(filename[:-4] + '_speed.mp3', format='mp3')
driver.close()
