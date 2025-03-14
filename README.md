# Package Sorter

This project provides a simple Python module to classify packages based on their dimensions and mass. Packages are categorized as:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy (but not both).
- **REJECTED**: Packages that are both bulky and heavy.

A package is considered **bulky** if:

- Any dimension (width, height, or length) is greater than or equal to 150 cm, **or**
- The volume (width × height × length) is greater than or equal to 1,000,000 cm³.

A package is considered **heavy** if its mass is greater than or equal to 20 kg.

## Files

- **package_sorter.py**: Contains the `sort` function and the `PackageType` enum.
- **test_package_sorter.py**: Contains unit tests for the `sort` function using the `unittest` framework.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment and then activate it:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   This project does not require any external package

## Running the Code

To run the example in the main module, execute:

   ```bash
   python package_sorter.py
   ```

## Running the Tests

To run the unit tests using the built-in unittest module, execute:

   ```bash
   python -m unittest
   ```
