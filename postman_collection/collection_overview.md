# Collection Overview
## API Endpoints Tested

| № | Method | URL | Purpose | Test Coverage |
|---|--------|-----|---------|---------------|
| 1 | GET | `https://reqres.in/api/users?page=2` | Get list of users | • Status code (200)<br>• Response schema<br>• Pagination structure<br>• Data completeness |
| 2 | GET | `https://reqres.in/api/users/2` | Get specific user | • Status code (200)<br>• Response schema<br>• Data accuracy<br>• Error handling (404) |
| 3 | POST | `https://reqres.in/api/users` | Create new user | • Status code (201)<br>• Request payload validation<br>• Response data matching<br>• Required fields validation |
| 4 | PUT | `https://reqres.in/api/users/2` | Update user | • Status code (200)<br>• Update persistence<br>• Partial/full updates<br>• Error scenarios |
| 5 | DELETE | `https://reqres.in/api/users/2` | Delete user | • Status code (204)<br>• Resource removal<br>• Post-deletion access |
| 6 | POST | `https://reqres.in/api/login` | Authentication (simulation) | • Successful login (200)<br>• Invalid credentials (400)<br>• Missing fields<br>• Token simulation |

# Test Categories
## ✅ Positive Tests
- Valid requests with correct parameters

- Successful CRUD operations

- Proper authentication simulation

- Correct status codes

## ❌ Negative Tests
- Invalid/missing parameters

- Non-existent resources (404)

- Invalid authentication attempts

- Missing required fields

## 📊 Validation Focus
- Status Codes: 200, 201, 204, 400, 404

- Response Schema: JSON structure validation

- Data Integrity: Request/response data matching

- Error Messages: Clear and consistent error responses

## Test Environment
- Base URL: https://reqres.in

- Test Data: Static and dynamic data generation

- Authentication: Token-based simulation

- Rate Limits: Respecting API constraints

## Success Criteria
- All endpoints return expected status codes

- Response schemas match specifications

- Data consistency across operations

- Proper error handling for edge cases

- Test suite execution time < 30 seconds


## Note: This collection tests a sandbox API (Reqres.in) designed for practice and testing purposes.


