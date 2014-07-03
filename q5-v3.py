# InterviewCake (Beta Exercise 5)
# Brett Beutell
# June 17, 2014

# Define rectangles as hashes
# r = {"x" : x, "y" : y, "width" : w, "height" : h}

def find_r_int(r1,r2):
	result = {}
	left_rect, right_rect = (r1,r2) if r1["x"] <= r2["x"] else (r2,r1)
	if left_rect["x"] + left_rect["width"] < right_rect["x"]:
		return None
	result["x"] = right_rect["x"]
	result["width"] = min(left_rect["x"] + left_rect["width"] - right_rect["x"],\
							right_rect["width"])

	lower, higher = (r1,r2) if r1["y"] <= r2["y"] else (r2,r1)
	if higher["y"] - higher["height"] >= lower["y"]:
		return None
	result["y"] = lower["y"]
	result["width"] = min(lower["height"], lower["y"] - (higher["y"] - higher["height"]))

	return result
