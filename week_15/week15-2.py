(SOIT107_ADVANCE_002) 
a = list(map(int, input().split() ))

print( max(a) - min(a) , end='' )


(SOIT107_ADVANCE_003) 
ans = 0 

while True:
	a = int(input('Enter an integer ( 999 to end ): \n' ))
	a = int(a)
	if a == 999:
		break
	ans += a
	
print('The total is:', ans, end='')