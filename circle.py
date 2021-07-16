import math#importing module math
def Area(rad):  
    result = math.pi*(rad*rad)  #calculating area of the circle with user given radius input 
    print "The area of the circle is: %f"%result
    
while True:
    try:
        rad = input("Enter the radius of the circle:")  #Taking input from User
        print 
        if (isinstance(rad,int) or isinstance(rad,float)):  #Checking if the given input is Integer or Float
            break
        else:
            raise ValueError    #raising Exception if the input number is not Integer or Float
    except ValueError:
        print "The value of the radius should be either in integer or in float"
        print 
Area(rad)   #calling the Area() function
