import streamlit as st
import numpy as np
import pandas as pd
import math as m
import time
import sympy as sp
import scipy.optimize as spo


""" Bisection-Trisection method"""
def BTsection(f, a, b, tol, imax):
  for i in range(1, imax + 1):  # starts a loop that will iterate from 1 to imax"iteration"
    # Bisection step
    r = (a + b) / 2  # root of bisection
    if f(a) * f(r) < 0:  # check if a , r have oppsite signs
      b = r  # then 'b' will take the value of r
      r = (a + 2 * b) / 3  # calc the new root by using the trisection law
    elif f(r) * f(b) < 0:  # check if b , r have oppsite signs
      a = r  # then 'a' will take the value of r
      r = (2 * a + b) / 3  # calc the new root by using the trisection law

    # Trisection step
    if f(a) * f(r) < 0:  # check if a , r have oppsite signs
      b = r  # then 'b' will take the value of r
    elif f(r) * f(b) < 0:  # check if b , r have oppsite signs
      a = r  # then 'a' will take the value of r

    if abs(f(r)) < tol:  # # check if f(r) less than 10^-12
      return i, r, a, b

  return i, r, a, b