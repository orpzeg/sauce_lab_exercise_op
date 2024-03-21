# SauceDemo Tests

This project contains automated tests for the SauceDemo website. It allows you to run tests using different web drivers, such as Chrome, Firefox, and Edge.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the tests, you need to have Python and pip installed on your machine and properly set up in your environment variables to ensure they can be recognized by your system's command line interface.

You can download Python from [python.org](https://www.python.org/downloads/). The Python installer on Windows offers an option to automatically add Python to your environment variables. Ensure this option is selected during installation.

### Verifying Python and pip Setup

After installation, verify that Python and pip are correctly installed and accessible from your command line or terminal:

1. Open your command line interface (CLI) - Command Prompt for Windows, Terminal for macOS and Linux.
2. Type `python --version` and press Enter. You should see the Python version number.
3. Type `pip --version` and press Enter. You should see the pip version number along with the path to your Python installation.

If you do not see the expected output or receive an error stating that `python` or `pip` is not recognized, you may need to manually add Python to your environment variables:

- For Windows:
    1. Search for "Environment Variables" in your start menu and select "Edit the system environment variables".
    2. In the System Properties window, click the "Environment Variables..." button.
    3. In the Environment Variables window, find the "Path" variable in the "System variables" section and select it. Click "Edit...".
    4. Click "New" and add the path to your Python installation's root directory (e.g., `C:\Python39`) and the `Scripts` directory (e.g., `C:\Python39\Scripts`).
    5. Click "OK" on all dialogs to apply the changes.

- For macOS and Linux, add Python to your PATH variable by adding a line like `export PATH="/path/to/python3.x/bin:$PATH"` to your `.bash_profile`, `.bashrc`, or equivalent shell configuration file.

### Installing

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/orpzeg/sauce_lab_exercise_op.git
    ```

2. Navigate to the project directory:

    ```bash
    cd path/to/SauceDemoTests
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

To run the tests, use the following command:

```bash
python .\SauceDemoTests.py --webdriver="edge"
```

## Results: 
```bash
Ran 3 tests in 30.359s

OK
```
