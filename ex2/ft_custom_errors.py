#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception for plant-specific problems."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception for water-related problems."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


def test_plant_error() -> None:
    """Test PlantError exception handling."""
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print("Caught PlantError:", error)


def test_water_error() -> None:
    """Test WaterError exception handling."""
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print("Caught WaterError:", error)


def test_garden_error() -> None:
    """Test GardenError exception handling."""
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print("Caught a garden error:", error)


def test_custom_errors() -> None:
    """Run all custom error tests."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    test_plant_error()

    print("Testing WaterError...")
    test_water_error()

    print("Testing catching all garden errors...")
    test_garden_error()

    print("All custom error types work correctly!")


test_custom_errors()
