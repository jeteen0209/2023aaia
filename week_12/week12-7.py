A 

a = int(input())

ans = 0
for i in range(1,a+1):
	ans += i*i
	
print(ans, end='')

B 

a, b = list(map(int, input().split() ))

ans = 0
for i in range(a, b+1):
	if i%3==0: ans +=i
	
print(ans, end='')