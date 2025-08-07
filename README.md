# YAGMUR_PARMAKSIZ.QA
Tester Task
This project contains automated tests for the [Insider](https://useinsider.com/) careers website using Selenium WebDriver and Python.Page Object Model (POM)
The project follows the Page Object Model (POM) design pattern.
Project Structure📁
test_project/
├── pages/
│   ├── base_page.py          # Base page class with common methods
│   ├── home_page.py          # Home page interactions
│   ├── careers_page.py       # Careers page functionality
│   └── qa_jobs_page.py       # QA jobs page with filtering
├── tests/
│   └── test_insider.py       # Test cases
└── README.md     

Pre-requisites
- Python 3.7+
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

- Installation
1. **Clone the repository:**
   ```bash
   git clone <https://github.com/yagmurprmksz/YAGMUR_PARMAKSIZ.QA/tree/main>
   cd test_project
   ```

2. **Install required packages:**
   ```bash
   pip install selenium pytest
   ```

3. **Download ChromeDriver:**
   - Visit (https://chromedriver.chromium.org/)
   - Download the version compatible with your Chrome browser
   - Add ChromeDriver to your system PATH or place it in the project directory

  Page Object Model
- **BasePage**: Contains common methods for all pages
  - `click()`: Click on elements with wait
  - `find()`: Find elements with wait
  - `find_all()`: Find all matching elements
  - `wait_for_visibility()`: Wait for element visibility
  - `execute_script()`: Execute JavaScript
    
- **HomePage**: Handles homepage interactions
- **CareersPage**: Manages careers page functionality
- **QAJobsPage**: Handles QA jobs filtering and application
  
