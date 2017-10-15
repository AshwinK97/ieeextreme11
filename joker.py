n = int(input())
htable = {}
for i in range(0, n):
    member, height = raw_input().split()
    if height in htable:
        htable[height].append(member)
    else:
        htable[height] = [member]

# sort dictionary by height
hsorted = []
for key in sorted(htable.iterkeys()):
    htable[key].sort()
    hsorted.append([key, htable[key]])

start = 1
end = 1
for height in hsorted:
    end = start + len(height[1]) - 1 
    print ' '.join(height[1]) + ' ' + str(start) + ' ' + str(end)
    start = end + 1
