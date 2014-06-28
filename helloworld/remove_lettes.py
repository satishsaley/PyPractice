##Write a program to remove specific characters from a string.
##Input sample:
##
##The first argument will be a path 
##to a filename containing an input string followed by a comma and then the 
##characters that need to be scrubbed. E.g.
##
##how are you, abc
##hello world, def
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    input_data = (test.rsplit(", "))
    list_word = list(input_data[1])
    for word in list_word:
        input_data[0]=input_data[0].replace(word,"")
    print(input_data[0])
