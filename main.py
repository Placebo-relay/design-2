import streamlit as st
from sympy import *
import numpy as np

def main():
    st.title('Custom Function Root Finder')

    # Sidebar for user input
    st.sidebar.header('Enter Custom Function')
    custom_function = st.sidebar.text_input('f(x) = ', 'x**2 - 4')

    # Parse the custom function using SymPy
    custom_function_expr = sympify(custom_function)

    # Main body
    st.header('Root Finding Methods')

    # Method 1: Newton's method with initial guess
    st.subheader("Newton's Method")
    initial_guess = st.sidebar.text_input('Initial Guess', value='3.0')
    if st.button("Find Root with Newton's Method"):
        root_newton = newtons_method(custom_function_expr, initial_guess)
        st.write(f'Root found with Newton\'s Method: {root_newton:.6f}')

    # Method 2: Super accurate method for finding all roots
    st.subheader('Super Accurate Method')
    if st.button('Find All Roots'):
        all_roots = find_all_roots(custom_function_expr)
        st.write(f'All roots found: {all_roots}')

def newtons_method(expr, initial_guess, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, expr, 'numpy')
    f_prime = lambdify(x, diff(expr, x), 'numpy')

    x_n = float(initial_guess)  # Convert initial_guess to float
    for _ in range(max_iter):
        x_n1 = x_n - f(x_n) / f_prime(x_n)
        if abs(x_n1 - x_n) < tol:
            return x_n1
        x_n = x_n1
    return x_n

def find_all_roots(expr, tol=1e-6):
    x = symbols('x')
    roots = set()  # Use a set to store unique roots
    for guess in np.linspace(-10, 10, 100):  # Try different initial guesses
        try:
            root = nsolve(expr, x, guess)
            root_eval = root.evalf()
            # Check if the root is distinct from existing roots
            is_distinct = all(abs(root_eval - r) > tol for r in roots)
            if is_distinct:
                roots.add(root_eval)  # Add the root to the set
        except:
            pass  # Ignore any exceptions
    return roots

if __name__ == '__main__':
    main()
