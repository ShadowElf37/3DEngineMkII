#!/usr/bin/env python3
import engine
e = engine.Engine(400, 300, "testing")
e.color(255, 0, 0)
arr = []
paused = False
e.fontsize(30)
def trip():
	for i in arr:
		e.color(*(i[0]))
		e.ellipse(*(i[1]), 20, 20)
	if paused:
		e.fill(128, 128, 128, 128)
		e.color(255, 255, 255)
		e.text(200, 100, "Paused")
	elif e.getmouse()[0]: # 0 for left, 1 for right, 2 for middle
		arr.append(((128, e.mouseX * 255 / e.width, 255 * (1 - e.mouseY / e.height)), (e.mouseX, e.mouseY)))
def chkpause():
	global paused
	if e.getkey("ESCAPE"):
		paused = not paused
e.setloop(trip)
e.setonkey(chkpause)
e.mainloop()
