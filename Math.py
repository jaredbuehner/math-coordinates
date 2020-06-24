# Imports.
import math

# Start prompt.
print('\n**** Welcome to the math application! ****\n')

print('Enter a number between -2\u03C0 and 2\u03C0',
    'in increments of \u03C0/64: ')
userInput = int(input())
# Holds user's selection in memory.
x = userInput

print('\nEnter a number between 0 and 200',
    'in increments of 0.5: ')
userInput2 = int(input())
# Holds user's selection in memory.
x2 = userInput2

# Trig functions.
def sin():
    y = math.sin(x)
    print('(' + str(x) + ', ' + str(y) + ')')
def cos():
    y = math.cos(x)
    print('(' + str(x) + ', ' + str(y) + ')')

# Algebraic functions.
def sqrt():
    y = math.sqrt(x2)
    print('(' + str(x2) + ', ' + str(y) + ')')
def log10():
    y = math.log10(x2)
    print('(' + str(x2) + ', ' + str(y) + ')')

# Outputs results to the standard I/O.
print("(x, sin(x)) ="), sin()
print("\n(x, cos(x)) ="), cos()
print("\n(x, sqrt(x)) ="), sqrt()
print("\n(x, log10(x)) ="), log10()

# Exit prompt.
print('\n**** Thanks for trying the math application! ****\n')
