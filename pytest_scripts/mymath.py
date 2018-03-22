from __future__ import division

def add(num1, num2):
    assert type(num1) == int or type(num1) == float
    assert type(num2) == int or type(num2) == float
    return num1 + num2

def divide(numerator, denominator):
    return numerator / denominator


def multiply(num1, num2):
    assert type(num1) == int or type(num1) == float
    assert type(num2) == int or type(num2) == float
    return num1 * num2

def raise_to_the_power(num, power):
    assert type(num) == int or type(num) == float
    assert type(power) == int or type(power) == float
    return num ** power
