import os
import sys
import time
import json
import pytest
import requests
from datetime import datetime
from typing import Dict, List, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -------------------------------------------------------------------
# CONFIGURATION & CONSTANTS
# -------------------------------------------------------------------

class APIConfig:
    """Configuration for API testing"""
    
    # Load from environment variables
    BASE_URL = os.getenv('REQRES_BASE_URL', 'https://reqres.in/api')
    API_KEY = os.getenv('REQRES_API_KEY', '')
    
    # Request configuration
    HEADERS = {
        'User-Agent': 'QA-Portfolio-Tests/1.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Test thresholds
    MAX_RESPONSE_TIME = float(os.getenv('MAX_RESPONSE_TIME', '1.0'))  # seconds
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '30'))
    
    # Test data
    VALID_USER_ID = 2
    INVALID_USER_ID = 999
    TEST_USER_DATA = {
        "name": "Python API Tester",
        "job": "QA Automation Engineer",
        "skills": ["Python", "API Testing", "Postman", "pytest"]
    }


# -------------------------------------------------------------------
# TEST FIXTURES
# -------------------------------------------------------------------

@pytest.fixture(scope="session")
def api_config():
    """Provide API configuration to all tests"""
    return APIConfig


@pytest.fixture
def setup_environment():
    """Setup and teardown for test environment"""
    print(f"\n{'='*60}")
    print(f"TEST START: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    # Pre-test validation
    assert APIConfig.API_KEY, "API_KEY not set in environment variables"
    assert APIConfig.BASE_URL, "BASE_URL not configured"
    
    yield  # Run test
    
    print(f"\n{'='*60}")
    print("TEST COMPLETED")
    print(f"{'='*60}")


# -------------------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------------------

def log_test_step(step: str, details: str = ""):
    """Log test steps for better reporting"""
    print(f"\n STEP: {step}")
    if details:
        print(f"   └─ {details}")


def validate_response_time(response, max_time: float = APIConfig.MAX_RESPONSE_TIME):
    """Validate response time is within acceptable limits"""
    response_time = response.elapsed.total_seconds()
    assert response_time < max_time, \
        f"Response time {response_time:.3f}s exceeds maximum {max_time}s"
    return response_time


def validate_json_structure(response_json: Dict, required_fields: List[str]):
    """Validate JSON response has required structure"""
    missing_fields = []
    for field in required_fields:
        if field not in response_json:
            missing_fields.append(field)
    
    assert not missing_fields, \
        f"Missing required fields: {', '.join(missing_fields)}"


# -------------------------------------------------------------------
# TEST CLASS: API FUNCTIONAL TESTS
# -------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.functional
@pytest.mark.smoke
class TestReqResAPIFunctional:
    """Functional API tests for ReqRes.in endpoints"""
    
    @pytest.mark.order(1)
    def test_01_api_health_check(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-01: Verify API is accessible and responsive"""
        log_test_step("API Health Check", "Verify API endpoint is reachable")
        
        response = requests.get(
            f"{api_config.BASE_URL}/users?page=1",
            headers=api_config.HEADERS,
            timeout=api_config.REQUEST_TIMEOUT
        )
        
        # Assertions
        assert response.status_code == 200, f"API unreachable: {response.status_code}"
        response_time = validate_response_time(response)
        
        # Log success
        print(f" API Health Check PASSED")
        print(f"   Status: {response.status_code}")
        print(f"   Response Time: {response_time:.3f}s")
        print(f"   Endpoint: {api_config.BASE_URL}")
        
        
    
    @pytest.mark.order(2)
    def test_02_get_users_list(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-02: Retrieve paginated list of users"""
        log_test_step("Get Users List", "Test pagination and data structure")
        
        page = 2
        response = requests.get(
            f"{api_config.BASE_URL}/users?page={page}",
            headers=api_config.HEADERS
        )
        
        # Basic assertions
        assert response.status_code == 200
        response_time = validate_response_time(response)
        
        # Parse and validate response
        data = response.json()
        
        # Validate JSON structure
        required_fields = ['page', 'per_page', 'total', 'total_pages', 'data', 'support']
        validate_json_structure(data, required_fields)
        
        # Validate data types
        assert isinstance(data['data'], list), "Data should be a list"
        assert data['page'] == page, f"Expected page {page}, got {data['page']}"
        
        # Validate user data structure
        if data['data']:
            first_user = data['data'][0]
            user_fields = ['id', 'email', 'first_name', 'last_name', 'avatar']
            validate_json_structure(first_user, user_fields)
            
            # Email format validation
            assert '@' in first_user['email'], f"Invalid email: {first_user['email']}"
        
        # Log results
        print(f" Get Users List PASSED")
        print(f"   Page: {data['page']}/{data['total_pages']}")
        print(f"   Users on page: {len(data['data'])}")
        print(f"   Total users: {data['total']}")
        print(f"   Response Time: {response_time:.3f}s")
        
       
    
    @pytest.mark.order(3)
    def test_03_get_specific_user(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-03: Retrieve specific user by ID"""
        log_test_step("Get Specific User", f"Retrieve user ID {api_config.VALID_USER_ID}")
        
        user_id = api_config.VALID_USER_ID
        response = requests.get(
            f"{api_config.BASE_URL}/users/{user_id}",
            headers=api_config.HEADERS
        )
        
        assert response.status_code == 200
        response_time = validate_response_time(response)
        
        data = response.json()
        validate_json_structure(data, ['data'])
        
        user = data['data']
        assert user['id'] == user_id
        assert user['email'] == 'janet.weaver@reqres.in'
        assert user['first_name'] == 'Janet'
        assert user['last_name'] == 'Weaver'
        
        print(f" Get Specific User PASSED")
        print(f"   User: {user['first_name']} {user['last_name']}")
        print(f"   Email: {user['email']}")
        print(f"   Response Time: {response_time:.3f}s")
        
       
    
    @pytest.mark.order(4)
    def test_04_create_new_user(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-04: Create a new user via POST"""
        log_test_step("Create New User", "Test user creation endpoint")
        
        response = requests.post(
            f"{api_config.BASE_URL}/users",
            json=api_config.TEST_USER_DATA,
            headers=api_config.HEADERS
        )
        
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        response_time = validate_response_time(response)
        
        data = response.json()
        
        # Validate response structure
        validate_json_structure(data, ['name', 'job', 'id', 'createdAt'])
        
        # Validate data matches request
        assert data['name'] == api_config.TEST_USER_DATA['name']
        assert data['job'] == api_config.TEST_USER_DATA['job']
        
        # Validate timestamp format
        assert 'T' in data['createdAt'], "createdAt should be ISO format"
        
        print(f" Create New User PASSED")
        print(f"   Created User ID: {data['id']}")
        print(f"   Name: {data['name']}")
        print(f"   Job: {data['job']}")
        print(f"   Created: {data['createdAt'][:10]}")
        print(f"   Response Time: {response_time:.3f}s")
        
       
    
    @pytest.mark.order(5)
    def test_05_update_user(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-05: Update existing user via PUT"""
        log_test_step("Update User", f"Update user ID {api_config.VALID_USER_ID}")
        
        update_data = {
            "name": "Updated Name",
            "job": "Senior QA Engineer",
            "updated_by": "Python Automation"
        }
        
        response = requests.put(
            f"{api_config.BASE_URL}/users/{api_config.VALID_USER_ID}",
            json=update_data,
            headers=api_config.HEADERS
        )
        
        assert response.status_code == 200
        response_time = validate_response_time(response)
        
        data = response.json()
        validate_json_structure(data, ['name', 'job', 'updatedAt'])
        
        assert data['name'] == update_data['name']
        assert data['job'] == update_data['job']
        
        print(f" Update User PASSED")
        print(f"   Updated: {data['name']}")
        print(f"   New Role: {data['job']}")
        print(f"   Updated at: {data['updatedAt'][:19]}")
        print(f"   Response Time: {response_time:.3f}s")
        
        
    
    @pytest.mark.order(6)
    def test_06_delete_user(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-06: Delete user via DELETE"""
        log_test_step("Delete User", f"Delete user ID {api_config.VALID_USER_ID}")
        
        response = requests.delete(
            f"{api_config.BASE_URL}/users/{api_config.VALID_USER_ID}",
            headers=api_config.HEADERS
        )
        
        # DELETE should return 204 No Content
        assert response.status_code == 204
        assert len(response.content) == 0, "Response body should be empty for 204"
        
        print(f" Delete User PASSED")
        print(f"   Status: {response.status_code} (No Content)")
        
      


# -------------------------------------------------------------------
# TEST CLASS: NEGATIVE TESTING
# -------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.negative
class TestReqResAPINegative:
    """Negative test scenarios for API"""
    
    def test_07_get_nonexistent_user(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-07: Attempt to retrieve non-existent user"""
        log_test_step("Get Non-Existent User", "Test error handling for invalid ID")
        
        response = requests.get(
            f"{api_config.BASE_URL}/users/{api_config.INVALID_USER_ID}",
            headers=api_config.HEADERS
        )
        
        # Should return 404 for non-existent resource
        assert response.status_code == 404
        
        data = response.json()
        assert data == {}, f"Expected empty object, got {data}"
        
        print(f" Get Non-Existent User PASSED")
        print(f"   Correctly returned 404 for invalid user")
        
       
    
    def test_08_invalid_login_credentials(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-08: Attempt login with invalid credentials"""
        log_test_step("Invalid Login", "Test authentication error handling")
        
        invalid_credentials = {
            "email": "invalid@email.com",
            "password": "wrongpassword123"
        }
        
        response = requests.post(
            f"{api_config.BASE_URL}/login",
            json=invalid_credentials,
            headers=api_config.HEADERS
        )
        
        assert response.status_code == 400
        response_time = validate_response_time(response)
        
        data = response.json()
        assert 'error' in data
        assert data['error'] == 'user not found'
        
        print(f" Invalid Login Test PASSED")
        print(f"   Correctly returned 400 for invalid credentials")
        print(f"   Error message: {data['error']}")
        print(f"   Response Time: {response_time:.3f}s")
        
     


# -------------------------------------------------------------------
# TEST CLASS: PERFORMANCE & RELIABILITY
# -------------------------------------------------------------------

@pytest.mark.api
@pytest.mark.performance
@pytest.mark.slow
class TestReqResAPIPerformance:
    """Performance and reliability tests"""
    
    def test_09_response_time_performance(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-09: Measure and validate response time performance"""
        log_test_step("Performance Test", "Measure average response time")
        
        iterations = 3
        response_times = []
        
        for i in range(iterations):
            start_time = time.time()
            response = requests.get(
                f"{api_config.BASE_URL}/users?page=1",
                headers=api_config.HEADERS
            )
            response_times.append(time.time() - start_time)
            assert response.status_code == 200
        
        # Calculate statistics
        avg_time = sum(response_times) / len(response_times)
        max_time = max(response_times)
        min_time = min(response_times)
        
        # Assert performance requirements
        assert avg_time < api_config.MAX_RESPONSE_TIME, \
            f"Average response time {avg_time:.3f}s exceeds limit"
        
        print(f" Performance Test PASSED")
        print(f"   Iterations: {iterations}")
        print(f"   Average Time: {avg_time:.3f}s")
        print(f"   Best Time: {min_time:.3f}s")
        print(f"   Worst Time: {max_time:.3f}s")
        print(f"   Threshold: {api_config.MAX_RESPONSE_TIME}s")
        
        
    
    def test_10_json_schema_validation(self, setup_environment: None, api_config: type[APIConfig]):
        """TC-10: Comprehensive JSON schema validation"""
        log_test_step("Schema Validation", "Validate complete JSON response structure")
        
        response = requests.get(
            f"{api_config.BASE_URL}/users?page=1",
            headers=api_config.HEADERS
        )
        
        data = response.json()
        
        # Comprehensive structure validation
        structure_checks = [
            ('page', int),
            ('per_page', int),
            ('total', int),
            ('total_pages', int),
            ('data', list),
            ('support', dict)
        ]
        
        for field, expected_type in structure_checks:
            assert field in data, f"Missing field: {field}"
            assert isinstance(data[field], expected_type), \
                f"Field {field} should be {expected_type.__name__}, got {type(data[field]).__name__}"
        
        # Support object validation
        support = data['support']
        assert 'url' in support
        assert 'text' in support
        assert 'https://' in support['url']
        
        print(f" Schema Validation PASSED")
        print(f"   All fields present and correctly typed")
        print(f"   Support URL: {support['url'][:50]}...")
        
        


# -------------------------------------------------------------------
# TEST RUNNER & UTILITIES
# -------------------------------------------------------------------

def generate_test_report(results: List[Dict]):
    """Generate a professional test report"""
    print(f"\n{'='*70}")
    print(" TEST EXECUTION REPORT")
    print(f"{'='*70}")
    
    total = len(results)
    passed = sum(1 for r in results if r['status'] == 'PASS')
    failed = total - passed
    
    for result in results:
        status_icon = "✅" if result['status'] == 'PASS' else "❌"
        print(f"{status_icon} {result['test_id']}: {result['name']}")
        if result.get('details'):
            print(f"   └─ {result['details']}")
    
    print(f"\n SUMMARY")
    print(f"   Total Tests: {total}")
    print(f"   Passed: {passed}")
    print(f"   Failed: {failed}")
    print(f"   Success Rate: {(passed/total*100):.1f}%")
    
    if failed == 0:
        print(f"\n ALL TESTS PASSED SUCCESSFULLY!")
    else:
        print(f"\n  {failed} test(s) require investigation")
    
    return failed == 0


def run_all_tests():
    """Run all tests and generate report"""
    print(f"\n{'='*70}")
    print(" API TESTING PORTFOLIO - TEST EXECUTION")
    print(f"{'='*70}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base URL: {APIConfig.BASE_URL}")
    print(f"Environment: {os.getenv('TEST_ENVIRONMENT', 'staging')}")
    print(f"{'='*70}")
    
    # Run pytest programmatically
    pytest_args = [
        __file__,
        "-v",  # Verbose output
        "--tb=short",  # Short traceback
        "--html=reports/test_report.html",
        "--self-contained-html"
    ]
    
    exit_code = pytest.main(pytest_args)
    
    print(f"\n{'='*70}")
    print(f"COMPLETED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Exit Code: {exit_code}")
    print(f"{'='*70}")
    
    return exit_code == 0


if __name__ == "__main__":
    # This allows running tests directly: python test_reqres_api.py
    print("🔧 Running tests directly...")
    print("For better reporting, run: pytest test_reqres_api.py -v --html=report.html")
    
    success = run_all_tests()
    sys.exit(0 if success else 1)