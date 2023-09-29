from typing import Any
from contextlib import suppress
from functools import reduce


def sum_up_to(n: int) -> int:
    """Calculate the sum up to and including n.
    Pre-condition: n is a natural number.
    >>> sum_up_to(4)
    10
    """
    if n == 0:
        return 0
    else:
        return n + sum_up_to(n - 1)


def sum_even(n: int) -> int:
    """Calculate the sum of even numbers up to and including n.
    Pre-condition: n is a natural number.
    >>> sum_even(7)
    12
    >>> sum_even(4)
    6
    """
    n -= n % 2
    if n == 0:
        return 0
    else:
        return sum_even(n - 2) + n


def sum_between(m: int, n: int) -> int:
    """Calculate the sum between m and n including m and n.
    Pre-condition: n is greater than or equal to m.
    >>> sum_between(-2, 4)
    7
    >>> sum_between(3, 5)
    12
    """
    if m == n:
        return n
    else:
        return m + sum_between(m + 1, n)


def factorial(n: int) -> int:
    """Calculate the factorial of a number.
    Pre-condition n is a natural number.
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


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
        return n * double_factorial(n - 2)


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
        return 1 + logarithm(n // 2)


def gcd(m: int, n: int) -> int:
    """Calculate greatest common divisor for two numbers.
    Pre-condition: m and n are positive integers.
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
    Pre-condition: m and n are positive integers.
    >>> lcm(6, 4)
    12
    """
    return m * n // gcd(m, n)


def first_digit(n: int, k: int = 10) -> int:
    """Calculate first digit of n in k base representation,
    where n is in base 10 representation.
    Pre-condition: k is a positive integer.
    >>> first_digit(12, 3)
    1
    >>> first_digit(98)
    9
    """
    if n < k:
        return n
    else:
        return first_digit(n // k, k)


def print_multiples(k: int, n: int, _progress: int = 0) -> None:
    """Print the multiples of k that are less than n not including n.
    Pre-condition: k is a positve integer and n is a natural number.
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
    if _divisor > n:  # happens if 0 is used as n
        return 0
    elif _divisor == n:
        return 1
    else:
        return int(n % _divisor == 0) + count_divisors(n, _divisor + 1)


def is_perfect(n: int) -> bool:
    """Calculate if an integer n is a perfect number.
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
    """Calculate the number of perfect numbers smaller than n or equal to n.
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
        return count_perfect(n - 1) + int(is_perfect(n))


def is_prime(n: int, _progress: int = 2) -> bool:
    """Calculate if a number is a prime.
    Pre-condition n is a natural number.
    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    """
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    elif _progress == n:
        return True
    else:
        return is_prime(n, _progress + 1) and n % _progress != 0


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


