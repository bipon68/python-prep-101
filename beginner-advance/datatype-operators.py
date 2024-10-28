####################################################
## 1. Primitive Datatypes and Operators
####################################################
# Math is what you would expect
print(1+1)
print(8-1)
print(10*2)
print(35/5)
print("Math is what you would expect")

# Floor division rounds towards negative infinity
print(5//3)
print(-5//3)
print(5.0//3.0)
print(-5.0//3.0)
print("End of Floor division")

# The result of division is always a float
print(10.0/3)
print("End of The result of division is always a float")

# Modulo operation
print(7%3)
print("End of Modulo operation")

# Exponentiation (x**y, x to the yth power)
print(2**3)
print("End of Exponentiation")

# Enforce precedence with parentheses
print(1 + 3*2)
print((1 + 3) * 2)
print("End of Enforce precedence with parentheses")

# Boolean values are primitives (Note: the capitalization)
print(True)
print(False)
print("End Boolean values")

# negate with not
print(not True)
print(not False)
print("End negate with not")

# Boolean Operators
# Note "and" and "or" are case-sensitive
print(True and False)
print(False or True)
print("End Boolean Operators")

# True and False are actually 1 and 0 but with different keywords
print(True + True)
print(True * 8)
print(False - 5)
print("End True and False are actually 1 and 0 but with different keywords")

# Comparison operators look at the numerical value of True and False
print(0 == True)
print(2 > True)
print(2 == True)
print(-5 != False)
print("Comparison operators look at the numerical value of True and False")

# Strings can be added too
print("Hello " + " World")
# String literals (but not variables) can be concatenated without using '+'
print("Hello " "Man")

# A string can be treated like a list of characters
print("Hello World"[0] )

# You can find the length of a string
print(len("This is a string"))

# None is an object
print(None)


# single line comment
# print("Hello man")
# multiline comment
'''multiline comment
print(23)
 declare a variable'''
name = "Bipon"
# print name
print(name)

# Prevent Executing Code Using Comments
num1 = 10
num2 = 20
sum = num1 + num2
print("The sum is :", sum)
#print("The product is : ", product)
