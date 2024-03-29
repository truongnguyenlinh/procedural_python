import doctest


def sum_of_primes(upperbound: int) -> int:
    """Return the sum of probes between 0 and upper bound as an integer.

    PRECONDITION upperbound is a positive integer
    RETURN the sum of all prime numbers including upperbound
    >>> sum_of_primes(10)
    17
    >>> sum_of_primes(5)
    10
    >>> sum_of_primes(0)
    0
    >>> sum_of_primes(1000)
    76127
    """
    not_primes = []
    prime = []
    if upperbound < 0:
        raise ValueError("Please enter a positive integer!")
    else:
        for i in range(2, upperbound + 1):
            if i not in not_primes:
                prime.append(i)
                for j in range(i*i, upperbound + 1, i):
                    not_primes.append(j)
        return sum(prime)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
