# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def check_if_prime(num):
    # Numbers less than 2 are not prime numbers
    if num < 2:
        return False
        
    # Check for factors manually using a simple loop
    for i in range(2, num):
        if num % i == 0:
            return False # Found a factor, so it is not prime
            
    return True # No factors found, so it is prime

def main():
    user_input = input("Enter a number: ")
    target_number = int(user_input)
    
    if check_if_prime(target_number):
        print(target_number, "is a prime number.")
    else:
        print(target_number, "is NOT a prime number.")

if __name__ == "__main__":
    main()

