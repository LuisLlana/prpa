def is_prime(n, prime_list):
    """
    Function that tests if n is prime using the list of
    prime numbers prime_list

    Paramenters
    -----------
    n: int
    prime_list: list of int

    Precondition
    ------------
    n>2
    prime_list is an ordered list. l[i] contains the i-th prime number.
    """
    i = 2
    while i*i < n and n%i!=0:
        i = next_prime(i, prime_list)
    return i*i>n


def next_prime(n, prime_list):
    """
    Function that compute the next prime number after n.
    Paramenters
    -----------
    n: int
    prime_list: list of int

    Precondition
    ------------
    n>2
    prime_list is an ordered list. l[i] contains the i-th prime number.
    """
    n += 1
    if n<prime_list[-1]:
        i = 0
        while n > prime_list[i]:
            i += 1
        prime = prime_list[i]
    else:
        i = prime_list[-1] + 1
        while prime_list[-1]<n:
            i += 1
            if is_prime(i, prime_list):
                prime_list.append(i)
        prime = prime_list[-1]
    return prime
