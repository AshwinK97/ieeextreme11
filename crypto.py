import math

def getdistance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def measure(r, d, s):
	s = ''.join(e for e in s if e.isalnum()) # remove punctuation
	s = ''.join([i for i in s if not i.isdigit()]) # remove digits
	length = 0.0
	prevx, prevy = 0, 0

	for i, c in enumerate(s):
		angle = d[c] # get angle for letter
		x = r * math.cos(math.radians(angle)) # get x distance
		y = r * math.sin(math.radians(angle)) # get y distance
		length += getdistance(x, y, prevx, prevy) # get magnitude
		prevx, prevy = x, y

	return int(math.ceil(length))

r = int(input()) # distance from any letter to center
d = {} # contains each letter's angle from the x-axis
for i in range(0, 26):
	line = raw_input().split()
	d[line[0]] = float(line[1]) # ex) 'A': 168.05

print measure(r, d, raw_input().upper())