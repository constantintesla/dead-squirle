# -*- coding: utf-8 -*-
#file = open("dbtest.txt", "r",encoding="utf-8")
#content = f.read()

import random
lines = open("dbtest.txt", "r", encoding="utf-8").read()

f = lines.replace('\nответить\n','')

lines.splitlines()
myline =random.choice(lines)

print(myline)

