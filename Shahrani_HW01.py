"""
    Abdulellah Shahrani's solution to HW01 on Jan 28
    with the unittests to test the function

"""

import unittest


def classify_triangle(a, b, c):
    """
        a function classify_triangle() that takes three  parameters: a, b, and c.
        The three parameters represent the lengths of the sides of a triangle.
        The function returns a string that specifies whether the triangle is scalene,
        isosceles, or equilateral, and whether it is a right triangle as well.
    """

    if a + b > c and a + c > b and b + c > a:
        if a > 0 and b > 0 and c > 0:

            if a == b == c:
                return "Equilateral"

            elif a == b or a == c or b == c:
                return "Isosceles"

            elif a * a + b * b == c * c:
                return "Right"

            else:
                return "Scalene"

        else:
            return "Not a triangle"

    else:
        return "Not a triangle"


class TriangleTests(unittest.TestCase):
    def test_triangle(self):
        """ test case to test the triangle function """
        self.assertNotEqual(classify_triangle(3, 3, 4), "Right")
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(2, 4, 5), "Scalene")
        self.assertEqual(classify_triangle(4, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
        self.assertNotEqual(classify_triangle(2, 3, 4), "Equilateral")
        self.assertEqual(classify_triangle(1, 2, 6), "Not a triangle")
        self.assertEqual(classify_triangle(2, 0, 1), "Not a triangle")


def main():
    a = input("Please enter the first parameter of the triangle, or Q to exit: ")
    b = input("Please enter the second parameter of the triangle, or Q to exit: ")
    c = input("Please enter the third parameter of the triangle, or Q to exit: ")

    if a == "Q" or a == "q" or b == "Q" or b == "q" or c == "Q" or c == "q":
        exit()
    else:
        try:
            """ transforming the inputs to integers """
            aa = int(a)
            bb = int(b)
            cc = int(c)

        except ValueError:
            print("One of the parameters have invalid input")
            exit()

    print(f"The triangle is ", classify_triangle(aa, bb, cc))

    unittest.main()


if __name__ == '__main__':
    main()
