FastAPI CRUD Application
This FastAPI application provides a simple CRUD (Create, Read, Update, Delete) implementation using an in-memory dictionary as a database.
🚀 Features
Full CRUD operations
In-memory database using Python dictionary
Data validation with Pydantic models
API documentation with Swagger UI
🛠 Installation
If you haven’t already installed FastAPI and Uvicorn, run:
pip install fastapi uvicorn
📜 Usage
1️⃣ Run the App
python main.py
2️⃣ API Endpoints
🏠 Home Route
GET /
Response:
{
  "message": "Welcome to FastAPI CRUD App"
}
➕ Create an Item
POST /items/{item_id}
Request Body:
{
  "name": "Laptop",
  "price": 1000.0,
  "description": "Gaming Laptop"
}
Response:
{
  "message": "Item created",
  "item": { "name": "Laptop", "price": 1000.0, "description": "Gaming Laptop" }
}
🔍 Read an Item
GET /items/{item_id}
Response:
{
  "name": "Laptop",
  "price": 1000.0,
  "description": "Gaming Laptop"
}
✏️ Update an Item
PUT /items/{item_id}
Request Body:
{
  "name": "Updated Laptop",
  "price": 1200.0,
  "description": "High-end Gaming Laptop"
}
Response:
{
  "message": "Item updated",
  "item": { "name": "Updated Laptop", "price": 1200.0, "description": "High-end Gaming Laptop" }
}
❌ Delete an Item
DELETE /items/{item_id}
Response:
{
  "message": "Item deleted"
}
3️⃣ API Documentation
Open your browser and go to:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
🎯 Run the Server Manually
If you prefer running the server manually, execute:
uvicorn main:app --reload
💡 This project is a simple implementation of FastAPI CRUD operations. It can be extended with a database like SQLite, PostgreSQL, or MongoDB.
