"""QUESTION 6:
Given an string input find all the no.s in the string using regular expression. If there are more than one no. present return a list containing all the no.s

Example -

Input - "There are 12 dogs and 7 cats in the house."

Output - ['12','7']"""

import re
def main(i):
    result = re.findall(r'[0-9]+', i)
    return result