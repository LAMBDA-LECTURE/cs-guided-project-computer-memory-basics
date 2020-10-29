"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""
def hamming_weight(n):
    # Your code here
    # solution one
    #  if were given an unsigned int, convert it to bitwise representation
    # logical operators: `&&`, `||`
    # vs bitwise logical operators: `&`, `\`
        # `&` will compare if the last spots (in bitwise notation) matches
        #ie: its a way to check the rightmost bit of n, to see if it's 1.
    #other bitwise: the left and right shift operations
        # << or >>
        # >> lets  us "move" the bitwise digits ober one spot to the right
    #if `&` on the rightmost returns a 1, increase a counter
    # >> by 1 bitwise digit
    counter = 0
    # when do we stop right shifing
    while n != 0:
        if n & 1 == 1:
            counter += 1
        n = n >> 1
    return counter
        # well, everytime we shift, it adds a zero at the first point, and eventually the decimal number will be zero

    # solution 2
    counter = 0
    bin_representation = bin(n)
    for i in range(length(bin_representation)):
        if bin_representation[i] == "1":
            counter += 1
    return counter

    # solution 3
    return bin(n).count('1')