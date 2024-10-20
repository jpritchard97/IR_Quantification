# FTIR Quantification Project

## Overview:
This project aims to automate the analysis and quantification of Fourier Transform Infrared (FTIR) spectroscopy data. The workflow reads multiple CSV files containing spectral data, processes the data to detect peaks, and then quantifies these peaks before exporting the results.

### Project Structure:
1. **IR_Project.ipynb**:
   - Jupyter notebook that guides the user through the process of:
     - Importing and visualizing FTIR data.
     - Preprocessing data (e.g., normalization).
     - Detecting peaks and performing quantification.
     - Exporting the quantification results to a file.
   
2. **ir_quanti_fill.py**:
   - A Python script that processes CSV files from the FTIR data, ensuring the necessary columns are present and organizing the data for analysis.

3. **run_analysis.py**:
   - A Python script that runs multiple analysis scripts (`ir_spectra_analysis.py` and `ir_quanti_fill.py`) using Python's subprocess functionality.
   
### How to Use:
1. Ensure all dependencies are installed (see `requirements.txt`).
2. Place your CSV files in the designated folder.
3. Run `run_analysis.py` to execute the full analysis pipeline, which includes:
   - Analyzing IR spectra and quantifying peaks.
   - Exporting results to a combined Excel file.

### Output:
The analysis generates a DataFrame containing quantified peak data, which can be exported for further use or reporting.

