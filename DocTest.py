import doctest

def factorial(n):
    """
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(10)
    3628800
    >>> factorial(-1)  # Este test podría fallar si no se maneja el caso negativo.
    0
    """

    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def main():
    print(factorial(5))

main()

if __name__ == "__main__":
    doctest.testmod()
