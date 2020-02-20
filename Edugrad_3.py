"""QUESTION 3:
Given an array of elements N return the count of odd and even no.s using lambda function

Example -

Input - [2,3,4,5,6,7,8]

Output -(3,4)

Explanation - There are 3 odd no.s and 4 even no.s in the list."""
def main(i):

    x = len(list(filter(lambda x:x%2 == 0,i)))
    y = len(list(filter(lambda y:y%2 != 0,i)))
    return(y,x)