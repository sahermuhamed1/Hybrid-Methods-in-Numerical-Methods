import streamlit as st
import numpy as np
import plotly.express as px

"""Bi-Section Method"""
def bisection(f, a, b, tol=1.e-6):
    iteration = 0  # initialize counter iteration
    if f(a) * f(b) >= 0.0:  # check if there is a root
        raise ValueError("The function must have different signs at endpoints a and b")

    x = (a + b) / 2  # initialize x to a midpoint value
    while (b - a) > tol:  # check if the end-points converge
        iteration += 1
        x = (a + b) / 2
        if f(a) * f(x) < 0.0:  # if f(b)'s sign equal to f(x)'s sign, then b=x
            b = x
        elif f(x) * f(b) < 0.0:  # if f(a)'s sign equal to f(x)'s sign, then a=x
            a = x
        else:
            break
        print(iteration, x)
    return x

def Bi_answer():
    # Bi-Section Method
    st.title("Bi-Section Method")

    # ask a user to input the function
    st.write("Please input the function")
    function = st.text_input("f(x) = ")

    try:
        f = lambda x: eval(function)
        # test if the function can be evaluated
        f(1)
    except Exception as e:
        st.error(f"Invalid function input: {e}")
        return

    # ask a user to input the interval
    st.write("Please input the interval")
    a = st.number_input("a = ", value=0.0)
    b = st.number_input("b = ", value=0.0)

    if a >= b:
        st.error("Invalid interval: 'a' must be less than 'b'")
        return

    # ask a user to input the tolerance
    st.write("Please input the tolerance")
    tol = st.number_input("tolerance = ", value=1.e-6)

    try:
        x = bisection(f, a, b, tol)
        st.write("The root is", x)
        st.write("The value of the function at the root is", f(x))
    except Exception as e:
        st.error(f"An error occurred during the computation: {e}")
        return

    # Plot the function
    x_vals = np.linspace(a, b, 1000)
    y_vals = np.array([f(x) for x in x_vals])
    fig = px.line(x=x_vals, y=y_vals, labels={'x': 'x', 'y': 'f(x)'})
    st.plotly_chart(fig)
