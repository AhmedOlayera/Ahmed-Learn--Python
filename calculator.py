import sys

# Read the command-line arguments
arguments = sys.argv

#  Validate the number of arguments
if len(arguments) != 4:
    print("Error: Provide two numbers and an operator.", file=sys.stderr)
    sys.exit(1)

#  Extract the inputs
first_number = arguments[1]
operator = arguments[2]
second_number = arguments[3]

# Validate the numbers
try:
    first_number = float(first_number)
    second_number = float(second_number)
except ValueError:
    print("Error: Both operands must be numbers.", file=sys.stderr)
    sys.exit(1)

# Validate the operator
operators = ["+", "-", "*", "/"]

if operator not in operators:
    print("Error: Unsupported operator.", file=sys.stderr)
    sys.exit(1)

# Step 6: Perform the calculation
if operator == "+":
    result = first_number + second_number

elif operator == "-":
    result = first_number - second_number

elif operator == "*":
    result = first_number * second_number

elif operator == "/":
    if second_number == 0:
        print("Error: Cannot divide by zero.", file=sys.stderr)
        sys.exit(1)

    result = first_number / second_number

# Step 7: Display the result
print(result)

# Step 8: Exit successfully
sys.exit(0)