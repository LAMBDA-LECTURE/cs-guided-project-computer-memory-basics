"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    output = ""
    for letter in string:
        ord_letter = ord(letter)
        if ord_letter < 90: # if it's capital
            output += chr(ord_letter + 32)
        else:
            output += chr(ord_letter)
    print(output)



to_lower_case("alTESTpabet")
# to_lower_case("A")
# to_lower_case("b")
# to_lower_case("B")