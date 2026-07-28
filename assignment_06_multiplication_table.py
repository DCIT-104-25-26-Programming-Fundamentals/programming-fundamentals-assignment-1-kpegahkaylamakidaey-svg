# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# PART A: Print a single table from 1 to 12
def print_single_table(num):
    print("Multiplication Table for " + str(num) + ":")
    for i in range(1, 13):
        answer = num * i
        print(num, "x", i, "=", answer)

# PART B: Bonus tables from 1 to N
def print_all_tables_up_to_n(n):
    for current_num in range(1, n + 1):
        print_single_table(current_num)
        print("---") # The required separator line

def main():
    try:
        # Execute Part A
        user_input_a = input("Enter a number: ")
        number_a = int(user_input_a)
        
        if number_a <= 0:
            print("Error: Number must be a positive integer.")
            return # Stop execution
            
        print_single_table(number_a)
        print() # Clean spacing line
        
        # Execute Part B
        user_input_b = input("Enter a number N: ")
        number_b = int(user_input_b)
        
        # Validation check for Part B as requested
        if number_b <= 0:
            print("Error: N must be a positive integer.")
            return # Stop execution
            
        print_all_tables_up_to_n(number_b)
        
    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    main()
