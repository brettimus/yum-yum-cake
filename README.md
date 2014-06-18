Exercise 5
==========
Given two rectangles (each has a top-left `(x,y)` coordinate and a (width, height)), find the intersecting rectangle, if any.

## The gist
We have four pieces of information that perfectly describe a rectangle (in two dimensions). 
We can break our solution into two parts that handle each dimension separately.

## All the info we need
Given the top-left coordinate `(x,y)` and a description of its width and height, 
we have a rectangle whose vertices are described (clock-wise) by the set
`{(x,y),(x+w,y),(x+w,y-h),(x,y-h)}`

## Intersecting intervals
If the rectangles intersect, 
we would expect their respective x-intervals to overlap non-trivially.

Of course, same goes for their y-intervals.

### For the top-left `x` coords

### For the top-left `y` coords

## Runtime and Space Complexity
We have a fixed input in this case so meh. 

***

| TODO     | Description   |
|----------|:-------------:|
| Clean-up | Could be written to be a little easier on the eyes, methinks |
| Visuals  | To illustrate idea of intersecting intervals                 |

