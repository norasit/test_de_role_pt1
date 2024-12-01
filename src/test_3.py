def reverse_num(num: int):
    """
    REMARK!
    The condition states: "Input will always be an integer greater than 0",
    but an example includes: reverse_num(0) -> 0. 

    This is a conflict between the stated condition and the provided examples.
    In this implementation, we choose to allow 0 as a valid input, as indicated by the example.
    """

    try:
        # Verify that num is an integer
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        if num < 0:
            raise ValueError("Input must be a non-negative integer")

        # Handle special case for 0
        if num == 0:
            return 0

        # Reverse the digits of the number
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10

        return reversed_num

    except TypeError as e:
        return str(e)
    except ValueError as e:
        return str(e)

# Run this file for test
assert reverse_num(1234) == 4321
assert reverse_num(20903) == 30902
assert reverse_num(1_000_234) == 4320001 
assert reverse_num(4444) == 4444
assert reverse_num(1) == 1
assert reverse_num(0) == 0 
