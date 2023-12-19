#SOIT108_Base_011
a,b,c,d = list(map(int, input().split() ))

ans = (a-c) * (b-d)
if ans<0: ans = -ans
print(ans, end='')

#SOIT108_Base_010
a,b = list(map(int, input().split() ))

ans = a//b
if a%b>0: ans += 1

print(ans, end='')

#SOIT108_Base_007
a = list(map(int, input().split() ))
for i in range(10-1, -1, -1):
	print(a[i], end=' ')
    
#SOIT108_Base_004
a,b = list(map(int, input().split() ))
if a>0 and b>0: ans = 1 
if a<0 and b>0: ans = 2
if a<0 and b<0: ans = 3
if a>0 and b<0: ans = 4
print(ans)