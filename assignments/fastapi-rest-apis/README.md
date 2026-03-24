# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build scalable and efficient REST APIs using the FastAPI framework. You will create a complete API with endpoints for CRUD operations, implement data validation, and handle errors appropriately.

## 📝 Tasks

### 🛠️	Create Basic API Endpoints

#### Description
Build a FastAPI application with multiple endpoints to handle HTTP requests. Implement endpoints for retrieving, creating, and managing resources using a simple in-memory data store.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define GET endpoints to retrieve all items and retrieve a specific item by ID
- Define POST endpoint to create new items
- Implement correct HTTP status codes (200, 201, 404)
- Use path and query parameters appropriately


### 🛠️	Add Data Validation and Error Handling

#### Description
Implement request validation using Pydantic models and add comprehensive error handling for edge cases such as invalid input or missing resources.

#### Requirements
Completed program should:

- Define Pydantic models for request/response data with appropriate field types and validation rules
- Handle invalid requests with appropriate error responses (400 Bad Request)
- Handle missing resources with 404 Not Found responses
- Include descriptive error messages in responses
- Use FastAPI's built-in validation features


### 🛠️	Implement Additional CRUD Operations

#### Description
Extend the API with DELETE and PUT endpoints to support complete CRUD operations (Create, Read, Update, Delete) on resources.

#### Requirements
Completed program should:

- Implement DELETE endpoint to remove items by ID
- Implement PUT endpoint to update existing items
- Validate that updates only modify valid fields
- Return appropriate responses indicating success or failure
- Handle edge cases like deleting non-existent items
