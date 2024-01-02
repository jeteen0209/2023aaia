# SOIT107_ADVANCE_011
a = input()
ans = 0
for c in a:
	if c>='0' and c<='9':
		ans += 1
print(ans)

# SOIT107_ADVANCE_012
a = int(input())

for i in range(a):
	space = a-1 - i
	for k in range(space):
		print(' ', end='')
		
	star = i*2 + 1
	for k in range(star):
		print('*', end='')
	print()