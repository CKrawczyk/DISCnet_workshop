'''Utility functions for calculating angle-based metrics'''


def angle_distance(a, b):
    '''A function that takes in two angles and returns the
    absolute values of the interior angle between them.

    Parameters
    ----------
    a : float
        The first angle in degrees
    b : float
        The second angle in degrees

    Returns
    -------
    d : float
        The absolute value of the interior angle between a and b
        in degrees
    '''
    return abs(b - a)
    #
    # return abs(b - a) % 180
    #
    # d = abs(b - a)
    # return min(360 - d, d)
    #
    # d = abs((b % 360) - (a % 360))
    # return min(360 - d, d)
