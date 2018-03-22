from mymath import raise_to_the_power


def area_of_square(length):
    """Finds area of square."""
    assert type(length) == int or type(length) == float
    return raise_to_the_power(length, 2)