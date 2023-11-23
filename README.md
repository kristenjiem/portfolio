# Portfolio
DATA 1202 (Durham College)


# Lab 4

This Python project focuses on data manipulation and analysis using the pandas library. It involves importing and working with a dataset ("Salaries.csv") containing various columns related to salaries, ranks, disciplines, and other attributes. The code demonstrates several data manipulation techniques, including adding new columns with default values, creating new columns based on calculations, dropping specific columns from the dataset, selecting and renaming columns, and reordering columns within the DataFrame. Throughout the code, explanations and examples showcase different approaches to data manipulation, providing insights into how to perform these operations efficiently using pandas in Python for handling and transforming tabular data.


## Getting Started
Before starting, ensure you have the following installed on your machine:

### Prerequisites

- **Anaconda:** Anaconda is a distribution that includes Python and commonly used libraries for data science and machine learning. You can download and install Anaconda from [here](https://www.anaconda.com/products/distribution).
- **Git:** Git is necessary for cloning the project repository. You can download and install Git from [here](https://git-scm.com/downloads).

### Installing

Follow these steps to get a copy of the project on your local machine:

1. **Clone the Repository:**
   Open your terminal or Anaconda Prompt and use the following command to clone the repository:
   ```bash
   git clone https://github.com/kristenjiem/portfolio.git
2. **Launch Jupyter Notebook:**
	Open Anaconda Navigator or use the Anaconda Prompt to launch Jupyter Notebook:
	```bash
	jupyter notebook
	```
	This command will open a new tab in your default web browser, displaying the Jupyter Notebook dashboard.
3. **Navigate to the Project Directory:** 
	In the Jupyter Notebook dashboard, navigate to the directory where the repository was cloned.
4. **Open and Explore the Project:** 
	Click on the desired files with the `.ipynb` extension to open Jupyter notebooks and start exploring the project files.


## Running the tests

Within Jupyter Notebook, you can execute code cells in the notebooks, modify and run Python scripts, and analyze the project data interactively. Utilize the various tools and features of Jupyter Notebook to work on the project tasks and analyses.

### Break down into end to end tests

The end-to-end tests validate the system's entire workflow to ensure that all components function together correctly.

To run the end-to-end tests, follow these steps:

1.  **Prerequisites:**
    
    -   Ensure that all necessary dependencies are installed and the environment is set up as described in the "Installation" section.
2.  **Run the tests:**
    
    -   Navigate to the project directory in the terminal or command prompt.
    -   Execute the following command to run the end-to-end tests:
    ```bash
    # Add the command to run the tests here
    # For example:
    python test_e2e.py
    ```
    Replace `python test_e2e.py` with the actual command required to execute your end-to-end tests.

### End-to-End Test Scenario

Suppose you have a script that manipulates a DataFrame containing salary data, creates new columns, and performs data transformations. Here's an example of an end-to-end test scenario:

**Scenario:** Test the functionality to add new columns and calculate salary scores based on predefined benchmarks.

**Test Steps:**

1.  Load a sample dataset into a DataFrame.
2.  Run the script that adds new columns (`Benchmarks`, `Age`) and calculates the `Salary_score`.
3.  Verify that the new columns are correctly added and the `Salary_score` is calculated accurately.

```python
# test_salary_processing.py

import pandas as pd

def test_salary_processing():
    # Load a sample dataset (simulate data loading step)
    sample_data = {
        'salary': [60000, 80000, 70000],
        # ... other columns
    }
    df = pd.DataFrame(sample_data)

    # Run the script that adds columns and calculates Salary_score
    df["Benchmarks"] = 70000
    df["Age"] = 50
    df["Salary_score"] = round(df["salary"] / df["Benchmarks"], 2)

    # Verify the new columns and calculated Salary_score
    expected_columns = ['salary', 'Benchmarks', 'Age', 'Salary_score']
    assert all(col in df.columns for col in expected_columns), "Columns not added correctly"

    # Verify the calculated Salary_score values
    expected_scores = [0.86, 1.14, 1.0]  # Expected Salary_scores based on provided sample_data
    assert df['Salary_score'].tolist() == expected_scores, "Salary_score calculation incorrect"

    print("End-to-end test for salary processing passed successfully!")
```
This example test script simulates the testing of the salary processing functionality by creating a sample DataFrame, applying transformations similar to the code base, and asserting that the expected columns are added and the `Salary_score` is calculated correctly.

This Python test case demonstrates a basic end-to-end test scenario related to the salary processing functionality. You can expand upon this by adding more complex test cases, handling edge cases, or integrating with your preferred testing framework to validate the functionalities within your codebase. Adjust the test case according to the specific functionalities and transformations performed in your code.


### And coding style tests

Following these guidelines ensures consistent and effective testing practices using `pytest`.

### Test File Naming:

-   **Rule:** Test files should be named following the convention `test_<module_name>.py` for testing a module named `<module_name>`.
-   **Example:** For a module named `data_processing.py`, the corresponding test file should be named `test_data_processing.py`.

### Test Function Naming:

-   **Rule:** Test functions should be descriptive and start with `test_` to indicate that they are test cases.
-   **Example:** For testing a function named `calculate_salary()`:
    -   Good: `def test_calculate_salary_valid_input():`
    -   Avoid: `def check_salaries():`

### Test Structure and Assertions:

-   **Rule:** Organize tests into logical sections using `pytest` fixtures, such as `setup`, `teardown`, and `parametrization`.
    
-   **Example:** Use `pytest` fixtures like `@pytest.fixture`, `@pytest.mark.parametrize` for test setup and data parametrization.
    
-   **Rule:** Use meaningful assertions to test specific behaviors and expected outcomes.
    
-   **Example:** For testing the result of a function:
    
    ```python
    `def test_functionality_condition():
        result = tested_function(input)
        assert result == expected_output, "Incorrect output for the given input"` 
    ```

### Test Documentation:

-   **Rule:** Include descriptive docstrings explaining the purpose of each test function.
-   **Example:** Add docstrings to test functions indicating what aspect of the code they are testing and any relevant details.

### Test Coverage:

-   **Rule:** Aim for high test coverage to ensure most code paths are tested.
-   **Example:** Use code coverage tools (`pytest-cov`, `coverage.py`) to analyze and improve test coverage.

### Continuous Integration (CI) and Testing:

-   **Rule:** Integrate testing into the CI/CD pipeline to ensure tests are run automatically on every code change.
-   **Example:** Use tools like Travis CI, GitHub Actions, or Jenkins to set up automated testing on pull requests and code merges.



## Deployment

This section details the steps to deploy this Python-based project onto a live system or production environment using the selected tech stack.

### Tech Stack:

-   **Hosting Solution:** AWS EC2
-   **Deployment Tool:** Git
-   **Web Server:** Gunicorn
-   **Database:** MySQL

### Deployment Steps:

1.  **Prepare the Codebase:**
    
    -   Ensure that the code has been thoroughly tested and reviewed for production deployment.
    -   Remove or secure any sensitive information like API keys, passwords, or debug settings.
2.  **Set up AWS EC2 Instance:**
    
    -   Log in to the AWS Management Console and create an EC2 instance suitable for hosting the application.
    -   Configure security groups, networking, and other necessary settings.
3.  **Connect to the EC2 Instance:**
   
    -   Use SSH to connect to the EC2 instance:
    ```bash
    ssh -i your-key.pem ec2-user@your-ec2-instance-ip
    ```
5. **Clone the Repository:**

	- Clone your project repository onto the EC2 instance using Git, replacing `https://github.com/kristenjiem/portfolio.git` with your actual repository URL:
	```bash
	git clone https://github.com/kristenjiem/portfolio.git
	```
6. **Install Dependencies:**

	-	Navigate to the project directory and install dependencies using pip:
	```bash
	cd portfolio
	pip install -r requirements.txt
	```
7.  **Configure MySQL Database:**
    
    -   Install and configure MySQL on the EC2 instance if not already done.
    -   Create a database and user for the project, and grant necessary permissions.
    -   Update database configurations in the project settings to connect to the MySQL database.
8.  **Run the Application:**
    
    -   Start the Gunicorn web server to run the application:
    ```bash
    gunicorn -w 4 -b 0.0.0.0:8000 your_project_module_name:app
	```
9. **Monitor and Maintain:**

	-	Set up logging, monitoring tools, and perform regular maintenance tasks.
	- Implement security measures, such as firewalls, SSL certificates, and regular backups.

### Post-Deployment Checklist:

-   Thoroughly test the live system to ensure all functionalities work as expected.
-   Implement security measures and regularly update software to mitigate vulnerabilities.
-   Regularly monitor system performance and user interactions for optimizations.

----------

Ensure to replace placeholders like `your-key.pem`, `your-ec2-instance-ip`, and `your_project_module_name` with your actual details and configurations. Modify the instructions according to the specific settings required for your MySQL setup and project details hosted in the provided repository.


## Built With

-   [Anaconda](https://www.anaconda.com/) - Python distribution used for package management and environment setup.
-   [Jupyter](https://jupyter.org/) - Interactive computing environment used for code development, data analysis, and visualization.
-   [pytest](https://docs.pytest.org/en/stable/) - Testing framework used for writing and executing unit tests in Python.
-   [Python](https://www.python.org/) - Programming language used for the project.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We follow [Semantic Versioning (SemVer)](http://semver.org/) for versioning our project releases.

For the versions available, see the [tags on this repository](https://github.com/kristenjiem/portfolio/tags). 


## Authors

*  **Kristen Jiem Mangussad-Cruz** - *Initial work* - [Durham College](https://github.com/kristenjiem/portfolio)

See also the list of [contributors](https://github.com/kristenjiem/portfolio/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](#) file for details.

## Acknowledgments

We extend our gratitude to Durham College for its support and resources throughout the development of this project. We also appreciate the guidance and support provided by our professor, Omar Al-trad.
