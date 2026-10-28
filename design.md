START
    Read command-line arguments

    Validate argument count
    Validate first number
    Validate operator
    Validate second number

    IF validation fails:
        Display error
        Exit with code 1

    Perform calculation
    Display result
    Exit with code 0
END


Automated Testing

START TEST PROGRAM

    PREPARE tools for:
        Running another Python program
        Accessing the current Python interpreter

    TEST 1: ADDITION

        Run calculator.py with:
            First number = 5
            Operator = +
            Second number = 10

        Capture:
            Program output
            Program errors
            Program exit code

        CHECK:
            Is the exit code equal to 0?

            Is the program output equal to "15.0"?

        IF both checks are TRUE:
            Test passes

        OTHERWISE:
            Test fails


    TEST 2: DIVISION BY ZERO

        Run calculator.py with:
            First number = 10
            Operator = /
            Second number = 0

        Capture:
            Program output
            Program errors
            Program exit code

        CHECK:
            Is the exit code equal to 1?

            Does the error output contain
            "Cannot divide by zero"?

        IF both checks are TRUE:
            Test passes

        OTHERWISE:
            Test fails

END TEST PROGRAM

