# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Separate functions for each arithmetic operation
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return None
    return a / b

def modulus_numbers(a, b):
    if b == 0:
        return None
    return a % b

def exponentiate_numbers(a, b):
    return a ** b

# Helper function to remove decimal point trailing zero if integer
def format_num(n):
    if n.is_integer():
        return str(int(n))
    return str(n)

# Helper function to format results up to 2 decimal places
def format_result(res):
    if res.is_integer():
        return str(int(res))
    return f"{res:.2f}"

def main():
    while True:
        print("======================")
        print("SIMPLE CALCULATOR")
        print("======================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")
        
        choice = input("Select an operation (1-7): ")
        print()
        
        if choice == "7":
            print("Goodbye!")
            break
            
        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                n1_str = format_num(num1)
                n2_str = format_num(num2)
                
                if choice == "1":
                    ans = add_numbers(num1, num2)
                    print("Result:", n1_str, "+", n2_str, "=", format_result(ans))
                    
                elif choice == "2":
                    ans = subtract_numbers(num1, num2)
                    print("Result:", n1_str, "-", n2_str, "=", format_result(ans))
                    
                elif choice == "3":
                    ans = multiply_numbers(num1, num2)
                    print("Result:", n1_str, "*", n2_str, "=", format_result(ans))
                    
                elif choice == "4":
                    ans = divide_numbers(num1, num2)
                    if ans is None:
                        print("Error: Cannot divide by zero.")
                    else:
                        print("Result:", n1_str, "/", n2_str, "=", format_result(ans))
                        
                elif choice == "5":
                    ans = modulus_numbers(num1, num2)
                    if ans is None:
                        print("Error: Cannot divide by zero.")
                    else:
                        print("Result:", n1_str, "%", n2_str, "=", format_result(ans))
                        
                elif choice == "6":
                    ans = exponentiate_numbers(num1, num2)
                    print("Result:", n1_str, "**", n2_str, "=", format_result(ans))
                    
            except ValueError:
                print("Error: Please enter numbers only.")
        else:
            print("Invalid selection. Try again.")
        print()

if __name__ == "__main__":
    main()
