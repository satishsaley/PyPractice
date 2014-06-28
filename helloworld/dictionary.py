__author__ = 'satish'
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

#Dictionaries can be iterated over, just like a list.
#  However, a dictionary, unlike a list, does not keep
# the order of the values stored in it. To iterate over key value pairs, use the following syntax:

for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)
del phonebook["John"]
phonebook.pop("Jill")

phonebook.update({"Jake": 938273443})
