#SOIT106_BASE_003
a = list(map(int, input().split() ))

print( sum(a)- a[0] )


#SOIT106_BASE_004
a = int(input())
if a<=2000: ans = 100
else:
	ans = 100+(a-2000)//500*5
	if (a-2000)%500>0: ans += 5
print(ans)