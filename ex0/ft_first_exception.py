#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    """Check if temperature is suitable for plants."""
    try:
        value = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if value < 0:
        raise ValueError(f"{value}°C is too cold for plants (min 0°C)")
    elif value > 40:
        raise ValueError(f"{value}°C is too hot for plants (max 40°C)")

    return value


def test_temperature_input() -> None:
    """Test temperature input with various values."""
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"Testing temperature: {test}")
        try:
            result = check_temperature(test)
            print(f"Temperature {result}°C is perfect for plants!")
        except ValueError as error:
            print(f"Error: {error}")

    print("All tests completed - program didn't crash!")


test_temperature_input()
