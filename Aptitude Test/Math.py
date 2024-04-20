"""
Math.py

This program tests the methods of the basic math operations
package I created.

Usage:
- Testing my package for basic math operations.

@author: Aryan Bansal
@date: 25th April 2024
@version: 1.0
"""

from basic_math_operations import *

if __name__ == "__main__":
    result_add = add(5, 3)
    result_subtract = subtract(5, 3)
    result_multiply = multiply(5, 3)
    result_divide = divide(5, 3)
    result_pow = pow(5, 3)
    result_int_divide = intDivide(5, 3)
    result_left_shift = leftShift(5, 3)
    result_right_shift = rightShift(5, 3)

    print(result_add)           # Output: 8
    print(result_subtract)      # Output: 2
    print(result_multiply)      # Output: 15
    print(result_divide)        # Output: 1.67
    print(result_pow)           # Output: 125
    print(result_int_divide)    # Output: 1
    print(result_left_shift)    # Output: 40
    print(result_right_shift)   # Output: 0