import math

def longest_side(a, b):
    """
    Founction to find the length of the longest side of a right triangle.

    :arg a : Side a of the triangle
    :arg b: Side b of the triangle

    :return Length of the longest side c as float

    """

    return math.sqrt(a*a + b*b)
if _name_ == '_main_':
    print(longest_side._doc_)
    print(longest_side(4,5))
    