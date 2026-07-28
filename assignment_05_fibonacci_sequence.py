# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# PART A: Function to print the first N terms
def print_first_n_terms(n):
    first = 0
    second = 1
    counter = 0
    
    sequence_list = []
    while counter < n:
        sequence_list.append(first)
        next_num = first + second
        first = second
        second = next_num
        counter = counter + 1
        
    print("Fibonacci sequence:", end=" ")
    for value in sequence_list:
        print(value, end=" ")
    print()

# PART B: Function to check if a number belongs to the sequence
def check_if_fibonacci(target):
    if target < 0:
        return False
        
    first = 0
    second = 1
    
    while first < target:
        next_num = first + second
        first = second
        second = next_num
        
    if first == target:
        return True
    else:
        return False

def main():
    try:
        user_n = input("How many terms? ")
        n_value = int(user_n)
        
        # Check if N is a positive integer as requested
        if n_value <= 0:
            print("Error: Number of terms must be a positive integer.")
            return
            
        print_first_n_terms(n_value)
        
        user_check = input("Enter a number to check: ")
        check_value = int(user_check)
        
        if check_if_fibonacci(check_value):
            print(check_value, "is a Fibonacci number.")
        else:
            print(check_value, "is NOT a Fibonacci number.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()
