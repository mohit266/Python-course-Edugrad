"""
QUESTION 7:
Create a 2-D list from the given input. You will get 2 inputs 1st parameter is the no. of elements in the list and the 2nd parameter is the no. of lists.
 the elements inside the list should start from 0 and end at n-1.



Example -

Input - 8 3

Output - [
    [0,1,2,3,4,5,6,7],
    [0,1,2,3,4,5,6,7],
    [0,1,2,3,4,5,6,7],
    ]
"""
def main(i,j):
    result=[]
    for val in range(j):
        r = []
        for value in range(i):
            r.append(value)
        result.append(r)
    return result