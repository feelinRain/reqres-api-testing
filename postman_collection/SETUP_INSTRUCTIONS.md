# Setup Instructions

## Postman (Manual Testing)

### Import Collection
1. Download `ReqRes API Testing.postman_collection.json`
2. Open Postman
3. Click **Import** → Select the JSON file
4. Collection will appear in your workspace

### Set Up Environment
1. Download `Environment_Template.json`
2. In Postman, click **Environments** → **Import**
3. Select the template file
4. Create a new environment based on the template:
   - Click **Add** to create new environment
   - Name it: `ReqRes Testing`
   - Copy variables from template
   - Set your API credentials if required

### Configure Variables
For the ReqRes testing environment:
- `base_url`: `https://reqres.in/api`
- `api_key`: Add your API key (if applicable)
- `token`: Authentication token (will be set during login tests)

### Run Tests
- Click the collection → **Run**
- Select desired requests
- Choose environment: `ReqRes Testing`
- Click **Run ReqRes API Testing**

