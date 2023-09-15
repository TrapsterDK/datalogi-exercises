from typing import Any
from contextlib import suppress

def sum_up_to(n: int) -> int:
    """Calculate the sum up to and including n.
    Pre-condition: n is a natural number.
    >>> sum_up_to(4)
    10
    """
    if n == 0:
        return 0
    else:
        return n+sum_up_to(n-1)


def sum_even(n: int) -> int:
    """Calculate the sum of even numbers up to and including n.
    Pre-condition: n is a natural number.
    >>> sum_even(7)
    12
    >>> sum_even(4)
    6
    """
    n -= n%2
    if n == 0:
        return 0
    else:
        return sum_even(n-2) + n


def sum_between(m: int, n: int) -> int:
    """Calculate the sum between m and n includig m and n.
    >>> sum_between(-2, 4)
    7
    >>> sum_between(3, 5)
    12
    """
    if m == n:
        return n
    else:
        return m + sum_between(m+1, n)


def factorial(n: int) -> int:
    """Calculate the factorial of a number.
    Pre-condition n is a natural number.
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def double_factorial(n: int) -> int:
    """Calculate the double factorial of a number.
    Pre-condition n is a natural number.
    >>> double_factorial(5)
    15
    >>> double_factorial(4)
    8
    """
    if n <= 0:
        return 1
    else:
        return n * double_factorial(n-2)


def logarithm(n: int) -> int:
    """Calculate the base 2 logarithm as an floored int for a number.
    >>> logarithm(8)
    3
    >>> logarithm(7)
    2
    """
    if n <= 1:
        return 0
    else:
        return 1 + logarithm(n//2)
    

def gcd(m: int, n: int) -> int:
    """Calculate greatest common divisor for two numbers.
    >>> gcd(6, 4)
    2
    """
    if m == n:
        return m
    elif m < n:
        return gcd(m, n - m)
    else:
        return gcd(m - n, n)


def lcm(m: int, n: int) -> int:
    """Calculate least common divisor for two numbers.
    >>> lcm(6, 4)
    12
    """
    return m * n // gcd(m, n)


def first_digit(n: int, k: int = 10) -> int:
    """Calculate first digit of n in k base representation,
    where n is in base 10 representation.
    >>> first_digit(12, 3)
    1
    >>> first_digit(98)
    9
    """
    if n < k:
        return n
    else:
        return first_digit(n//k, k)


def print_multiples(k: int, n: int, _progress: int = 0) -> None:
    """Print the multiples of k that are less than n not including n.
    Pre-condition k and n are natural numbers.
    >>> print_multiples(7, 28)
    7
    14
    21
    """
    progress = _progress + k
    if progress < n:
        print(progress)
        print_multiples(k, n, progress)
        
    return None


def count_divisors(n: int, _divisor: int = 1) -> int:
    """Calculate number of divisors n has.
    Pre-condition n is a natural number.
    >>> count_divisors(12)
    6
    >>> count_divisors(0)
    0
    """
    if _divisor > n: # happens if 0 is used as n
        return 0
    elif _divisor == n:
        return 1
    else:
        return int(n % _divisor == 0) + count_divisors(n, _divisor + 1)


def is_perfect(n: int) -> bool:
    """Calculate if an integer n is perfect.
    Pre-condition n is a natural number.
    >>> is_perfect(6)
    True
    >>> is_perfect(8)
    False
    """
    def divisor_sum(m: int, _divisor: int = 1) -> int:
        """Calculate the sum of all divisors for a given number excluding m.
        >>>divisor_sum(8)
        7
        """
        if _divisor == m:
            return 0
        else:
            a = divisor_sum(m, _divisor + 1)
            if m % _divisor == 0:
                a += _divisor
            return a

    return divisor_sum(n) == n
        

def count_perfect(n: int) -> int:
    """Calculate the number of perfect numbers smaller than n including n.
    Pre-condition n is a natural number.
    Tests from https://en.wikipedia.org/wiki/Perfect_number.
    >>> count_perfect(27)
    1
    >>> count_perfect(28)
    2
    """
    if n == 0:
        return 0
    else:
        return count_perfect(n-1) + int(is_perfect(n))


def is_prime(n: int, _progress: int = 2) -> bool:
    """Calculate if a number is a prime.
    Pre-condition n is a natural number.
    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    """
    if n <= 1: # 0 and 1 are not prime numbers
        return False
    elif _progress == n:
        return True
    else:
        return is_prime(n, _progress + 1) and n%_progress != 0


def count_primes(n: int) -> int:
    """Calculate the amount of primes smaller than n including n.
    Pre-condition n is a natural number.
    >>> count_primes(6)
    3
    >>> count_primes(7)
    4
    """
    if n == 0:
        return 0
    else:
        return count_primes(n - 1) + int(is_prime(n))

 
def sum_beyond(k: int) -> int:
    """Calculate the smallest number n where the sum of all natural
    numbers up to n excluding n sums up to at least k.
    Pre-condition k is a natural number.
    >>> sum_beyond(0)
    2
    >>> sum_beyond(14)
    6
    """
    def sum_beyond_solver(k: int, progress: int) -> int:
        """Helper function that solves the sum_beyond,
        but returns the result as a negative number
        and needs the starting position + 1.
        >>> sum_beyond_solver(14)
        -6
        """
        if progress == 0:
            return 0
        else:
            # sr can both store the sum or the result
            # this depends on if the number is negative
            # if positive it stores the sum
            # if negative it stores the result
            sr = sum_beyond_solver(k, progress - 1)
            if sr < 0:
                return sr
            elif k < sr:
                return -progress
            else:
                return sr + progress
            

    # if k is 0 for example we need 1 therefore k + 2
    return -sum_beyond_solver(k, k + 2)


def is_palindrome(n: int) -> bool:
    """Calculate if a number is a palindrome.
    Pre-condition n is a natural number.
    >>> is_palindrome(10)
    False
    >>> is_palindrome(11)
    True
    >>> is_palindrome(303)
    True
    >>> is_palindrome(301)
    False
    """
    s = str(n)
    if s[0] != s[-1]:
        return False
    
    ns = s[1:-1]
    if ns == "":
        return True
    else:
        return is_palindrome(int(ns))


def find_power(k: int, _n: int = 0) -> int:
    """Calculate the smallest int n such that 2^n starts with k.
    Pre-condition k must be a natural number and,
    must be some more specific value or something i guess......
    >>> find_power(8)
    3
    >>> find_power(6)
    6
    """
    if str(2**_n).startswith(str(k)):
        return _n
    else:
        return find_power(k, _n+1)


def length(v: list) -> int:
    """Calculate the length of any list.
    >>> length([2, 5, 7, 9])
    4
    """
    if not v:
        return 0
    else:
        return length(v[1:]) + 1


def count(x: Any, v: list) -> int:
    """Calculate the amount of times x apears in v.
    >>> count(2, [2, 5, 6, 2, 4, 2])
    3
    """
    if not v:
        return 0
    else:
        return count(x, v[1:]) + int(x == v[0])


def member(x: Any, v:list) -> bool:
    """Check if x is in a list v.
    >>> member(3, [2, 3, 4])
    True
    >>> member(6, [2, 3, 4])
    False
    """
    if not v:
        return False
    else:
        return member(x, v[1:]) or x == v[0]

def subset(v: list, w:list) -> bool:
    """Check if v is a subset of w.
    >>> subset([2, 4], [2, 3, 4])
    True
    >>> subset([2, 5], [2, 3, 4])
    False
    """
    if not v:
        return True
    else:
        return subset(v[1:], w) and member(v[0], w)


def set_equals(v: list, w: list) -> bool:
    """Check if two list represent the same set.
    >>> set_equals([3, 4, 2], [4, 2, 3])
    True
    >>> set_equals([3, 4, 2], [4, 2, 3, 2])
    False
    >>> set_equals([3, 5, 2], [4, 1, 3])
    False
    """
    if not v:
        if w:
            return False
        else:
            return True
    else:
        try:
            w.remove(v[0])
            return set_equals(v[1:], w)
        except ValueError:
            return False


def intersection(v: list, w:list) -> list:
    """Compute the shared elements of two lists, returns shared duplicates.
    >>> intersection([2, 4, 6, 8], [5, 2, 6, 1])
    [6, 2]
    >>> intersection([3, 4, 3, 6], [5, 3, 6, 3])
    [6, 3, 3]
    """
    if not v:
        return []
    else:
        i = intersection(v[1:], w)
        with suppress(ValueError):
            w.remove(v[0])
            i.append(v[0])
        
        return i


def sum(v: list[int]) -> int:
    """Calculate the sum of all elements in v.
    >>> sum([5, 2, 4])
    11
    """
    if not v:
        return 0
    else:
        return sum(v[1:]) + v[0]


def max(v: list[int]) -> int:
    """Compute the maximum value in a list.
    Pre-condition list has at least 1 element.
    >>> max([3, 5, 2, 4])
    5
    """
    if len(v) == 1:
        return v[0]
    else:
        m = max(v[1:])
        return m if v[0] < m else v[0]


def smaller_than(n: int, v: list[int]) -> int:
    """Count the amount of elements less than n.
    >>> smaller_than(5, [5, 3, 4, 6])
    2
    """
    if not v:
        return 0
    else:
        return smaller_than(n, v[1:]) + int(n>v[0])
    

def two_zeros(v: list[int]) -> bool:
    """Check whether a list contains two consecutive zeros.
    >>> two_zeros([4, 0, 0, 1 , 3])
    True
    >>> two_zeros([4, 4, 0, 2, 0])
    False
    """
    if len(v) <= 1:
        return False
    else:
        return two_zeros(v[1:]) or v[0] == v[1] == 0 


def even_after_7(v: list[int]) -> int:
    """Compute the amount of even elements after the first 7 elements.
    Pre-condition the list v contains 7 or more elements.
    >>> even_after_7([5, 2, 7, 0, 7, 2, 2, 4, 5, 2])
    2
    """
    def count_even(w: list) -> int:
        """Count the amount of even numbers in a list.
        >>> count_even([3, 5, 2, 4 , 3, 6, 1])
        3
        """
        if not w:
            return 0
        else:
            return count_even(w[1:]) + int(w[0]%2 == 0)
        
    return count_even(v[7:])


def is_sorted(v: list[int]) -> bool:
    """Check if a list is sorted.
    >>> is_sorted([3, 5, 6, 29])
    True
    >>> is_sorted([3, 2, 6, 29])
    False
    """
    if len(v) <= 1: # always sorted if one or zero elements
        return True
    else:
        return is_sorted(v[1:]) and v[0] < v[1]


def squares(n: int) -> list[int]:
    """Calculate all squares from 1 to and including n.
    Pre-condition n is a natural number.
    >>> squares(4)
    [1, 4, 9, 16]
    """
    s = [n**2]
    if n == 1:
        return s
    else:
        return squares(n-1) + s
    

def decreasing_squares(n: int) -> list[int]:
    """Calculate all squares from n to and including 1.
    Pre-condition n is a natural number.
    >>> decreasing_squares(4)
    [16, 9, 4, 1]
    """
    s = [n**2]
    if n > 1:
        s += decreasing_squares(n-1)
    return s
    

def divisors(n: int, _divisor: int = 1) -> list[int]:
    """Calculate the divisors for the number n, including n.
    Pre-condition n is a natural number.
    >>> divisors(12)
    [12, 6, 4, 3, 2, 1]
    >>> divisors(0)
    []
    """
    if _divisor > n: # happens if 0 is used as n
        return []
    if _divisor == n: # any number is divisible by itself except 0
        return [n]
    else:
        d = divisors(n, _divisor + 1)
        if n%_divisor == 0:
            d.append(_divisor)
        return d

def square_it(v: list[int]) -> list[int]:
    """Square every number in the list v.
    >>> square_it([3, 5, 7])
    [9, 25, 49]
    """
    if not v:
        return []
    else:
        return [v[0]**2] + square_it(v[1:])


def reverse(v: list[int]) -> list[int]:
    """Reverse a list.
    >>> reverse([4, 1, 3, 12])
    [12, 3, 1, 4]
    """
    if not v:
        return []
    else:
        return reverse(v[1:]) + [v[0]]
















































