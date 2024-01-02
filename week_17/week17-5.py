# SOIT106_BASE_007
a, b = list(map(int, input().split() ))
print( a//b )


# SOIT106_BASE_008
a, b = list(map(int, input().split() ))
if a>b:
	a, b = b, a
for i in range(a, b+1):
	if i%5==0: print(i)
    

# SOIT106_BASE_009
a = list(map(int, input().split() ))
print( max(a) - min(a) )


# SOIT106_BASE_010
a = list(map(int, input().split() ))
ans = 0 
for b in a:
	if b%3==0: ans += 1
print( ans )