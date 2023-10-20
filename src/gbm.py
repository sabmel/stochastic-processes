# Geometric Brownian Motion related functions
import numpy as np

# TODO: Add functions and classes related to Geometric Brownian Motion


# TODO: simulate_stock_price: A function to simulate stock prices using GBM model
def simulate_stock_price(s0: float, mu: float, sigma: float, dt: float, n: int) -> np.ndarray:
    """
    Simulates stock prices using the Geometric Brownian Motion (GBM) model.

    Parameters:
    - s0 (float): Initial stock price.
    - mu (float): Expected return (drift coefficient).
    - sigma (float): Volatility (diffusion coefficient).
    - dt (float): Time increment, typically a day (1/252 for daily, assuming 252 trading days in a year).
    - n (int): Number of time steps to simulate.

    Returns:
    - np.ndarray: Simulated stock prices
    """

    # Generate standard Brownian motion (Wt)
    W = np.random.standard_normal(size=n)
    W = np.cumsum(W) * np.sqrt(dt) # standard brownian motion

    # Calculate stock prices using GBM formula
    t = np.arange(0, n)