def sum_beyond(k: int) -> int:  # TODO make smarter
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
    Pre-condition k must be a natural number.
    >>> find_power(8)
    3
    >>> find_power(6)
    6
    """
    if str(2**_n).startswith(str(k)):
        return _n
    else:
        return find_power(k, _n + 1)


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


def member(x: Any, v: list) -> bool:
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


def subset(v: list, w: list) -> bool:
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


def intersection(v: list, w: list) -> list:
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
        return smaller_than(n, v[1:]) + int(n > v[0])


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
            return count_even(w[1:]) + int(w[0] % 2 == 0)

    return count_even(v[7:])


def is_sorted(v: list[int]) -> bool:
    """Check if a list is sorted.
    >>> is_sorted([3, 5, 6, 29])
    True
    >>> is_sorted([3, 2, 6, 29])
    False
    """
    if len(v) <= 1:  # always sorted if one or zero elements
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
        return squares(n - 1) + s


def decreasing_squares(n: int) -> list[int]:
    """Calculate all squares from n to and including 1.
    Pre-condition n is a natural number.
    >>> decreasing_squares(4)
    [16, 9, 4, 1]
    """
    s = [n**2]
    if n > 1:
        s += decreasing_squares(n - 1)
    return s


def divisors(n: int, _divisor: int = 1) -> list[int]:
    """Calculate the divisors for the number n, including n.
    Pre-condition n is a natural number.
    >>> divisors(12)
    [12, 6, 4, 3, 2, 1]
    >>> divisors(0)
    []
    """
    if _divisor > n:  # happens if 0 is used as n
        return []
    if _divisor == n:  # any number is divisible by itself except 0
        return [n]
    else:
        d = divisors(n, _divisor + 1)
        if n % _divisor == 0:
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
        return [v[0] ** 2] + square_it(v[1:])


def reverse(v: list) -> list:
    """Reverse a list.
    >>> reverse([4, 1, 3, 12])
    [12, 3, 1, 4]
    """
    if not v:
        return []
    else:
        return reverse(v[1:]) + [v[0]]


def compare(v: list[int], n: int) -> tuple[int, int, int]:
    """Compute number of elements greater than n,
    the number of elements v equal to n,
    number of elements less than n. In this order.
    >>> compare([2, 3, 7, 4, 10, 9, 4, 4], 4)
    (3, 3, 2)
    """
    if not v:
        return (0, 0, 0)
    else:
        r = compare(v[1:], n)
        return (r[0] + int(v[0] > n), r[1] + int(v[0] == n), r[2] + int(v[0] < n))


def join(v: list, w: list) -> list:
    """Join v followed by w.
    >>> join([2, 3, 1], [2, 8])
    [2, 3, 1, 2, 8]
    """
    if not w:
        return v
    else:
        return join(v + [w[0]], w[1:])


def sorted_join(v: list[int], w: list[int]) -> list[int]:
    """Join 2 sorted lists, usch that the list returned is ordered.
    Pre-condition: v and w are sorted lists.
    >>> sorted_join([3, 5, 11, 13], [1, 7, 14])
    [1, 3, 5, 7, 11, 13, 14]
    """
    if not v or not w:
        return v + w
    elif v[0] < w[0]:
        return [v[0]] + sorted_join(v[1:], w)
    else:
        return [w[0]] + sorted_join(v, w[1:])


def shuffle(v: list, w: list) -> list:
    """Create list where values from v and w alternate.
    Pre-condition: v and w has the same length.
    >>> shuffle([1, 4, 6], [2, 7, 9])
    [1, 2, 4, 7, 6, 9]
    """
    if not v:
        return []
    else:
        return [v[0], w[0]] + shuffle(v[1:], w[1:])


def remove(x: Any, v: list) -> list:
    """Compute list with all occurences of x removed.
    >>> remove(4, [4, 2, 3, 4, 2, 4])
    [2, 3, 2]
    """
    if not v:
        return []
    elif v[0] == x:
        return remove(x, v[1:])
    else:
        return [v[0]] + remove(x, v[1:])


def s_count(c: str, s: str) -> int:
    """Count number of occurrences character in c, in s.
    >>> s_count("c", "heycyascac")
    3
    """
    if s == "":
        return 0
    elif c == s[0]:
        return s_count(c, s[1:]) + 1
    else:
        return s_count(c, s[1:])


def s_member(c: str, s: str) -> bool:
    """Check if character c is in string s.
    >>> s_member("c", "heycyascac")
    True
    >>> s_member("e", "gfhf")
    False
    """
    return s != "" and (c == s[0] or s_member(c, s[1:]))


def is_prefix(s1: str, s2: str) -> bool:
    """Check if s1 is a prefix of s2.
    >>> is_prefix("her", "herme")
    True
    >>> is_prefix("nau", "nata")
    False
    """
    return not s1 or (s2 != "" and s1[0] == s2[0] and is_prefix(s1[1:], s2[1:]))


def is_suffix(s1: str, s2: str) -> bool:
    """Check if s1 is a prefix of s2.
    >>> is_suffix("rme", "herme")
    True
    >>> is_suffix("nsa", "nata")
    False
    """
    return not s1 or (s2 != "" and s1[-1] == s2[-1] and is_suffix(s1[:-1], s2[:-1]))


def is_substring(s1: str, s2: str) -> bool:
    """Check is s1 is a substring of s2.
    >>> is_substring("hey", "aheylo")
    True
    >>> is_substring("heya", "aheylo")
    False
    """
    return s2 != "" and (is_prefix(s1, s2) or is_substring(s1, s2[1:]))


def s_contains(s1: str, s2: str) -> bool:
    """Check if s2 can be obtained by deleting characters from s1.
    >>> s_contains("haea", "hea")
    True
    >>> s_contains("haea", "hya")
    False
    """
    return s2 == "" or (
        s1 != ""
        and ((s1[0] == s2[0] and s_contains(s1[1:], s2[1:])) or s_contains(s1[1:], s2))
    )


def ceasar_code(s: str, n: int) -> str:
    """Caesar encode a string by increasing each char by n,
    that wraps characters from a-z.
    >>> ceasar_code("heY", 2)
    'jgA'
    """
    if not s:
        return ""
    else:
        nc = (
            " "
            if s[0] == " "
            else chr(
                (ord(s[0].lower()) + n - ord("a")) % (ord("z") + 1 - ord("a"))
                + (ord("A") if s[0].isupper() else ord("a"))
            )
        )

        return nc + ceasar_code(s[1:], n)


def to_uppercase(s: str) -> str:
    """Convert all alphabetic characters in string to uppercase.
    >>> to_uppercase("Hey aA")
    'HEY AA'
    """
    if not s:
        return ""
    elif ord("a") <= ord(s[0]) <= ord("z"):
        return chr(ord(s[0]) - ord("a") + ord("A")) + to_uppercase(s[1:])
    else:
        return s[0] + to_uppercase(s[1:])


def to_lowercase(s: str) -> str:
    """Convert all alphabetic characters in string to uppercase.
    >>> to_lowercase("Hey aA")
    'hey aa'
    """
    if not s:
        return ""
    elif ord("A") <= ord(s[0]) <= ord("Z"):
        return chr(ord(s[0]) - ord("A") + ord("a")) + to_lowercase(s[1:])
    else:
        return s[0] + to_lowercase(s[1:])


def toCamelCase(s: str) -> str:
    """Changes text to camel case by removing spaces,
    and changing the next character to uppercase.
    >>> toCamelCase("this is camel case")
    'thisIsCamelCase'
    """
    if not s:
        return ""
    elif s[0] == " ":
        if len(s) == 2:  # check if there isn't a character after space
            return ""
        else:
            return to_uppercase(s[1]) + toCamelCase(s[2:])
    else:
        return s[0] + toCamelCase(s[1:])


def equals_ignore_case(s1: str, s2: str) -> bool:
    """Check if strings are equal ignoring if letters are lower or upper-case.
    >>> equals_ignore_case("heY A", "HeY a")
    True
    >>> equals_ignore_case("heY b", "HeY a")
    False
    """
    return to_lowercase(s1) == to_lowercase(s2)


def first_position(c: str, s: str) -> int:
    """Index of first occurrence of character c in string s,
    returns -1 if it is not in string s.
    >>> first_position("c", "hecac")
    2
    >>> first_position("v", "hecac")
    -1
    """
    if not s:
        return -1
    elif c == s[0]:
        return 0
    else:
        r = first_position(c, s[1:])
        return r if r == -1 else r + 1


def last_position(c: str, s: str) -> int:
    """Index of last occurrence of character c in string s,
    returns -1 if it is not in string s.
    >>> last_position("c", "hecac")
    4
    >>> last_position("v", "hecac")
    -1
    """

    def _last_position(c: str, s: str) -> int:
        if not s:
            return -1
        elif c == s[-1]:
            return 1
        else:
            r = first_position(c, s[:-1])
            return r if r == -1 else r + 1

    p = _last_position(c, s)
    return -1 if p == -1 else len(s) - p


def positions(c: str, s: str) -> list[int]:
    """Return list of positions where c occur in s.
    >>> positions("h", "heheh")
    [0, 2, 4]
    """
    if not s:
        return []
    else:
        v = [0] if c == s[0] else []
        return v + [e + 1 for e in positions(c, s[1:])]


def is_permutation(s1: str, s2: str) -> bool:
    """Check if s1 is a permutation of s2, with same characters counting repetitions.
    >>> is_permutation("aba", "aab")
    True
    >>> is_permutation("aba", "abb")
    False
    """
    if not s1 and not s2:
        return True
    elif not s1 or not s2:
        return False
    elif s_member(s1[0], s2):
        p = first_position(s1[0], s2)
        return is_permutation(s1[1:], s2[:p] + s2[p + 1 :])
    else:
        return False


def s_reverse(s: str) -> str:
    """Reverse a string.
    >>> s_reverse("hey")
    'yeh'
    """
    if not s:
        return ""
    else:
        return s_reverse(s[1:]) + s[0]


def reverse_words(s: str) -> str:
    """Reverse each word seperated by space, while preserving order.
    >>> reverse_words("lar nar bas")
    'ral ran sab'
    """

    def _split(s: str) -> list[str]:
        if not s:
            return []
        else:
            p = first_position(" ", s)
            if p == -1:
                return [s]
            else:
                return [s[:p]] + _split(s[p + 1 :])

    def _reverse_words(v: list[str]) -> list[str]:
        if not v:
            return []
        else:
            return [v[0][::-1]] + _reverse_words(v[1:])

    def _join(v: list[str]) -> str:
        if not v:
            return ""
        elif len(v) == 1:
            return v[0]
        else:
            return v[0] + " " + _join(v[1:])

    return _join(_reverse_words(_split(s)))


def remove_vowels(s: str) -> str:
    """Remove all vowels from a string.
    >>> remove_vowels("hey you are fine")
    'h  r fn'
    """
    if not s:
        return ""
    elif s[0] in ["a", "e", "i", "o", "u", "y"]:
        return remove_vowels(s[1:])
    else:
        return s[0] + remove_vowels(s[1:])


def respace(s: str, n: int) -> str:
    """Remove all spaces and add a space after every n character.
    >>> respace("hey how are you", 2)
    'he yh ow ar ey ou '
    """

    def _remove_spaces(s: str) -> str:
        if not s:
            return ""
        elif s[0] == " ":
            return _remove_spaces(s[1:])
        else:
            return s[0] + _remove_spaces(s[1:])

    def _respace(s: str, n: int) -> str:
        if not s:
            return ""
        if len(s) >= 2:
            return s[0:2] + " " + _respace(s[2:], n)
        else:
            return s[0]

    return _respace(_remove_spaces(s), n)


def encode_with_key(s: str, code: dict[str, str]) -> str:
    """Encode the key chracter by character using the hashmap.
    >>> encode_with_key("hE y", {"H": "B", "E": "L", "Y": "C"})
    'bL c'
    """
    if not s:
        return ""
    elif ord("a") <= ord(s[0]) <= ord("z"):
        return to_lowercase(code[to_uppercase(s[0])]) + encode_with_key(s[1:], code)
    elif ord("A") <= ord(s[0]) <= ord("Z"):
        return code[s[0]] + encode_with_key(s[1:], code)
    else:
        return s[0] + encode_with_key(s[1:], code)


def histogram(s: str) -> dict[str, int]:
    """Return a dictionary containing how many times a alphabetic letter appeared.
    >>> histogram("tes tss")
    {'S': 3, 'T': 2, 'E': 1}
    """
    if not s:
        return dict()
    elif ord("A") <= ord(to_uppercase(s[0])) <= ord("Z"):
        h = histogram(s[1:])
        h[to_uppercase(s[0])] = h.get(to_uppercase(s[0]), 0) + 1
        return h
    else:
        return histogram(s[1:])


def replicate(s: str, v: list[int]) -> str:
    """Replicate each character s[i] by v[i].
    Pre-condition: len(s) == len(v) and each int in v is a positive integer.
    >>> replicate("tes", [2, 4, 3])
    'tteeeesss'
    """
    if not s:
        return ""
    else:
        return s[0] * v[0] + replicate(s[1:], v[1:])


def f_sum(v: list[int]) -> int:
    """Sum of a list of ints.
    >>> f_sum([1, 4, 6, 2])
    13
    >>> f_sum([])
    0
    """
    return reduce(lambda x, y: x + y, v, 0)


def f_length(v: list) -> int:
    """Length of a list.
    >>> f_length([2, 3, 1, 2, 2])
    5
    """
    return reduce(lambda x, y: x + 1, v, 0)


def f_remove(x: Any, v: list) -> list:
    """Remove all occurrences of x from v.
    >>> f_remove(3, [3, 4, 3, 2])
    [4, 2]
    """
    return list(filter(lambda y: x != y, v))


def f_count(x: Any, v: list) -> int:
    """Count occurrences of x in list v.
    >>> f_count(2, [3, 2, 3, 2, 5])
    2
    """
    return reduce(lambda z, k: z + 1, filter(lambda y: x == y, v), 0)


def f_max(v: list[int]) -> int:
    """Largest element in a list.
    Pre-condition: list must have 1 or more elements.
    >>> f_max([2, 4, 1, 3])
    4
    """
    return reduce(lambda x, y: x if x > y else y, v)


def f_square_it(v: list[int]) -> list[int]:
    """Square all elements in v.
    Pre-condition element contains at least one element.
    >>> f_square_it([3, 1,  2, 4])
    [9, 1, 4, 16]
    """
    return list(map(lambda x: x**2, v))


def f_squares(n: int) -> list[int]:
    """List of squares from 1 to n, including n.
    Pre-condition: n is a positive integer.
    >>> f_squares(4)
    [1, 4, 9, 16]
    """
    return list(map(lambda x: x**2, range(1, n + 1)))


def f_decreasing_squares(n: int) -> list[int]:
    """List of squares from n to 1, including 1.
    Pre-condition: n is a positive integer.
    >>> f_decreasing_squares(4)
    [16, 9, 4, 1]
    """
    return list(map(lambda x: x**2, range(n, 1 - 1, -1)))


def f_reverse(v: list) -> list:
    """Reverse a list.
    Pre-condition: list contains at least one element.
    >>> f_reverse([3, 1, 2])
    [2, 1, 3]
    """
    return reduce(lambda x, y: [y] + x, v, [])


def f_sum_up_to(n: int) -> int:
    """Sum up to n, excluding n.
    Pre-condition: n is a natural number.
    >>> f_sum_up_to(4)
    6
    >>> f_sum_up_to(0)
    0
    """
    return reduce(lambda x, y: x + y, range(n), 0)


def f_sum_between(m: int, n: int) -> int:
    """Sum between m and n, including m and not n.
    >>> f_sum_between(-2, 4)
    3
    """
    return reduce(lambda x, y: x + y, range(m, n), 0)


def f_sum_even(n: int) -> int:
    """Sum of all even numbers up to n, excluding n.
    Pre-condition: n is a natural number.
    >>> f_sum_even(5)
    6
    >>> f_sum_even(6)
    6
    """
    return reduce(lambda x, y: x + y, range(0, n, 2), 0)


def f_factorial(n: int) -> int:
    """Factorial of n.
    Pre-condition: n is a natural number.
    >>> f_factorial(4)
    24
    """
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def f_double_factorial(n: int) -> int:
    """Double factorial of n.
    Pre-condition: n is a natural number.
    >>> f_double_factorial(4)
    8
    >>> f_double_factorial(5)
    15
    """
    return reduce(lambda x, y: x * y, range(2 + n % 2, n + 1, 2), 1)


def f_member(x: Any, v: list) -> bool:
    """Check if x is a member of v.
    >>> f_member(3, [4, 3, 2, 1])
    True
    >>> f_member(3, [4, 2, 1])
    False
    """
    return reduce(lambda y, z: y or z == x, v, False)
    #      reduce(lambda y, z: y or z, filter(lambda m: m == x, v), False)


def f_subset(v: list, w: list) -> bool:
    """Check if all elements in v occur in w.
    >>> f_subset([3, 4, 2], [1, 2, 4, 5, 3])
    True
    >>> f_subset([3, 4, 2], [1, 2, 5, 3])
    False
    """
    return reduce(lambda x, y: x and y in w, v, True)
    #      reduce(lambda x, y: x and y, map(lambda z: z in w, v), True)


def f_intersection(v: list, w: list) -> list:
    """Intersection between two lists.
    >>> f_intersection([3, 2, 1], [0, 1, 2])
    [2, 1]
    """
    return list(filter(lambda x: x in w, v))


def f_smaller_than(n: int, v: list[int]) -> int:
    """Count have many elements in v are strictly smaller than n.
    >>> f_smaller_than(5, [1, 4, 5, 7])
    2
    """
    return reduce(lambda x, y: x + 1, filter(lambda x: x < n, v), 0)


def f_ceasar_code(s: str, n: int) -> str:
    """Caesar encode a string by increasing each char by n,
    that wraps characters from a-z.
    >>> f_ceasar_code("he Y", 2)
    'jg A'
    """

    def _ceasar_char(c: str, n: int) -> str:
        if c == " ":
            return " "
        else:
            return chr(
                (ord(c.lower()) + n - ord("a")) % (ord("z") + 1 - ord("a"))
                + (ord("A") if c.isupper() else ord("a"))
            )

    return reduce(lambda x, y: x + y, map(lambda z: _ceasar_char(z, n), s), "")


def f_to_uppercase(s: str) -> str:
    """Convert alphabetic characters to uppercase.
    >>> f_to_uppercase("heY a")
    'HEY A'
    """

    def _to_uppercase(c: str) -> str:
        if ord("a") <= ord(c) <= ord("z"):
            return chr(ord(c) - ord("a") + ord("A"))
        else:
            return c

    return reduce(lambda x, y: x + y, map(lambda z: _to_uppercase(z), s), "")


def f_to_lowercase(s: str) -> str:
    """Convert alphabetic characters to uppercase.
    >>> f_to_lowercase("heY a")
    'hey a'
    """

    def _to_lowercase(c: str) -> str:
        if ord("A") <= ord(c) <= ord("Z"):
            return chr(ord(c) - ord("A") + ord("a"))
        else:
            return c

    return reduce(lambda x, y: x + y, map(lambda z: _to_lowercase(z), s), "")


def f_count_divisors(n: int) -> int:
    """Count positive divisors for n.
    Precondition n is a non zero integer.
    >>> f_count_divisors(8)
    4
    >>> f_count_divisors(-8)
    4
    """
    n = abs(n)
    return reduce(lambda x, y: x + 1, filter(lambda z: n % z == 0, range(1, n + 1)), 0)


def f_is_perfect(n: int) -> int:
    """Check if n is a perfect number.
    Pre-condition: n is a positive integer.
    >>> f_is_perfect(6)
    True
    >>> f_is_perfect(8)
    False
    """
    return (
        reduce(
            lambda x, y: x + y, filter(lambda z: n % z == 0, range(1, n // 2 + 1)), 0
        )
        == n
    )


def f_count_perfect(n: int) -> int:
    """Count number of perfect numbers less than n or equal to n.
    Pre-condition n is a positive integer.
    Tests from https://en.wikipedia.org/wiki/Perfect_number.
    >>> f_count_perfect(27)
    1
    >>> f_count_perfect(28)
    2
    """
    return reduce(lambda x, y: x + 1, filter(f_is_perfect, range(1, n + 1)), 0)


def f_is_prime(n: int) -> int:
    """Check if n is a prime number.
    Pre-condition: n is a natural number.
    >>> f_is_prime(7)
    True
    >>> f_is_prime(4)
    False
    """

    if n == 0:
        return False
    else:
        return (
            reduce(
                lambda x, y: x + 1,
                filter(lambda z: n % z == 0, range(1, n // 2 + 1)),
                0,
            )
            == 1  # Must have 1 divisor to be a prime, as the other is implicitly itself
        )


def f_count_primes(n: int) -> int:
    """Count number of prime numbers less than n or equal to n.
    Pre-condition: n is a natural number.
    >>> f_count_primes(7)
    4
    >>> f_count_primes(6)
    3
    """
    return reduce(lambda x, y: x + 1, filter(f_is_prime, range(n + 1)), 0)
