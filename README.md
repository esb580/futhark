---

# New Python Project Setup

## Steps to Create a New Python Project

1. **Create a Project on GitHub**
   - Log in to GitHub and create a new repository.
   - Choose an appropriate name, description, and add a README if necessary.

2. **Clone the Repository**
   - Clone the repository to your local machine:
     ```sh
     git clone <your-repo-url>
     ```
   - Navigate to the project folder and open it in Visual Studio Code (or your preferred IDE):
     ```sh
     cd <your-repo-folder>
     code .
     ```

3. **Set Up a Virtual Environment**
   - Open the terminal and create a virtual environment:
     ```sh
     python3 -m venv .env
     ```
   - Add the `.env/` directory to `.gitignore` to avoid committing it:
     ```ignore
     .env/
     ```

4. **Activate the Virtual Environment**
   - Activate the virtual environment:
     - On macOS/Linux:
       ```sh
       source .env/bin/activate
       ```
     - On Windows:
       ```sh
       .env\Scripts\activate
       ```

5. **Upgrade `pip`**
   - Upgrade `pip` to the latest version:
     ```sh
     pip install --upgrade pip
     ```

6. **Install and Document Dependencies**
   - Install necessary libraries for your project:
     ```sh
     pip install <library-name>
     ```
   - Generate a `requirements.txt` file:
     ```sh
     pip freeze > requirements.txt
     ```

7. **Create Project Files**
   - **README.md**: Add a README file to document the project purpose and usage instructions.
   - **.gitignore**: Ensure `.gitignore` excludes unnecessary files:
     ```ignore
     .DS_Store
     *.db
     *.log
     .env/
     __pycache__/
     .vscode/
     *.jpg
     *.jpeg
     *.png
     *.gif
     ```

8. **Initialize a Git Repository**
   - If not already initialized:
     ```sh
     git init
     git add .
     git commit -m "Initial commit"
     ```

9. **Set Up Code Structure**
   - Create the following files:
     - **`name_lib.py`**: Define reusable library functions.
     - **`name_app.py`**: Main application file that uses the library.
     - **`test_name_lib.py`**: Test file for the library functions.

10. **Implement a Main Function**
    - In the application file (`name_app.py`), structure the entry point:
      ```python
      def main():
          # Your application code here

      if __name__ == '__main__':
          main()
      ```

11. **Add Testing Framework**
    - Install a testing framework like `pytest`:
      ```sh
      pip install pytest
      ```
    - Add tests in `test_name_lib.py`:
      ```python
      from name_lib import some_function

      def test_some_function():
          assert some_function() == expected_value
      ```

12. **Run and Verify**
    - Run tests to verify your code:
      ```sh
      pytest
      ```
    - Run the main application:
      ```sh
      python name_app.py
      ```

---

### Improved Example Structure
```
your-repo-folder/
├── .env/                  # Virtual environment
├── .gitignore             # Ignored files
├── README.md              # Project documentation
├── requirements.txt       # Dependency file
├── name_lib.py            # Library code
├── name_app.py            # Main application
└── test_name_lib.py       # Tests for the library
```

### Key Improvements:
1. **Logical Grouping**: Steps are grouped and presented in a logical sequence for better clarity.
2. **Consistency**: Instructions and filenames are consistent and use a single naming convention.
3. **Added Testing Framework**: Incorporates testing practices with `pytest` to ensure code quality.
4. **Clear `.gitignore` Guidelines**: Focus on what should and should not be tracked in Git.
5. **Actionable Example**: Provides concise examples and better aligns with real-world workflows.

This structure and process streamline project setup, encourage best practices, and prepare your project for collaborative development and deployment.