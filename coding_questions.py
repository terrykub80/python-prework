def gap():
	"""Creates space between answers"""
	print("\n-----------------------\n")
	
user_name = 'terrykub'


def hello_name(user_name):
	"""Prints "hello_USERNAME!" """
	print("hello_" + user_name.upper() + "!")

print("Answer 1:")
hello_name(user_name)

gap()
print("Answer 2:")

def first_odds():
	"""Prints odd number from 1-100 but returns nothing"""
	number = 0
	while number < 100:
		number += 1
		if number % 2 == 1:
			continue
		else:
			continue
		print(number)
	

first_odds()

gap()
print("Answer 3:")

a_list= list(range(0, 5000))

def max_num_in_list(a_list):
	"""Returns the max number of a given list"""
	print(max(a_list))

max_num_in_list(a_list)

gap()
print("Answer 4:")

a_year = input("Type in any year and I'll let you know if it's a leap year: ")

def is_leap_year(a_year):
	"""Returns if a given year is a leap year"""	
	if int(a_year) % 4 == 0 and int(a_year) % 100 != 0 or int(a_year) % 400 == 0:
		print(str(a_year) + " is a leap year!")
	else:
		print(str(a_year) + " is not a leap year!")
	
is_leap_year(a_year)
	
gap()
print("Answer 5:")
print("(to really see this code in action please enter a list of numbers into 'a_list = []' before running it)\n")

a_list = [1,99,2,3]

def is_consecutive(a_list):
	"""Returns whether a numerical list is in consecutive order."""
	if a_list != sorted(a_list):
		print(str(a_list) + "\nThis list is not in consecutive order!")
	else:
		print(str(a_list) + "\nThis list is in consecutive order!")
		
is_consecutive(a_list)
		
	

	

	

