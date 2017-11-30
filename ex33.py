def append_numbers(limit, increment):
    #i = 0
    numbers = []
    
    for i in range(0,limit,increment):
        #print ("At the top i is %d" % i)
        numbers.append(i)
        i += increment      
        #print ("Numbers now: ", numbers)
        #print ("i at the bottom %d" % i)
    return numbers
    
    #while i<limit:
        #print ("At the top i is %d" % i)
        #numbers.append(i)
        #i += increment      
        #print ("Numbers now: ", numbers)
        #print ("i at the bottom %d" % i)
    #return numbers

num = append_numbers(int(input("Enter limit: ")), int(input("Enter increment: ")))
print ("The numbers:")

#num.reverse()

i = 0
while i < len(num):
    print (num[i])
    i += 1
    
num2 = []
num2.extend(range(0,6,3))
print (num2)