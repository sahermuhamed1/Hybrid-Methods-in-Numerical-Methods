import streamlit as st
import numpy as np
import sympy as sp

"""Newton-Raphson Method"""
def newton(f, df, x0, tol=1.e-6, maxit=100):
    # f = the function f(x)
    # df = the derivative of f(x)
    # x0 = the initial guess of the solution
    # tol = tolerance for the absolute error
    # maxit = maximum number of iterations
    err = 1.0
    iteration = 0
    xk = x0
    while err > tol and iteration < maxit:
        iteration += 1
        prev_xk = xk
        xk = xk - f(xk) / df(xk)  # corrected syntax
        err = np.abs(prev_xk - xk)  # compute the new error
        print(iteration, xk)
    return xk

def Newton_answer():
    st.title("Newton-Raphson Method")

    st.write("Please input the function")
    function = st.text_input("f(x) = ")

    try:
        # Convert the input function to sympy expression
        x = sp.symbols('x')
        f_expr = sp.sympify(function)
        f = sp.lambdify(x, f_expr, 'numpy')

        # Calculate the derivative using sympy
        df_expr = sp.diff(f_expr, x)
        df = sp.lambdify(x, df_expr, 'numpy')

        # Display the derivative for confirmation
        st.write(f"The derivative of the function is: {df_expr}")
    except Exception as e:
        st.error(f"Invalid function input: {e}")
        return

    st.write("Please input the initial guess")
    x0 = st.number_input("x0 = ", value=0.0)

    st.write("Please input the tolerance")
    tol = st.number_input("tolerance = ", value=1.e-6)

    try:
        x_root = newton(f, df, x0, tol)
        st.write("The root is", x_root)
        st.write("The value of the function at the root is", f(x_root))
    except Exception as e:
        st.error(f"An error occurred during the computation: {e}")

if __name__ == "__main__":
    Newton_answer()
