import streamlit as st
import numpy as np
import pandas as pd
import math as m
import time
import sympy as sp
import scipy.optimize as spo
from Newton import Newton_answer
from Bisection import Bi_answer


# make a sidebar
st.sidebar.title("Numerical Methods Project")
page = st.sidebar.radio("Choose a method", ["Bi-Section Method","Newton-Raphson Method"])

if page == "Bi-Section Method":
    Bi_answer()
else:
    Newton_answer()