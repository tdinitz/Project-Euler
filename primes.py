# primes.py
# created 2017.05.13 by stacy kim

from numpy import *
from sys import *


def get_primes(max):
    """Returns primes through at least 'MAX', and the max integer checked up to."""

    primes = [2,3,5]
    mods = [1,5]
    imax = 2
    next_factors = primes[:imax]

    while True:

        base = prod(next_factors)
        imax += 1
        next_factors = primes[:imax]

        bases,modsz = meshgrid(base*arange(1,next_factors[-1]), mods)
        possible = (bases + modsz).flatten()

        for p in possible:
            if all(mod(p,next_factors)):  mods   += [p] # has none of the factors
            if all(mod(p,primes      )):  primes += [p] # not divisible by primes

        primes.sort()

        if base > max: break # we're done!

    return array(primes), base
