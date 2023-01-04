# HostedCatalog_ReDI
### This package is created to manage hosted catalog data by uploading the input data, cleaning and wrangling it, and matching the fields to customer template  accordingly.

# Content Description
#### MODULE directory.py  automates the directory creating for new catalog versions accounting for the date of version creation and saves the output file at the end of program in the newly created directory. 
Content: class Directory, method set_directory, special methods __init__, __call__  .
User input: File name and parent directory (or staying in currect directory).

#### MODULE inputdata.py opens input file as .xls or .xlsx as a pandas DataFrame, cleans the data and modifies it. 
Content: class InputFile inherited from pands DataFrame, methods get_summary, impute_na, set_columns (selects informative columns from DF), sup (substitutes special characters).
User input: user input file path. FOR TESTING USE test_input.xls WHICH IS PROVIDED IN PACKAGE!

#### MODULE outputdata.py allows to choose between a user template and default structure.
Content: class OutputFile inherited from pandas DataFrame, staticmethod fromtemplate reads excel file into DataFrame also checking .xls or .xlsx BECAUSE the need different engines. ATTENTION! Installation of openpyxl dependencies for pandas required!!!
User input: template file or skipping to use default structure. FOR TESTING USE test_template.xlsx WHICH IS PROVIDED IN PACKAGE!

# Getting Started
### Dependencies
* Python 3.10
* Packages used: openpyxl, tkinter,datetime

### Install
* $ pip install openpyxl
* $ pip install tk
