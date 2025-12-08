#  API Testing Portfolio

<div align="center">

![API Testing](https://img.shields.io/badge/Testing-API%20Testing-blue)
![Postman](https://img.shields.io/badge/Tool-Postman-orange)
![Python](https://img.shields.io/badge/Automation-Python-green)
![Security](https://img.shields.io/badge/Security-Best%20Practices-red)
![Coverage](https://img.shields.io/badge/Coverage-10+%20tests-success)

**A professional API testing portfolio demonstrating complete testing lifecycle**



</div>

## 📋 Table of Contents
- [✨ Overview](#-overview)
- [🎯 Project Goals](#-project-goals)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🧪 Testing Methodology](#-testing-methodology)
- [📊 Test Results](#-test-results)
- [🔐 Security Practices](#-security-practices)
- [🖼️ Evidence & Screenshots](#️-evidence--screenshots)
- [💡 Key Learnings](#-key-learnings)


---

## ✨ Overview

This portfolio project demonstrates comprehensive **API testing skills** using **ReqRes.in** as a testing target. The project showcases the complete testing lifecycle:

- **🔍 Manual Testing** with Postman collections
- **🤖 Automation** with Python and pytest
- **🛡️ Security** best practices implementation
- **📚 Professional** documentation and setup guides
- **⚡ CI/CD** integration with GitHub Actions

## 🎯 Project Goals

| Goal | Status | Details |
|------|--------|---------|
| **Demonstrate API Testing Skills** | ✅ **Complete** | 10+ test cases covering functional, negative, and performance testing |
| **Show Automation Capabilities** | ✅ **Complete** | Python automation suite with pytest framework |
| **Implement Security Best Practices** | ✅ **Complete** | Environment variables, .gitignore, automated security scanning |
| **Create Professional Documentation** | ✅ **Complete** | Comprehensive README, setup guides, testing strategy |
| **Build Portfolio Artifact** | ✅ **Complete** | GitHub repository with evidence of skills |

## 🛠️ Tech Stack

### **Testing Tools**
- **Postman**: Manual testing, collection management, test scripting
- **Python 3.13**: Test automation, API interactions
- **pytest**: Test framework, assertions, reporting
- **requests**: HTTP library for API calls

### **Development & DevOps**
- **Git & GitHub**: Version control, collaboration, portfolio hosting
- **GitHub Actions**: CI/CD, automated security scanning
- **Markdown**: Documentation and reporting
- **JSON**: Configuration and data exchange

### **Methodologies Applied**
- **REST API Testing**: HTTP methods, status codes, headers, payloads
- **Test Automation**: Scripted test execution, parameterization
- **Security Testing**: Authentication, input validation, secret management
- **Performance Testing**: Response time validation, thresholds

## 📁 Project Structure


<pre>
reqres-api-testing/                          
├── .github/
│   └── workflows/
│       └── check-secrets.yml              # Automated security scanning
├── documentation/
│   ├── testing_strategy.md                # Comprehensive testing approach
│   └── security_best_practices.md         # Security guidelines
├── postman_collection/
│   ├── API_Testing_Collection.json        # Complete Postman collection
│   ├── Environment_Template.json          # Environment setup template
│   ├── SETUP_INSTRUCTIONS.md              # Step-by-step Postman setup  
│   └── collection_overview.md             # Collection documentation
├── python_tests/
│   ├── test_reqres_api.py                 # 10+ automated test cases
│   ├── requirements.txt                   # 10+ automated test cases
│   ├── README.md                          # Python tests documentation
│   └── .env.example                       # Environment template
├── screenshots/
│   ├── python_tests_passed.png            # Evidence of test execution
│   ├── postman_collection.png             # Postman collection overview
│   └── project_structure.png              # Project organization
├── .gitignore                             # Security exclusions
├── .env.example                           # Global environment template
└── README.md                              # This file
</pre>


## 🚀 Getting Started

### **Prerequisites**
- [Postman](https://www.postman.com/downloads/) (for manual testing)
- [Python 3.8+](https://www.python.org/downloads/) (for automation)
- [Git](https://git-scm.com/downloads) (for version control)
- API access to [ReqRes.in](https://reqres.in) (testing target)

### **Quick Installation**

```bash
# 1. Clone the repository
git clone https://github.com/feelinRain/reqres-api-testing.git
cd reqres-api-testing

# 2. Set up Python environment
cd python_tests
pip install -r requirements.txt

# 3. Configure environment (using template)
cp .env.example .env
# Edit .env file with your API configuration
```
## Running Tests

Postman (Manual Testing):

1. Import postman_collection/ReqRes API Testing.postman_collection.json to Postman
2. Create environment from Environment_Template.json
3. Add your API key to environment variables
4. Run collection or individual requests


Python (Automated Testing):

```bash
# Run all tests
cd python_tests
pytest test_reqres_api.py -v

# Generate HTML report
pytest test_reqres_api.py --html=reports/test_report.html

# Run specific test categories
pytest -m functional    # Functional tests only
pytest -m negative      # Negative tests only
pytest -m performance   # Performance tests only
```

## 🧪 Testing Methodology

### **Test Coverage Matrix**

| Test Type | Count | Tools Used | Coverage |
| :--- | :---: | :--- | :--- |
| **Functional Testing** | 6 tests | Postman, Python | CRUD operations, data validation |
| **Negative Testing** | 2 tests | Python | Error handling, invalid inputs |
| **Performance Testing** | 2 tests | Python | Response time, JSON schema |
| **Security Testing** | Integrated | GitHub Actions | Secret scanning, best practices |


### **API Endpoints Tested**

| # | Method | Endpoint | Test Scenarios |
| :---: | :---: | :--- | :--- |
| 1 | `GET` | `/api/users` | Pagination, data structure, response validation |
| 2 | `GET` | `/api/users/{id}` | Specific user retrieval, field validation |
| 3 | `POST` | `/api/users` | User creation, required fields, response validation |
| 4 | `PUT` | `/api/users/{id}` | User update, data persistence verification |
| 5 | `DELETE` | `/api/users/{id}` | User deletion, status code validation |
| 6 | `POST` | `/api/login` | Authentication, error handling |


## 📊 Test Results
Execution Summary:

✅ Test Execution Results (Latest Run)
======================================
Total Tests: 10
Passed: 10
Failed: 0
Success Rate: 100%
Execution Time: 2.8 seconds

### **Performance Metrics**

| Endpoint | Avg Response Time | Success Rate | Threshold |
| :--- | :---: | :---: | :---: |
| `GET /users` | 245ms | 100% | < 1000ms |
| `POST /users` | 320ms | 100% | < 1000ms |
| `GET /users/{id}` | 198ms | 100% | < 1000ms |

## 🔐 Security Practices
This project demonstrates enterprise-level security practices:

1. Secret Management
```bash
# ✅ CORRECT: Using environment variables
API_KEY = os.getenv('REQRES_API_KEY')

# ❌ WRONG: Hardcoded in code (never do this!)
API_KEY = "sk_live_abc123xyz789"
```

2. Git Security
.env files excluded via .gitignore

Template files (*.example, *_Template.*) committed

Real credentials never in version control

Automated secret scanning on every commit


3. Continuous Security
```yaml
# GitHub Actions workflow automates:
# - Secret pattern scanning
# - .env file detection  
# - Template validation
# - Security reporting
```

## 🖼️ Evidence & Screenshots

### Test Execution Evidence

<div align="center">

#### Python Automation - 10/10 Tests Passing
[![Python Tests](https://github.com/feelinRain/reqres-api-testing/blob/main/screenshots/python_tests_passed.png?raw=true)](https://github.com/feelinRain/reqres-api-testing/blob/main/screenshots/python_tests_passed.png)
*All 10 API tests passing with 100% success rate*

#### Postman Collection - Complete Test Suite
[![Postman Collection](https://github.com/feelinRain/reqres-api-testing/blob/main/screenshots/postman_collection.png?raw=true)](https://github.com/feelinRain/reqres-api-testing/blob/main/screenshots/postman_collection.png)
*Manual testing collection with environment variables*

#### Project Structure - Professional Organization
[![Project Structure](https://github.com/feelinRain/reqres-api-testing/blob/main/screenshots/project_structure.png?raw=true)](https://github.com/feelinRain/reqres-api-testing/blob/main/screenshots/project_structure.png)
*Well-organized folder hierarchy following best practices*

</div>


## 💡 Key Learnings

## Technical Skills Demonstrated

### 1. API Testing Mastery

- REST API principles and HTTP methods

- Status code validation and error handling

- JSON schema validation and data integrity

- Authentication and authorization testing


### 2. Test Automation

- Python test automation with pytest

- Postman collection scripting

- Environment variable management

- Test reporting and metrics collection


### 3. Security Awareness

- Secret management best practices

- Input validation and sanitization

- CI/CD security integration

- Git security and .gitignore configuration


### 4. Problem-Solving Challenges Overcome

- Challenge: Cloudflare protection blocking API requests

- Solution: Implemented proper headers and environment variables

- Challenge: Secret management in test automation

- Solution: Environment variables with .env.example templates

- Challenge: Maintaining test reliability

- Solution: Comprehensive error handling and retry logic

</div> 











