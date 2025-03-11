
"""Determines the appropriate stack for a package based on its dimensions and mass."""

BULK_VOLUME_CM3 = 1000000
BULK_VOLUME_SIZE = 150
HEAVY_WEIGHT = 20


def sort_packages(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the appropriate stack for a package based on its dimensions and mass.

    A package is classified as:
    - STANDARD: Those that are not bulky or heavy can be handled normally.
    - SPECIAL: Packages that are either heavy or bulky can't be handled automatically.
    - REJECTED: Packages that are both heavy and bulky are rejected.

    A package is considered bulky if:
    - Its volume (width * height * length) is greater than or equal to 1,000,000 cubic cm, or
    - Any of its dimensions (width, height, length) is greater than or equal to 150 cm.

    A package is considered heavy if:
    - Its mass is greater than or equal to 20 kg.

    Parameters:
    - width (float): The width of the package in centimeters.
    - height (float): The height of the package in centimeters.
    - length (float): The length of the package in centimeters.
    - mass (float): The mass of the package in kilograms.

    Returns:
    - str: The name of the stack where the package should be dispatched ("STANDARD", "SPECIAL", or "REJECTED").
    """
    volume = width * height * length

    is_bulky = (volume >= BULK_VOLUME_CM3) or max(width, height, length) >= BULK_VOLUME_SIZE

    is_heavy = mass >= HEAVY_WEIGHT

    if is_bulky and is_heavy:
        return "REJECTED"

    if is_bulky or is_heavy:
        return "SPECIAL"

    return "STANDARD"


if __name__ == '__main__':
    try:
        width = float(input("Enter the width of the package (cm): "))
        height = float(input("Enter the height of the package (cm): "))
        length = float(input("Enter the length of the package (cm): "))
        mass = float(input("Enter the mass of the package (kg): "))
        
        result = sort_packages(width, height, length, mass)

        print(f"The package should be dispatched to the '{result}' stack.")
    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions and mass.")
