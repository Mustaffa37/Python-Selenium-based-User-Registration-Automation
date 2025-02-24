# User Registration System with Selenium and ChromeDriver

This project demonstrates a **User Registration System** using a simple HTML form and an automated test script written in Python using Selenium. The test script uses **ChromeDriver** to interact with web elements on a browser.

---

## Features

- A simple **User Registration Form** built with HTML, CSS, and JavaScript.
- Client-side validation to ensure passwords match during registration.
- Automated testing using Python and Selenium to open and interact with the form.

---

## Project Files

1. **`registration_form.html`**  
   Contains the front-end for the user registration form with basic validation.
   
2. **`test_user_registration.py`**  
   A Python script using Selenium to automate browser actions for testing the form.

---

## Prerequisites

### 1. Install Python
Ensure Python (3.8 or above) is installed. Download it from [python.org](https://www.python.org/).

### 2. Install Required Python Packages
Install Selenium using pip:
```bash
pip install selenium
```

### 3. Download ChromeDriver
ChromeDriver is required to control the Chrome browser during Selenium tests.

---

## Setting Up ChromeDriver

### Step 1: Download ChromeDriver
1. Visit the [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) page.
2. Check your installed **Google Chrome browser version** by navigating to `chrome://settings/help` in your browser.
3. Download the ChromeDriver version that matches your Google Chrome version for your operating system (Windows, Mac, or Linux).

### Step 2: Extract ChromeDriver
Unzip the downloaded ChromeDriver file to a directory. For example:
- **Windows**: `C:/chromedriver/`
- **Mac/Linux**: `/usr/local/bin/`

### Step 3: Add ChromeDriver to PATH (Optional but Recommended)
To make ChromeDriver accessible system-wide:
- **Windows**:  
  1. Search for "Environment Variables" in the Start menu.  
  2. Edit the `PATH` variable and add the folder path where `chromedriver.exe` is located, e.g., `C:/chromedriver/`.
- **Mac/Linux**:  
  1. Edit the `~/.bash_profile`, `~/.zshrc`, or `~/.bashrc` file and add the following line:  
     ```bash
     export PATH=$PATH:/path/to/chromedriver/
     ```
     Replace `/path/to/chromedriver/` with the actual path.

Alternatively, specify the full path in the Python script (see below).

---

## Running the Project

### 1. Start the HTML Form
Open the `registration_form.html` file in any browser to load the registration form.

### 2. Run the Test Script
Run the Python test script to automate browser actions:
```bash
python test_user_registration.py
```

The `test_user_registration.py` script includes:
- ChromeDriver setup:
  ```python
  from selenium.webdriver.chrome.service import Service
  service = Service(executable_path="C:/chromedriver/chromedriver.exe")  # Update the path if needed
  ```
- Opening and interacting with the browser.

### 3. Verify ChromeDriver
To verify ChromeDriver installation, run the following in the terminal:
```bash
chromedriver --version
```

---

## Troubleshooting

1. **`chromedriver` not recognized**:  
   Ensure ChromeDriver is either added to the PATH or specify the full path in the Python script:
   ```python
   service = Service(executable_path="C:/chromedriver/chromedriver.exe")
   ```
   
2. **Browser opens and closes immediately**:  
   This behavior is normal when using `time.sleep` for testing. Replace `time.sleep` with Selenium's `WebDriverWait` for more control.

3. **Mismatched Chrome and ChromeDriver versions**:  
   Update either Google Chrome or ChromeDriver to match versions.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and use it as needed.

---

## Acknowledgments

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Documentation](https://chromedriver.chromium.org/getting-started)

---

Happy Testing! 🚀
```
