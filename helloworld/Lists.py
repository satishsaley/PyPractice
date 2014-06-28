__author__ = 'satish'
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#Python also supports multiplying strings to form a string with a repeating sequence:
number = 7 ** 2 ** 2
print "number is %s" % (number * "hi ")

