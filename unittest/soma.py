def adicao(x, y):
    """ Soma x e Y

    >>> soma(10,20)
    30

    >>> soma(-10,20)
    10

    >>> soma(5,20)
    25

    >>> soma(5,5)
    10
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    return x + y
