import random
print(random.randint(5, 20))  # line 1
'''smallest is 5,starting point, and largest is 20,the stopping point'''
print(random.randrange(3, 10, 2))  # line 2
'''smallest is 3 and largest is 9 because the stopping point 10 is exclusive. 
No the line 2 will not output the value 4, due to the interval(AKA steps) of 2 values between all the outputs'''
print(random.uniform(2.5, 5.5))  # line 3
'''
smallest number would be somewhere over 2.50...
largest number would be somewhere over 5.49...(Not sure because I did't see 5.5, but according to documentations,
the ending point may or may not be included due to rounding)
'''

print(random.randint(1, 100))