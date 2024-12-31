import math
import os
import random
import re
import sys

def fizzBuzz(n):
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
