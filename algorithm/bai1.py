import re
import sys

input = '123456789'
def  checkSolution(arr):
    s = ''
    for i in range(8):
        s += input[i] + arr[i]
    s += '9'
    if(eval(s) == 100):
        print('{} = {}'.format(s, eval(s)))
    return 

# Function to generate all binary strings 
def generateAllBinaryStrings(n, arr, i): 

	if i == n: 
		checkSolution(arr)
		return
	

	arr[i] = '+'
	generateAllBinaryStrings(n, arr, i + 1) 

	arr[i] = '-'
	generateAllBinaryStrings(n, arr, i + 1) 
    
	arr[i] = ''
	generateAllBinaryStrings(n, arr, i + 1) 

# Driver Code 
if __name__ == "__main__": 
    
	n = 8
	arr = [None] * n 

	# Print all binary strings 
	generateAllBinaryStrings(n, arr, 0) 