from fractions import Fraction # https://docs.python.org/3/library/fractions.html?highlight=fractions#module-fractions

# The fractions module provides support for rational number arithmetic.
# A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.

print(Fraction(16, -10))
print(Fraction(123))
print(Fraction())
print(Fraction('3/7'))
print(Fraction(' -3/7 '))
print(Fraction('1.414213 \t\n'))
print(Fraction('-.125'))
print(Fraction('7e-6'))
print(Fraction(2.25))
print(Fraction(1.4))

# numerator = Numerator of the Fraction in lowest term.
print(Fraction(16, -10).numerator)
# denominator = Denominator of the Fraction in lowest term.
print(Fraction(123).denominator)

# Return a tuple of two integers, whose ratio is equal to the Fraction and with a positive denominator.
print(Fraction().as_integer_ratio())

