"""
DESCRIPTION:
_________

Implement a function called is_valid_parity. It accepts two strings called codeword
and parity.

The is_valid_parity function returns True if codeword is parity-encoded correctly. If it
is not, the function returns False.

A parity-encoded codeword is a series of binary digits (zeros and ones) where the
left-most digit is actually an extra digit that has been prepended to some original
number. The left-most digit we prepend is either a zero or one depending on the type
of parity being used (EVEN or ODD).

If a word is encoded with EVEN parity the total number of 1 bits in the codeword
must be an even number.

If a word is encoded with ODD parity the total number of 1 bits in the codeword
must be an odd number.

For example if the original word is 1001:

   an EVEN codeword is 01001 (The original number 1001 contains two 1s, 1 + 1 = 2
   which is even, so we prepend a 0 to the original 1001 to keep the total number
   of 1s even)

   an ODD codeword is 11001 (The original number 1001 contains two 1s, 1 + 1 = 2
   which is even, so we prepend a 1 to the original 1001 to keep the total number
   of 1s odd)

Your function must accept a string codeword (the original value with the parity bit
prepended to it) and a parity (EVEN or ODD) as parameters and return True if the
codeword has been correctly parity-encoded, else False.

ASSUMPTIONS:
____________

Your function only promises to work if the first string is a possibly empty string
that contains nothing but 0s and 1s, i.e.,"" or "0" or "10101010101111000", etc.

Your function only promises to work if the second string is "EVEN" or "ODD".

EXAMPLES:
_________

is_valid_parity("101", "EVEN") returns True
is_valid_parity("101", "ODD") returns False
is_valid_parity("11", "EVEN") returns True
is_valid_parity("11", "ODD") returns False
is_valid_parity("111111111100000000001010110101", "EVEN") returns True
is_valid_parity("111111111100000000001010110101", "ODD") returns False
is_valid_parity("11111111111000011111000001010110101", "EVEN") returns True
is_valid_parity("11111111111000011111000001010110101", "ODD") returns False
is_valid_parity("10", "ODD") returns True
is_valid_parity("10", "EVEN") returns False
is_valid_parity("111", "ODD") returns True
is_valid_parity("111", "EVEN") returns False
is_valid_parity("11", "ODD") returns False
is_valid_parity("11", "EVEN") returns True

DOCSTRING:
__________

Yes. Full docstrings are needed. Include pre- and post-conditions. Be precise.

DOCTESTS:
_________

Provide THREE (3) useful and different doctests that show me how is_valid_parity works.

UNI TESTS:
__________

Provide a suite of unit tests. Identify the disjointed equivalence partitions, and
create the correct number of nicely-named unit tests. Don't create too many!

GRADING:
________

(2) for implementation (don't forget the main function and the if-statement at
    the bottom of the file!)
(1) for docstring
(1) for doctests
(1) for unit tests
(-5) if not submitted to the cloud before the end of the exam.
"""
