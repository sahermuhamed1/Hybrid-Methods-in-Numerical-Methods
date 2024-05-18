import streamlit as st
import numpy as np
import pandas as pd
import math as m
import time
import sympy as sp
import scipy.optimize as spo

"""Newton-Raphson and Bisection Method"""
start_time = 0.0
start_time = time.time()

def newton_raphson_with_bisection(f, a, b, eps, imax, h=1e-5):
  if f(a) * f(b) > 0:
    raise ValueError("Root not bracketed")

  def df(x):
    return (f(x + h) - f(x - h)) / (2 * h)

  x = (a + b) / 2
  for i in range(imax):

    if abs(f(x)) < eps:
      return x, i + 1
    d = df(x)
    if d == 0:
      return None, i + 1
    x -= f(x) / d
    if f(a) * f(x) < 0:
      b = x
    else:
      a = x
  return None, imax