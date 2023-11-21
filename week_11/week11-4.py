#SOIT107_Base_005 
x, y = list(map(int, input().split() ))
#a[0] becomes x
#a[1] becomes y

print( 'Enter two numbers: The remainder is' , x % y)

#SOIT107_Base_006
x, y = list(map(int, input().split() ))

if x==y:
	print( 'Enter two numbers:  It is a square ' , end='')
else:
	print( 'Enter two numbers:  It is not a square ' , end='')