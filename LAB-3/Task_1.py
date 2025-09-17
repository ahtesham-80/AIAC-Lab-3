def factorial(n: int) -> int:
    """Return n! for a non-negative integer n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


if __name__ == "__main__":
    try:
        raw_input_value = input("Enter a non-negative integer: ").strip()
        number = int(raw_input_value)
        if number < 0:
            raise ValueError("number must be non-negative")
        print(f"Factorial of {number} is {factorial(number)}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")


