#CS1210 Homework 1, puzzle 1
#Lucas Johnson
#Section A09

#l=[1,4,5,3,2] Example list

centerIndex=int((len(l)-1)/2) #gets the index of the center integer, taking length-1 works for odds and evens due to int division
z=list(str('0')*l[centerIndex]) #makes a list of zeroes, number of zeroes is the middle integer
l.pop(centerIndex) #pops the middle integer from the list
l=l[:centerIndex]+z+l[centerIndex:] #puts the zeroes where the removed integer was

