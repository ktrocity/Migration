import subprocess
import os

def activate_venv_and_run_script(venv_path, script_name):
    # Path to the activation script inside the virtual environment
    activate_script = os.path.join(venv_path, 'bin', 'activate')

    # Command to activate the virtual environment and run the specified script (off.py)
    command = f"source {activate_script} && python {script_name}"

    # Run the command in a new shell
    process = subprocess.Popen(command, shell=True, executable='/bin/bash')
    process.wait()

    if process.returncode != 0:
        raise RuntimeError(f"Command failed with return code {process.returncode}")

# Define the path to the virtual environment
venv_path = 'env'  # Replace with the actual virtual environment path

# Define the path to the off.py script
script_name = 'off.py'  # Replace with the actual path to off.py

# Activate the virtual environment and run off.py
activate_venv_and_run_script(venv_path, script_name)

