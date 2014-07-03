# InterviewCake (Beta Exercise 5)
# Brett Beutell
# June 17, 2014

import sys

# Let top_left be a 2-tuple
# E.g., top_left = (x,y)

# Create a rectangle class containing the top_left x and y coordinates, width, and height
class Rectangle:
	def __init__(self, top_left=(sys.maxint,-sys.maxint - 1), width=0, height=0):
		self.x, self.y = top_left
		self.width = width
		self.height = height

	def __str__(self):
		return "[Top-left: (%d,%d), Width: %d, Height: %d]" % \
							(self.x, self.y, self.width, self.height)

def find_x_intersection(x1,w1,x2,w2):
	""" 
		Finds intersection along x-axis
		Returns tuple containing 
			[] top-left x-coord and 
			[] width 
		for intersecting rectangle
	"""
	# Case 1: left x-coord of the FIRST rectangle lies in the second rectangle's x-interval
	if (x2 <= x1) and (x1 < x2+w2):
		result_x = x1
		result_w = min(x2+w2-x1, w1)
	# Case 2: left x-coord of the SECOND rectangle lies in the first rectangle's x-interval
	elif (x1 <= x2) and (x2 < x1+w1):
		result_x = x2
		result_w = min(x1+w1-x2, w2)
	# Case 3: No intersection- we've got a dud
	else:
		result_x = sys.maxint
		result_w = 0
	return (result_x, result_w)

def find_y_intersection(y1,h1,y2,h2):
	""" 
		Finds intersection along y-axis
		Returns tuple containing 
			[] top-left y-coord and 
			[] height 
		for intersecting rectangle
	"""
	# Case 1: top y-coord of the FIRST rectangle lies in second rectangle's y-interval
	if (y1 <= y2) and (y2-h2 < y1):
		result_y = y1
		result_h = min(y1 - (y2-h2), h1)
	# Case 2: top y-coord of the SECOND rectangle lies in first rectangle's y-interval		
	elif (y2 <= y1) and (y1-h1 < y2):
		result_y = y2
		result_h = min(y2-(y1-h1), h2)
	# Case 3: No intersection
	else:
		result_y = -sys.maxint - 1
		result_h = 0
	return (result_y, result_h)

def find_intersection(rect_1,rect_2):
	# Find intersection along the x-axis
	x, width = find_x_intersection(rect_1.x,rect_1.width,\
												 rect_2.x,rect_2.width)
	# Find intersection along the y-axis
	y, height = find_y_intersection(rect_1.y, rect_1.height,\
												  rect_2.y, rect_2.height)
	return Rectangle((x,y),width,height)

def test_1():
	r1 = Rectangle((1,1),2,2)
	print("Rectangle 1", r1)
	r2 = Rectangle((1,1),1,1)
	print("Rectangle 2", r2)
	r3 = find_intersection(r1,r2)
	print("Rectangle 3", r3)

test_1()
