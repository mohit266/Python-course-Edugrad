"""
QUESTION 1:
Swap the case of the string that comes as an input and return the string while making sure that the first letter of the string stays Uppercase.
Example -

Input - "PyThON"

Output - "PYtHon"
"""
def main(i):
    result = ""
    for ch in range(len(i)):
        if ch == 0:
            result += i[ch].upper()
        elif i[ch].islower():
            result += i[ch].upper()
        else:
            result += i[ch].lower()
    return result