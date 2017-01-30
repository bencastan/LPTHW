#ex33.py
i = 0
incrementor = 8
numbers = []

def my_numbers(number, incremnter):
	i = 0
	numbers = []
	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + incremnter
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers



	


numbers = my_numbers(160, incrementor)
	


print "The numbers: "

for num in numbers:
	print num