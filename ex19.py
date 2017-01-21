def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

def output(string):
	print string


output("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)


output("OR, we can use variables form our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


output("We can enven do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


output("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)