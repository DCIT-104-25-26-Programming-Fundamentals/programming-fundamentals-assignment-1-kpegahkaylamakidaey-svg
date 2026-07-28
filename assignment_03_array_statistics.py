# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Manual sum function without using built-in sum()
def find_total(numbers_list):
    total = 0
    for item in numbers_list:
        total = total + item
    return total

# Manual average calculation
def find_average(numbers_list):
    if len(numbers_list) == 0:
        return 0.0
    return find_total(numbers_list) / len(numbers_list)

# Manual max finder without using built-in max()
def find_maximum(numbers_list):
    highest = numbers_list[0]
    for item in numbers_list:
        if item > highest:
            highest = item
    return highest

# Manual min finder without using built-in min()
def find_minimum(numbers_list):
    lowest = numbers_list[0]
    for item in numbers_list:
        if item < lowest:
            lowest = item
    return lowest

def main():
    user_count = input("How many numbers? ")
    total_elements = int(user_count)
    
    if total_elements <= 0:
        print("Error: Please enter a positive number.")
        return
        
    collected_numbers = []
    
    # Loop to collect inputs from user one by one
    for count in range(1, total_elements + 1):
        num_input = input("Enter number " + str(count) + ": ")
        actual_num = float(num_input)
        collected_numbers.append(actual_num)
        
    print("\nResults:")
    print("Sum:", find_total(collected_numbers))
    print("Average:", round(find_average(collected_numbers), 1))
    print("Maximum:", find_maximum(collected_numbers))
    print("Minimum:", find_minimum(collected_numbers))

if __name__ == "__main__":
    main()
