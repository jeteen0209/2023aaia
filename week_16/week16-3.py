# SOIT107_ADVANCE_006
a = input()
N = len(a)
for i in range(N):
	if a[i] != '2':
		print(a[i], end='')
print()


# SOIT107_ADVANCE_010
a = input()
N = len(a)
bad = 0
for i in range(N):
	if a[i] != a[N-1-i]:
		bad = 1 
if bad==0: print('YES',end='')
else: print('NO', end='')