"""QUESTION 2:
You will get a list in input consisting of only tuple elements. Each tuple will have 2 numeric elements. You have to return the maximum difference between the tuple pairs

Example -

Input - [(10,12),(8,15),(20,8),(2,-10)]

Output - 12

Reason - The difference between all the tuple pairs are 2,7,12,12 respectively and max of them is 12.

"""


def main(i):
    ls = []
    for value in i:
        result = value[0] - value[1]
        if result >= 0:
            ls.append(result)
        else:
            ls.append(-1 * result)

    result = ls[0]
    for val in ls:
        if result < val:
            result = val
    return result