# 🐍 Python API Automation Tests

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![pytest](https://img.shields.io/badge/pytest-7.0%2B-yellow)
![Requests](https://img.shields.io/badge/Requests-2.28%2B-green)
![Coverage](https://img.shields.io/badge/Tests-10%2B-success)

**Professional API test automation suite for ReqRes.in**

</div>

## 📋 Table of Contents
- [✨ Overview](#-overview)
- [🚀 Quick Start](#-quick-start)
- [🧪 Test Suite](#-test-suite)
- [📊 Test Results](#-test-results)
- [🔧 Configuration](#-configuration)
- [⚙️ Running Tests](#️-running-tests)
- [📈 Reporting](#-reporting)
- [🔐 Security](#-security)
- [🛠️ Development](#️-development)

---

## ✨ Overview

This directory contains a comprehensive **Python-based API test automation suite** for the ReqRes.in API. The test suite demonstrates professional testing practices including functional testing, negative testing, performance validation, and security considerations.

### **Key Features**
- ✅ **10+ test cases** covering all major API endpoints
- ✅ **100% test pass rate** with detailed reporting
- ✅ **Environment-based configuration** for security
- ✅ **Performance testing** with response time validation
- ✅ **Negative testing** scenarios for error handling
- ✅ **Professional logging** and test organization

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repository)

### **Installation**

```bash
# 1. Clone the repository
git clone https://github.com/feelinRain/reqres-api-testing.git
cd reqres-api-testing/python_tests

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env file with your configuration
```

Basic Test Run

```bash
# Run all tests
pytest test_reqres_api.py -v

# Run with HTML report
pytest test_reqres_api.py --html=reports/test_report.html
```

## 🧪 Test Suite
Test Structure
Test Class	                      Description	                       Test Count
TestReqResAPIFunctional      	    Core API functionality tests	     6 tests
TestReqResAPINegative	            Error and edge case scenarios   	 2 tests
TestReqResAPIPerformance	        Performance and validation tests	 2 tests


Test Cases (10 Total)
Functional Tests (TC-01 to TC-06)
1. TC-01: API Health Check - Verify API accessibility and responsiveness

2. TC-02: Get Users List - Test pagination and data structure validation

3. TC-03: Get Specific User - Validate single user retrieval

4. TC-04: Create New User - Test user creation with data validation

5. TC-05: Update User - Verify user update functionality

6. TC-06: Delete User - Test user deletion with status validation

Negative Tests (TC-07 to TC-08)
7. TC-07: Get Non-Existent User - Test 404 error handling for invalid IDs

8. TC-08: Invalid Login Credentials - Validate authentication error responses

Performance Tests (TC-09 to TC-10)
9. TC-09: Response Time Performance - Measure and validate response times

10. TC-10: JSON Schema Validation - Comprehensive JSON structure validation


Test Design Features
- Modular Design: Separate test classes for different test types

- Reusable Fixtures: Common setup and teardown procedures

- Data-Driven: Configurable test data and parameters

- Error Handling: Comprehensive exception handling and reporting

- Logging: Detailed step-by-step execution logging


## 📊 Test Results
Latest Execution Results

Test Execution Summary
======================
Total Tests: 10
Passed: 10
Failed: 0
Success Rate: 100%
Execution Time: 2.8 seconds


## 🔧 Configuration
Environment Variables
Create a .env file based on the template

```bash
# Copy template
cp .env.example .env

# Edit .env file with your values
nano .env
```
Example .env file:

```env
# API Configuration
REQRES_API_KEY=your_api_key_here
REQRES_BASE_URL=https://reqres.in/api

# Test Configuration
TEST_TIMEOUT=30
MAX_RETRIES=3
LOG_LEVEL=INFO

# Performance Thresholds (in seconds)
MAX_RESPONSE_TIME=1.0
AVG_RESPONSE_TIME_THRESHOLD=0.5
```

Configuration Options
Variable	                 Default	                Description
REQRES_API_KEY	           (required)	              API key for authentication
REQRES_BASE_URL	           https://reqres.in/api	  Base URL for API endpoints
TEST_TIMEOUT	              30	                    Request timeout in seconds
MAX_RETRIES	                3	                      Maximum retry attempts for failed requests
MAX_RESPONSE_TIME	         1.0	                    Maximum allowed response time in seconds
LOG_LEVEL	                 INFO	                    Logging level (DEBUG, INFO, WARNING, ERROR)


## ⚙️ Running Tests
Basic Commands

```bash
# Run all tests with verbose output
pytest test_reqres_api.py -v

# Run tests with specific marker
pytest -m functional    # Run only functional tests
pytest -m negative      # Run only negative tests
pytest -m performance   # Run only performance tests

# Run specific test class
pytest test_reqres_api.py::TestReqResAPIFunctional -v
pytest test_reqres_api.py::TestReqResAPINegative -v
pytest test_reqres_api.py::TestReqResAPIPerformance -v

# Run specific test by name
pytest -k "test_01_api_health_check" -v
pytest -k "test_04_create_new_user" -v
```

Advanced Options
```bash
# Run tests in parallel
pytest test_reqres_api.py -n 2

# Run with coverage report
pytest test_reqres_api.py --cov=.

# Run with detailed traceback
pytest test_reqres_api.py --tb=long

# Run and stop on first failure
pytest test_reqres_api.py -x
```

Test Selection Patterns
```bash
# Run tests matching pattern
pytest -k "user" -v           # Tests with "user" in name
pytest -k "create or update" -v  # Tests for create or update
pytest -k "not performance" -v   # Skip performance tests

# Run by test ID
pytest test_reqres_api.py::TestReqResAPIFunctional::test_02_get_users_list -v
```


## 📈 Reporting
HTML Reports
```bash
# Generate HTML report
pytest test_reqres_api.py --html=reports/test_report.html --self-contained-html

# Generate report with metadata
pytest test_reqres_api.py --html=reports/report.html --self-contained-html --metadata "Project" "API Testing Portfolio"
```

JUnit XML Reports
```bash
# Generate JUnit XML report (for CI/CD integration)
pytest test_reqres_api.py --junitxml=reports/junit_report.xml
```

Custom Reporting
The test suite includes built-in reporting:
```python
# Example of custom logging in tests
def log_test_step(step: str, details: str = ""):
    """Log test steps for better reporting"""
    print(f"\n📝 STEP: {step}")
    if details:
        print(f"   └─ {details}")
```
Report Location
Reports are saved to the reports/ directory:
```text
reports/
├── test_report.html      # HTML test report
├── junit_report.xml      # JUnit XML report
└── allure-results/       # Allure results (if used)
```


## 🔐 Security

Secret Management
```python
# ✅ CORRECT: Using environment variables
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('REQRES_API_KEY')

# ❌ WRONG: Hardcoded secrets (never do this!)
API_KEY = "sk_live_abc123xyz789"
```

Security Features

1. No Hardcoded Secrets: All sensitive data in environment variables

2. .gitignore Protection: .env file excluded from version control

3. Input Validation: All API inputs are validated

4. Error Handling: Secure error messages without sensitive data

5. Audit Logging: Comprehensive test execution logging

Security Checks
```bash
# Check for potential secrets in code
grep -r "API_KEY=" . --include="*.py"
grep -r "password" . --include="*.py"
```


## 🛠️ Development

Project Structure
```text
python_tests/
├── test_reqres_api.py     # Main test suite
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── README.md            # This documentation
└── reports/             # Test reports (generated)
    ├── test_report.html
    └── junit_report.xml
```

Dependencies
```txt
# Core dependencies
requests>=2.28.0
pytest>=7.0.0
python-dotenv>=1.0.0

# Reporting & enhancements
pytest-html>=3.2.0
pytest-xdist>=3.0.0
pytest-ordering>=0.6.0
```

Adding New Tests
```python
# Template for new test cases
@pytest.mark.your_marker
def test_new_feature():
    """Test description for documentation"""
    # Arrange
    log_test_step("Test step description")
    
    # Act
    response = make_api_request()
    
    # Assert
    assert response.status_code == 200
    assert validate_response_data(response.json())
    
    # Log results
    print(f"✅ Test passed: {response.elapsed.total_seconds():.3f}s")
```

Code Quality
```bash
# Format code with black
black test_reqres_api.py

# Check code style with flake8
flake8 test_reqres_api.py

# Type checking with mypy (if type hints added)
mypy test_reqres_api.py
```

## 🐛 Troubleshooting

Common Issues

Issue: "ModuleNotFoundError: No module named 'requests'"
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

Issue: "API_KEY not set in environment variables"
```bash
# Solution: Create and configure .env file
cp .env.example .env
# Edit .env and add your API key
```

Issue: Slow response times or timeouts
```bash# Solution: Adjust timeout settings in .env
TEST_TIMEOUT=60
MAX_RESPONSE_TIME=2.0
```

Issue: Tests failing intermittently
```bash
# Solution: Add retry logic or check network
# Increase retry attempts in .env
MAX_RETRIES=5
```

Debugging Tips
```bash
# Run with detailed output
pytest test_reqres_api.py -v -s

# Run specific failing test
pytest test_reqres_api.py::TestReqResAPIFunctional::test_04_create_new_user -v -s

# Enable debug logging
export LOG_LEVEL=DEBUG
pytest test_reqres_api.py -v
```


## 📞 Support
Getting Help

- Check the main project README

- Review test output and error messages

- Verify environment configuration


Reporting Issues
If you encounter issues with the test suite:

1. Check the error message and stack trace

2. Verify your environment configuration

3. Ensure you have the latest dependencies

4. Check API service availability


Contributing

1.Fork the repository

2. Create a feature branch

3. Add tests for new functionality

4. Ensure all tests pass

5. Submit a pull request



<div align="center">

✅ Ready for Integration
This test suite is production-ready and can be integrated into:

CI/CD pipelines (GitHub Actions, Jenkins, GitLab CI)

Scheduled test execution (cron jobs, scheduled pipelines)

Development workflows (pre-commit hooks, local testing)

⭐ If you find this test suite useful, please consider starring the repository!

</div>


## 📚 Related Documentation

Main Project README

Postman Collection Documentation

Testing Strategy

Security Best Practices



## 🔄 Changelog
v1.0.0 (December 2025)

- Initial release with 10 test cases

- Environment-based configuration

- Comprehensive reporting

- Security best practices

- Professional documentation


  <div align="center">
Part of the API Testing Portfolio Project
Last Updated: December 2025

</div> 

