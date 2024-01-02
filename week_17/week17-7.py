# SOIT108_Base_008
a = int(input())

print( int(1.2*60*60/a) , end=''


# SOIT108_Advance_010
a = input()
N = len(a)
for i in range(N):
	if i!=0 and (N-i)%3==0:
		print(',' , end='')
	print(a[i] , end='')
    
    
# SOIT108_Advance_012
k = int(input())
total = 0 
for i in range(1, 1001):
	total += i
	if total>k:
		ans = i 
		break
print(ans, end='')