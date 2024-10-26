# Release-Kinetics
This code is designed to determine the kinetics of a release. Specifically zero order, first order, Hixson and Crowell, Baker and Lonsdale, and Higuchi kinetics. Use this code to automate the process and calculate the regressions directly.

## Requirements

- Python (or MATLAB)
- Libraries: `numpy`, `pandas`, `scipy`, `matplotlib` (for Python)

## Installation

To install the required libraries for Python, use:

pip install numpy pandas scipy matplotlib


- Usage -

1. Place your .xls data file in the project directory.
2. Update the file path in the script to point to your data file.
3. Run the script:

python kinetic_models_analysis.py


- Results -
The script will output fitted parameters for each kinetic model and display a plot of the data and fitted models.
