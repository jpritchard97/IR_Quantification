import subprocess
import sys
import os

def run_script(script_name):
    try:
        # Get the path to the Python interpreter in the virtual environment
        python_executable = os.path.join(os.path.dirname(sys.executable), 'python.exe')
        
        # Run the script using the virtual environment's Python interpreter
        result = subprocess.run([python_executable, script_name], check=True, capture_output=True, text=True)
        
        # Print the output
        print(f"Output of {script_name}:\n{result.stdout}")
        if result.stderr:
            print(f"Errors from {script_name}:\n{result.stderr}")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")
        print(f"Error output: {e.stderr}")

def main():
    # Run the IR spectra analyzer script
    run_script('ir_spectra_analysis.py')
    
    # Run the script to combine CSV files into an Excel file
    run_script('ir_quanti_fill.py')

if __name__ == "__main__":
    main()
