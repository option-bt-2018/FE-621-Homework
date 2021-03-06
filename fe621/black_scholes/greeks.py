from .util import computeD1D2

from scipy.stats import norm

import numpy as np


def callDelta(current: float, volatility: float, ttm: float, strike: float,
              rf: float, dividend: float=0) -> float:
    """Function to compute the Delta of a call option using the Black-Scholes
    formula.
    
    Arguments:
        current {float} -- Current price of the underlying asset.
        volatility {float} -- Volatility of the underlying asset price.
        ttm {float} -- Time to expiration (in years).
        strike {float} -- Strike price of the option contract.
        rf {float} -- Risk-free rate (annual).
    
    Keyword Arguments:
        dividend {float} -- Dividend yield (annual) {default: {0}}.
    
    Returns:
        float -- Delta of a European Call Option contract.
    """

    d1, _ = computeD1D2(current, volatility, ttm, strike, rf)

    return np.exp(-1 * dividend * ttm) * norm.cdf(d1)


def putDelta(current: float, volatility: float, ttm: float, strike: float,
             rf: float, dividend: float=0) -> float:
    """Function to compute the Delta of a put option using the Black-Scholes
    formula.
    
    Arguments:
        current {float} -- Current price of the underlying asset.
        volatility {float} -- Volatility of the underlying asset price.
        ttm {float} -- Time to expiration (in years).
        strike {float} -- Strike price of the option contract.
        rf {float} -- Risk-free rate(annual).
    
    Keyword Arguments:
        dividend {float} -- Dividend yield (annual) (default: {0}).
    
    Returns:
        float -- Delta of a European Put Option contract.
    """

    d1, _ = computeD1D2(current, volatility, ttm, strike, rf)

    return -1 * np.exp(-1 * dividend * ttm) * norm.cdf(-1 * d1)


def callGamma(current: float, volatility: float, ttm: float, strike: float,
              rf: float) -> float:
    """Function to compute the Gamma of a Call option using the Black-Scholes
    formula.
    
    Arguments:
        current {float} -- Current price of the underlying asset.
        volatility {float} -- Volatility of the underlying asset price.
        ttm {float} -- Time to expiration (in years).
        strike {float} -- Strike price of the option contract.
        rf {float} -- Risk-free rate (annual).
    
    Returns:
        float -- Delta of a European Call Opton Option contract.
    """

    d1, _ = computeD1D2(current, volatility, ttm, strike, rf)

    return (norm.pdf(d1) / (current * volatility * np.sqrt(ttm)))


def vega(current: float, volatility: float, ttm: float, strike: float,
         rf: float) -> float:
    """Function to compute the Vega of an option using the Black-Scholes formula.
    
    Arguments:
        current {float} -- Current price of the underlying asset.
        volatility {float} -- Volatility of the underlying asset price.
        ttm {float} -- Time to expiration (in years).
        strike {float} -- Strike price of the option contract.
        rf {float} -- Risk-free rate (annual).
    
    Returns:
        float -- Vega of a European Option contract.
    """

    d1, _ = computeD1D2(current, volatility, ttm, strike, rf)

    return current * np.sqrt(ttm) * norm.pdf(d1)
