def dist(start, end):

	# if start and end are same
	if start == end:
		return 0

	distance = 1

	# walk from start to 1
	while True:
		# if start and end are same
		if start == end:
			distance-=1
			break

		# if they are 2 and 3
		if (start == 2 and end == 3) or (start == 2 and end == 3):
			distance+=1
			break

		# if they share the same parent node
		if start/2 == end/2:
			distance+=1
			break

		# if start is higher, you move start
		if start > end:
			if start % 2 == 0:
				start = start / 2
			else:
				start = (start - 1) / 2

		# if end is higher, you move end
		else:
			if end % 2 == 0:
				end = end / 2
			else:
				end = (end - 1) / 2

		# increment distance	
		distance+=1
	return distance

qs = int(input())
for q in range(0, qs):
	start, end = map(int, raw_input().split())
	print dist(start, end)