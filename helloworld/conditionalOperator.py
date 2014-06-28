__author__ = 'satish'
name = "John"
age = 23
if name in ["John", "Rick"]:
    print "Your name is either John or Rick."


if name == "John" and age == 23:
    print "Your name is John, and you are also 23 years old."

if name == "John" or name == "Rick":
    print "Your name is either John or Rick."

#Unlike the double equals operator "==", the "is" operator
#does not match the values of the variables, but the instances themselves.
print (not False) == (False) # Prints out False


# change this code
#Change the variables in the first section, so that each if statement resolves as True.
number = 16
second_number =0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print "1"

if first_array:
    print "2"

if len(second_array) == 2:
    print "3"

if len(first_array) + len(second_array) == 5:
    print "4"

if first_array and first_array[0] == 1:
    print "5"

if not second_number:
    print "6"