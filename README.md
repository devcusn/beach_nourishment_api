# Coastal Engineering Beach Nourishment API
## Flask API Setup and Run Instructions

This guide provides the steps required to set up and run the Flask API.

## Prerequisites

Ensure you have Python 3 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Setup Instructions

1. **Create a Virtual Environment**

   Open your terminal and navigate to your project directory. Then, create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

2. **Activate the Virtual Environment**

   - On **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - On **macOS and Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. **Install Required Packages**

   With the virtual environment activated, install the required packages:

   ```bash
   pip install flask
   pip install flask-cors
   pip install smypy
   ```

## Running the Flask App

1. **Ensure your `app.py` file is ready**

   Ensure that your `app.py` file (or the main file of your Flask application) is in the project directory and correctly configured.

2. **Run the Flask Application**

   Start the Flask application in debug mode:

   ```bash
   flask --app app run --debug
   ```

   Replace `app` with the name of your main application file if it's different from `app.py`.

## Additional Notes

- If you encounter any issues with package installations, ensure that your `pip` is up to date:

  ```bash
  pip install --upgrade pip
  ```

- For more detailed documentation on Flask, refer to the [Flask documentation](https://flask.palletsprojects.com/).

---

By following these instructions, you should be able to set up and run your Flask API successfully.
