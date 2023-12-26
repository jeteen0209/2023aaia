# SOIT107_ADVANCE_014
N = int(input())
ans = 0 

for i in range(1, N+1):
	if i%2==1: ans += i
	
print(ans, end='')


# SOIT107_ADVANCE_015
a , b = list(map(int, input().split() ))

for i in range(a, b+1):
	if i%7==0:
		print(i, end=' ')

        
# SOIT107_ADVANCE_016
a = list(map(int, input().split() ))
N = len(a)
print(N-1, end='')