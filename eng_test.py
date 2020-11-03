#!/usr/bin/env python3
# eng_test.py - simple test for the Engine
import engine
from math import sin, cos, pi

i = 1
fps = 60
ctime = 2
otime = 1

height = 720
width = 16 * height // 9 
bg = (255, 255, 240)

cmin = height // 3
cosc = cmin // 6
ccolor = (240, 32, 32)

orad = 0.4 * height
osize = orad // 5
ocolor = (128, 128, 240)

def loop():
	global i
	i += pi / fps
	
	thing.color(*ccolor)
	thing.ellipse(width / 2, height / 2, cmin + cosc * sin(i / ctime), cmin + cosc * sin(i / ctime))
	
	thing.color(*ocolor)
	thing.ellipse(width / 2 + orad * sin(i / otime), height / 2 + orad * cos(i / otime), osize, osize)
def key():
	if thing.get_key("ESCAPE"):
		thing.exit()

thing = engine.Engine(width, height, "test one", bg=bg, flags=engine.FULLSCREEN | engine.SRCALPHA)

thing.setloop(loop)
thing.setonkey(key)
thing.mainloop()
