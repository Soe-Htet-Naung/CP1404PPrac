"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    '''ValueError will occur when the user inputs values other than integers'''
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    '''Zero division error will occur when user inputs the value 0 as denominator'''
    print("Cannot divide by zero!")
print("Finished.")