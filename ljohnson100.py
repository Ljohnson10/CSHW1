#CS1210 Homework 1, Puzzle 0
#Lucas Johnson
#Section A09

#l = [4, 6, 9, 10, 12, 4, 5, 5] #example list

tuple((((str(min(l))+" ")*(max(l))).split())+(((str(max(l))+" ")*(min(l))).split()))

#makes strings consisting of max(l) and min(l) with trailing spaces, multiplies the min(l) and max(l) strings by
#min(l) and max(l) respectively as integers, using operator overloading.  The strings are split by whitespace and
#combined in a tuple




