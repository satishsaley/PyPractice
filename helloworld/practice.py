import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    #print(test)
    data = test
    if data=="\n":
        break
    #print(data)
    #input_data= [0 for listofrow in range(len(data))]
    for i in range(0, len(data)):
        input_data = (data.rsplit(" "))
        #print(input_data)
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    for k in range(1, c+1):
        if k % a == 0 and k % b == 0:
            print("FB", end=" ")
        elif (k % a == 0):
            print("F", end=" ")
        elif k % b == 0:
            print("B", end=" ")
        else:
            print("%d" %k, end=" ")
        #'''
    print()
        
test_cases.close()

#data = sys.stdin.readlines()


