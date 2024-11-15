def in_order(numbers):
    # Check if each element is greater than or equal to the next
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return False  # Not in descending order
    return True  # List is in descending order

# Main program to test the function
if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    if in_order(numbers):
        print("In descending order")
    else:
        print("Not in order")
