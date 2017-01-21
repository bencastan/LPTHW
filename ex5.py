my_name = 'Ben castan'
my_age = 55 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
my_height_in_cm = my_height * 2.54 # 1 inch = 2.54 cm's
my_weight_in_kg = my_weight * 0.453591 # 1 lb = 0.453591 cm's

print "Lets talk about %s." % my_name
print "He's %d inchaes tall." % my_height
print "In cm that is %d cm." % my_height_in_cm
print "He's %d poundes heavy." % my_weight
print "In kg's that is %d kg." % my_weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it right
print "If I add %d, %d,and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)