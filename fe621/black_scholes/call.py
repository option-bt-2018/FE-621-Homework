from .util import computeD1D2

from scipy.stats import norm
import numpy as np


def blackScholesCall(current: float, volatility: float, ttm: float,
                     strike: float, rf: float) -> float:
    """Function to compute the Black-Scholes-Merton price of a European Call
    Option, parameterized by the current underlying asset price, volatility,
    time to expiration, strike price, and risk-free rate.
    
    Arguments:
        current {float} -- Current price of the underlying asset.
        volatility {float} -- Volatility of the underlying asset price.
        ttm {float} -- Time to expiration (in years).
        strike {float} -- Strike price of the option contract.
        rf {float} -- Risk-free rate (annual).
    
    Returns:
        float -- Price of a European Call Option contract.
    """

    d1, d2 = computeD1D2(current, volatility, ttm, strike, rf)

    call = (current * norm.cdf(d1)) \
        - (strike * np.exp(-1 * rf * ttm) * norm.cdf(d2))

    return call
