# 8.5 Recursive Multiply: 
# Write a recursive function to multiply two positive integers without using the * operator (or / operator). 
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

# iterative solution
def multiply(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return 0
    
    while b > 1:
        if b & 1: # is odd
            b = b//2
            a = (a << 1) + (a >> 1)
        else: # is even
            b = b//2
            a = a << 1
    return a

# recursive solution
def multiply(a, b):
    if b == 0:
        return 0
        
    if b == 1:
        return a
    
    if b & 1: # is odd
        b = b//2
        a = (a << 1) + (a >> 1)
    else: # is even
        b = b//2
        a = a << 1
    
    return multiple(a, b)
