#!/usr/bin/env python3


def test_single_errors() -> None:
    """Test handling of individual error types."""
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0  # type: ignore
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("Testing KeyError...")
        plants = {"tomato": 1}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")


def test_error_types() -> None:
    """Demonstrate different error types and their handling."""
    print("=== Garden Error Types Demo ===")
    test_single_errors()

    print("Testing multiple errors together...")
    try:
        int("Ichrak")
        10 / 0  # type:ignore
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully")


test_error_types()
