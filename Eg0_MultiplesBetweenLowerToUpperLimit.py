'''
Can you  assign a function to set multiples (denominators)
of a number where the user enters the number
whose multiples are to be calculated and enters the upper limit
number (the largest possible number)
And the function calculates all the multiples
of the lower number that are smaller or equal to the upper limit
'''

def mul(lower_limit,upper_limit):
	mul_list = []
	for i in range(1,upper_limit):
		temp = lower_limit*i
		if(temp<=upper_limit):
			mul_list.append(temp)
	return mul_list

lower_limit = int(input("Enter the Lower limit"))
upper_limit = int(input("Enter the Upper limit"))
print("Multiples of lower number that are smaller or equal to \n the upper limit is \n",mul(lower_limit,upper_limit))
