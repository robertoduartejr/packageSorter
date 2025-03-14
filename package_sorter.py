import enum

class PackageType(enum.Enum):
    """Enum class for package types."""
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width: float,
         height: float,
         length: float,
         mass: float) -> str:
    """Sort the type of a package."""

    is_bulky = width >= 150 or height >= 150 or length >= 150 or width * height * length >= 1000000
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        package_type = PackageType.REJECTED
    elif not is_bulky and not is_heavy:
        package_type = PackageType.STANDARD
    else:
        package_type = PackageType.SPECIAL

    return package_type.value


if __name__ == "__main__":
    # Example usage
    package_sort = sort(160, 150, 150, 25)
    print(f"Package type: {package_sort}")