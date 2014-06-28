__author__ = 'satish'
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]

#Using a list comprehension, create a new list called
# "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(n) for n in numbers if n > 0]

print newlist