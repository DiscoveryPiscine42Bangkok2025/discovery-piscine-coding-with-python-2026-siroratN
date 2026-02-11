#!/usr/bin/env python3
number_1 = int(input("Enter the first number: \n"))
number_2 = int(input("Enter the second number: \n"))
result = number_1 * number_2
print(number_1, "*", number_2, "=", result)
if number_1 == 0 or number_2 == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is negative.")