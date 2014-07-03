# InterviewCake (Beta Exercise 5)
# Brett Beutell
# June 17, 2014

# Let top_left be a 2-tuple
# E.g., top_left = (x,y)

# Define rectangles as hashes
# r = {"top_left" : {"x" : x, "y" : y}, "width" : w, "height" : h}

def find_x_intersect(x1,w1,x2,w2):
	""" 
		Finds intersection along x-axis
		Returns tuple of 
			(leftmost intersecting x-coord, width of intersection)
	"""
	# Case 1: left x-coord of the first rectangle lies in the second rectangle's x-interval
	if (x2 <= x1) and (x1 < x2+w2):
		result_x = x1
		result_w = min(x2-(x1-w2), w1)
	# Case 2: left x-coord of the second rectangle lies in the first rectangle's x-interval
	elif (x1 <= x2) and (x2 < x1+w1):
		result_x = x2
		result_w = min(x1-(x2-w1), w2)
	# Case 3: No intersection- we've got a dud
	else:
		result_x, result_w = None, None

	return (result_x, result_w)

def find_y_intersect(y1,h1,y2,h2):
	""" 
		Finds intersection along y-axis
		Returns tuple of
			(topmost intersecting y-coord, height of intersection)
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
		result_y, result_h = None, None

	return (result_y, result_h)

def find_intersect(r1,r2):
	"""
		Returns a dict with fields
			top_left
			width
			height
	"""
	result = {}
	x1, x2 = r1["x"], r2["x"]

	result["x"], result["width"] = \
		 						find_x_intersect(r1["x"],r1["width"], r2["x"],r2["width"])

	y1, y2 = r1["top_left"]["y"], r2["top_left"]["y"]
	result["y"], result["height"] = \
								find_y_intersect(r1["y"], r1["height"], r2["y"], r2["height"])
	return result

