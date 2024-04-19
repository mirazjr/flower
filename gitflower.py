from turtle import *

import colorsys

bgcolor('black')
tracer (200)
def draw():
	h = 0
	for i in range(100):
		c = colorsys.hsv_to_rgb(h,1,1)
		h += 0.05
		up()
		goto (0,0)
		down()
		color('black')
		fillcolor (c)
		begin_fill()
		rt (7)
		circle(i, 27)
		fd (89)
		fd(i)
		lt (29)
		for j in range(129):
			fd(i)
			circle(j, 299, steps=2)
		end_fill()
draw()
done()
