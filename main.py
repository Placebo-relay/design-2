import streamlit as st
from sympy import *
import numpy as np

def main():
    st.title('Custom Function Root Finder')

    # Sidebar for user input
    st.sidebar.header('Enter Custom Function')
    custom_function = st.sidebar.text_input('f(x) = ', 'x**2 - 4')
    initial_guess = st.sidebar.text_input('Initial Guess', value='pi')

    # Parse the custom function and initial guess using SymPy
    try:
        custom_function_expr = sympify(custom_function)
        user_input = sympify(initial_guess)
    except SympifyError:
        st.sidebar.error('Invalid input. Please enter a valid mathematical expression.')
        return

    # Display the input and output side by side
    col1, col2 = st.beta_columns(2)
    with col1:
        st.write('Input:', custom_function)
        st.write('Initial Guess:', initial_guess)

    with col2:
        # Method 1: Newton's method
        st.subheader('Newton\'s Method')
        root_newton = newtons_method(custom_function_expr, user_input)
        st.write(f'Root found with Newton\'s Method: {root_newton:.6f}')

        # Method 2: Super accurate method
        st.subheader('Super Accurate Method')
        all_roots = find_all_roots(custom_function_expr)
        st.write(f'All roots found: {all_roots}')

def newtons_method(expr, initial_guess, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, expr, 'numpy')
    f_prime = lambdify(x, diff(expr, x), 'numpy')

    x_n = initial_guess
    for _ in range(max_iter):
        x_n1 = x_n - f(x_n) / f_prime(x_n)
        if abs(x_n1 - x_n) < tol:
            return x_n1
        x_n = x_n1
    return x_n

def find_all_roots(expr, tol=1e-6):
    x = symbols('x')
    roots = []
    for guess in np.linspace(-10, 10, 100):  # Try different initial guesses
        try:
            root = nsolve(expr, x, guess)
            roots.append(root.evalf())
            root_eval = root.evalf()
            # Check if the root is distinct from existing roots
            if all(abs(root_eval - r) > tol for r in roots):
                roots.append(root_eval)
        except:
            pass  # Ignore any exceptions
    return roots

if __name__ == '__main__':
    main()
