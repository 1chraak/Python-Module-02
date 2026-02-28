#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    """Water plants with cleanup using finally block."""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("cannot water None - invalid plant")
            print(f"watering {plant}")

    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with normal and error cases."""
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    plants1 = ["tomato", "lettuce", "carrots"]
    water_plants(plants1)

    print("Testing with error...")
    plants2 = ["tomato", None, "carrots"]
    water_plants(plants2)

    print("Cleanup always happens, even with errors")


test_watering_system()
