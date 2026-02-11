#!/usr/bin/env python3
number = int(input("Enter a number less than 25\n"))
if number > 25:
    print('Error')
else:
    for i in range(number, 25+1):
        print('Inside the loop, my variable is', i)