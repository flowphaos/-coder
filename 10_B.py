n=int(raw_input())
i = map(int, raw_input().split())
z = 0
for x in i:
	if x % 2 == 0 or x % 3 == 2:
		z+=1
	elif x % 2 == 0 and x % 3 == 2:
		z+=2

print z

