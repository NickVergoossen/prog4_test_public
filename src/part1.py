from operator import mul
def volume_kubus(x):
    """Return the volume of a cube

    Raise a RuntimeError exception with message "negatieve lengte" if x < 0.
    """
    if x < 0:
        raise RuntimeError("negatieve lengte")
    v = x*x*x
    return v


def minutes_in_day(x):
    """Return the number of minutes in x days

    Raise a custom NegativeDuration exception if x < 0.
    """
    class NegativeDuration(RuntimeError):
        pass

    if x < 0:
        raise NegativeDuration
    return 60 * 24 * x


def minutes_in_week(x):
    """Return the number of minutes in x weeks"""
    return 60 * 24 * x * 7


def list_of_squares(n):
    """Return a list of the first n squares

    >>> list_of_squares(3)
    [0, 1, 4]
    """
    L = [i*i for i in range(1, n+1)]
    return L


def product_of_list(l):
    """Return the product of all numbers in the list

    >>> product_of_list([2,3,4])
    24
    """
    p=1
    for i in l:
        p= i*p
    return p


def price_search(articles, name):
    """Return the price of the article in list articles

    >>> articles = [
        ["Doom", 25],
        ["Among Us", 5],
    ]
    >>> price_search("Doom")
    25
    """

