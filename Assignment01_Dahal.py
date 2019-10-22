# ############################################################################################################# #

## Suchana Dahal, Humboldt-Universität zu Berlin, 19/10/2019                                               #

# ####################################### LOAD REQUIRED LIBRARIES ############################################# #
import time
import os

## import the math packages to square root the numbers
import math

# ####################################### SET TIME-COUNT ###################################################### #
starttime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("Starting process, time: " + starttime)
print("")

## EXERCISE I - FUNCTION (1)
####################################### SQUARE OF A NUMBER  ###########################################################

## defination of function is here

def square(x):
    return x * x

## square() function square its parameter

print(square(1))
print(square(2))
print(square(3))
print(square(4))
print(square(5))

## list of the number were defined.
numbers = [1, 2, 3, 4, 5]

##The map() function applies the square() function on each element of the numbers list. map(aFunction, aSequence)

nums_squared = list(map(square, numbers))

## prints square of the list of the numbers given as a parameter.
print(nums_squared)



## EXERCISE II - FUNCTION (2)
######################################## SQUARE ROOT OF THE NUMBER  ################################################

## for square root of number -- math.sqrt(x); x is the numeric value and it must be greater than 0.


print ("The Square root of 4 = " ,math.sqrt(4))

print ("The Square root of 9 = " ,math.sqrt(9))

print ("The Square root of 16 = " ,math.sqrt(16))

print ("The Square root of 25 = " ,math.sqrt(25))

print ("The Square root of 36 = " ,math.sqrt(36))


### an example for square root of the negative value.

print ("The Square root of -4 = " ,math.sqrt(-4))

## when the value of x is less than 0 or say negative, it produces error. ValueError: math domain error.

# ####################################### END TIME-COUNT AND PRINT TIME STATS################################## #
print("")
endtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("start: " + starttime)
print("end: " + endtime)
print("")