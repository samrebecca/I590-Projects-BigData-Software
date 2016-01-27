n=int(input("Some integer please: "))
def fizzbuzz(n):
    for x in range(1, n):
        if (x%2) == 0 and (x%3) !=0:
            print ("fizz")
	elif (x%2) !=0 and (x%3) ==0: 
	    print ("buzz")
	elif (x%2 ==0) and (x%3) ==0: 
	    print ("fizzbuzz")
	else :
	    print (x)   		

fizzbuzz(n)

