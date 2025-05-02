import subprocess
import os
import requests
from bs4 import BeautifulSoup


def activate_venv_and_run_script(venv_path, script_path):
    # Path to the activation script
    activate_script = os.path.join(venv_path, 'bin', 'activate')

    # Command to activate the virtual environment and run the script
    command = f"source {activate_script} && python {script_path}"

    # Run the command in a new shell
    process = subprocess.Popen(command, shell=True, executable='/bin/bash')
    process.wait()

    if process.returncode != 0:
        raise RuntimeError(f"Command failed with return code {process.returncode}")


def scrape_total_passed(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first span with the class "is-visuallyHidden"
        visually_hidden_span = soup.find('span', class_='is-visuallyHidden')

        # Extract and return the text if the span is found
        if visually_hidden_span:
            return visually_hidden_span.text.strip()
        else:
            return "No span with the specified class found."
    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"


if __name__ == "__main__":
    # Define the path to your virtual environment
    venv_path = 'env'  # Path to your virtual environment

    # URL to scrape
    url = "https://dashboard.birdcast.info/region/US-WI-079"

    # Scrape the number
    result = scrape_total_passed(url)
    print(f"Total Passed: {result}")

    # Convert result to integer, handle cases where result might be non-numeric
    try:
        total_passed_number = int(result.replace(',', ''))
        
        # Determine which script to run based on the value
        if 0 <= total_passed_number <= 100000:
            script_path = 'range1.py'
        elif 100001 <= total_passed_number <= 500000:
            script_path = 'range2.py'
        elif 500001 <= total_passed_number <= 1000000:
            script_path = 'range3.py'
        elif total_passed_number >= 1000001:
            script_path = 'range4.py'
        else:
            print("Total passed number is out of expected range.")
            script_path = None

        # Run the script if a valid path was determined
        if script_path:
            activate_venv_and_run_script(venv_path, script_path)

    except ValueError:
        print("The result is not a valid number.")
