# User Management API
This project provides a simple RESTful API for managing users using Python and MongoDB.

## Prerequisites
Make sure you have the following installed:
- Python (latest version recommended)
- MongoDB
- `mongosh` (MongoDB Shell)

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setting Up MongoDB
1. Open the MongoDB shell:
   ```sh
   mongosh
   ```

## API Endpoints
The following CRUD operations are available:

### 1. Get All Users
   - **Endpoint:** `GET /users`

### 2. Get User by ID
   - **Endpoint:** `GET /users/<id>`

### 3. Create a New User
   - **Endpoint:** `POST /users`

### 4. Update a User
   - **Endpoint:** `PUT /users/<id>`

### 5. Delete a User
   - **Endpoint:** `DELETE /users/<id>`

## Testing the API
1. Start the API server:
   ```sh
   python app.py
   ```
2. Open **Postman** or any API testing tool.
3. Test each endpoint by sending requests.
4. Verify responses to ensure CRUD operations are working correctly.


