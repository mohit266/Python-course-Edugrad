"""
QUESTION 8:
You will get a number in input you have to get all the prime no.s till that no


Example -


Input - 10


Output -[2,3,5,7]
"""

def main(i):
    ls = []
    for val in range(1, i+1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                ls.append(val)
    return ls