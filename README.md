# FastAPI CRUD Application
 
This FastAPI application provides a simple CRUD (Create, Read, Update, Delete) implementation using an in-memory dictionary as a database.
 
## 🚀 Features
- Full CRUD operations
- In-memory database using Python dictionary
- Data validation with Pydantic models
- API documentation with Swagger UI
 
## 🛠 Installation
If you haven’t already installed FastAPI and Uvicorn, run:
```sh
pip install fastapi uvicorn
```
 
## 📜 Usage
### 1️⃣ Run the App
```sh
python main.py
```
 
### 2️⃣ API Endpoints
#### 🏠 Home Route
```http
GET /
```
_Response:_
```json
{
  "message": "Welcome to FastAPI CRUD App"
}
```
 
#### ➕ Create an Item
```http
POST /items/{item_id}
```
_Request Body:_
```json
{
  "name": "Laptop",
  "price": 1000.0,
  "description": "Gaming Laptop"
}
```
 
_Response:_
```json
{
  "message": "Item created",
  "item": { "name": "Laptop", "price": 1000.0, "description": "Gaming Laptop" }
}
```
 
#### 🔍 Read an Item
```http
GET /items/{item_id}
```
_Response:_
```json
{
  "name": "Laptop",
  "price": 1000.0,
  "description": "Gaming Laptop"
}
```
 
#### ✏️ Update an Item
```http
PUT /items/{item_id}
```
_Request Body:_
```json
{
  "name": "Updated Laptop",
  "price": 1200.0,
  "description": "High-end Gaming Laptop"
}
```
 
_Response:_
```json
{
  "message": "Item updated",
  "item": { "name": "Updated Laptop", "price": 1200.0, "description": "High-end Gaming Laptop" }
}
```
 
#### ❌ Delete an Item
```http
DELETE /items/{item_id}
```
_Response:_
```json
{
  "message": "Item deleted"
}
```
 
### 3️⃣ API Documentation
- Open your browser and go to:
  - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
 
## 🎯 Run the Server Manually
If you prefer running the server manually, execute:
```sh
uvicorn main:app --reload
