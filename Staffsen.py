import streamlit as st
import numpy as np
import pandas as pd
import math as m
import time
import sympy as sp
import scipy.optimize as spo


def steffensen_method(func, xi):
    # Define variables
    error = 1
    count = 0

    # Run until the error is less than 10^-6
    while error >= 1e-6 and count < 100:
        xi_old = xi
        xi = xi - ((func(xi))**2 / (func(xi + func(xi)) - func(xi)))

        # Find your error
        error = abs((xi - xi_old) / xi)

        # Count how many times this program is run
        count += 1

    return xi, error, count