def sumOfDigitsFrom1ToN(n) : 

	result = 0 
	
	for x in range(1, n+1) : 
		result = result + sumOfDigits(x) 

	return result 
 
def sumOfDigits(x) : 
	sum = 0
	while (x != 0) : 
		sum = sum + x % 10
		x = x // 10
	
	return sum

n = 328
print("Sum of digits in numbers from 1 to", n, "is", sumOfDigitsFrom1ToN(n)) 

 
