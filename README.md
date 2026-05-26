# ⚡ Learn FastAPI — Complete Revision Guide

> A chapter-wise FastAPI reference guide with concise definitions and code examples for quick revision.

---

## 📑 Table of Contents <a id="Table-of-Contents"></a>

| # | Topic | Key Concepts |
|---|-------|--------------|
| 0 | [What is FastAPI & Setup](#chapter-0--what-is-fastapi--setup) | FastAPI, Uvicorn, installation, Swagger UI |
| 1 | [First App & Routing Basics](#chapter-1--first-app--routing-basics) | `FastAPI()`, `@app.get()`, basic routes |
| 2 | [Path Parameters](#chapter-2--path-parameters) | Dynamic URLs, type hints, `{param}` |
| 3 | [Query Parameters](#chapter-3--query-parameters) | `?key=value`, typed params, `Request` object |
| 4 | [Request Body & Pydantic DTOs](#chapter-4--request-body--pydantic-dtos) | `BaseModel`, validation, `model_dump()` |
| 5 | [CRUD Operations — POST, PUT, DELETE](#chapter-5--crud-operations--post-put-delete) | Create, Read, Update, Delete |
| 6 | [Quick Cheat Sheet & API Reference](#chapter-6--quick-cheat-sheet--api-reference) | All routes, decorators, status codes |

---

## <a id="chapter-0--what-is-fastapi--setup"></a>Chapter 0 — What is FastAPI & Setup | [Back to Menu🔝](#Table-of-Contents)

### What is FastAPI?

**FastAPI** is a modern, high-performance Python web framework for building APIs. It is built on top of **Starlette** (for the web parts) and **Pydantic** (for data validation). It's one of the fastest Python frameworks available — on par with Node.js and Go.

Key highlights:
- **Automatic interactive API docs** (Swagger UI & ReDoc)
- **Type hints everywhere** — enables auto-validation and editor support
- **Async support** built-in (`async def`)
- **Very fast** — thanks to Starlette and ASGI

### What is Uvicorn?

**Uvicorn** is an ASGI (Asynchronous Server Gateway Interface) web server. It runs your FastAPI app. Think of it like this:
- **FastAPI** = your application code
- **Uvicorn** = the server that runs and serves your application

### Prerequisites

| Requirement | Command to check |
|-------------|-----------------|
| Python 3.7+ | `python --version` |
| pip | `pip --version` |

### Installation

```bash
# Install FastAPI and Uvicorn
pip install fastapi uvicorn
```

### Running the Server

```bash
# Start the development server with auto-reload
uvicorn main:app --reload
```

| Flag | Description |
|------|-------------|
| `main` | The Python file name (`main.py`) |
| `app` | The FastAPI instance variable name |
| `--reload` | Auto-restart on code changes (dev only) |

After running, your server is live at:

```
http://127.0.0.1:8000
```

### Swagger UI — Automatic API Docs

FastAPI **automatically generates** interactive API documentation:

| URL | Tool | Description |
|-----|------|-------------|
| `http://127.0.0.1:8000/docs` | **Swagger UI** | Interactive API testing interface |
| `http://127.0.0.1:8000/redoc` | **ReDoc** | Alternative read-only documentation |

> You don't need to write any extra code — just define your routes and FastAPI creates the docs for you!

### Project Structure

```
fast-api-guide/
├── 01-crud-operation/
│   ├── main.py          # FastAPI app — all routes defined here
│   ├── dtos.py          # Pydantic models (Data Transfer Objects)
│   ├── mockData.py      # In-memory mock data (products list)
│   └── .venv/           # Virtual environment
├── FastAPI Notes README.md   # ← You are here
└── Python Notes README.md
```

> **Key Takeaway:** Install with `pip install fastapi uvicorn`. Run with `uvicorn main:app --reload`. Auto-docs at `/docs`.

---

## <a id="chapter-1--first-app--routing-basics"></a>Chapter 1 — First App & Routing Basics | [Back to Menu🔝](#Table-of-Contents)

### Creating a FastAPI App

The `FastAPI()` class creates your application instance. All routes are attached to this instance.

```python
from fastapi import FastAPI

app = FastAPI()
```

### Defining Routes

A **route** (or **endpoint**) maps a URL path to a Python function. Use decorators like `@app.get()` to define routes.

```python
@app.get("/")
def home():
    return "Welcome to the FastAPI application!"

@app.get("/contact")
def contact():
    return "Contact us at anytime!"
```

### How It Works

| Component | Description |
|-----------|-------------|
| `@app.get("/")` | Decorator — listens for `GET` requests at `/` |
| `def home()` | Handler function — runs when the route is hit |
| `return "..."` | Response — FastAPI auto-converts to JSON |

### Testing the Routes

```
# Request:  GET http://127.0.0.1:8000/
# Response: "Welcome to the FastAPI application!"

# Request:  GET http://127.0.0.1:8000/contact
# Response: "Contact us at anytime!"
```

### Return Types

FastAPI automatically serializes return values to JSON:

| Return Type | JSON Output |
|-------------|-------------|
| `str` | `"text"` |
| `dict` | `{"key": "value"}` |
| `list` | `[1, 2, 3]` |
| Pydantic model | `{"field": "value"}` |

> **Key Takeaway:** Create app with `FastAPI()`. Define routes with `@app.get("/path")`. FastAPI auto-converts responses to JSON.

---

## <a id="chapter-2--path-parameters"></a>Chapter 2 — Path Parameters | [Back to Menu🔝](#Table-of-Contents)

### What are Path Parameters?

**Path parameters** are dynamic parts of the URL that capture values. They are defined using `{param_name}` in the route path.

```python
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}
```

### How It Works

| Part | Description |
|------|-------------|
| `"/product/{product_id}"` | URL path with dynamic segment `{product_id}` |
| `product_id: int` | Function parameter — **must match** the `{name}` in the path |
| `: int` | Type hint — FastAPI auto-validates and converts |

### Type Validation

FastAPI uses the type hint to **validate** incoming data automatically:

```
# ✅ Valid — "1" is converted to int
GET http://127.0.0.1:8000/product/1

# ❌ Invalid — "abc" cannot be converted to int
GET http://127.0.0.1:8000/product/abc
# Response: {"detail": [{"type": "int_parsing", ...}]}
```

> FastAPI returns an automatic **422 Validation Error** if the type doesn't match!

### Testing Path Parameters

```
# Request:  GET http://127.0.0.1:8000/product/1
# Response: {"id": 1, "title": "Mobile Phone", "price": 299.99, "count": 10}

# Request:  GET http://127.0.0.1:8000/product/2
# Response: {"id": 2, "title": "Laptop", "price": 999.99, "count": 5}

# Request:  GET http://127.0.0.1:8000/product/999
# Response: {"message": "Product not found"}
```

### Mock Data Used

The products come from `mockData.py`:

```python
# mockData.py
products = [
    {
        "id": 1,
        "title": "Mobile Phone",
        "price": 299.99,
        "count": 10
    },
    {
        "id": 2,
        "title": "Laptop",
        "price": 999.99,
        "count": 5
    },
]
```

And imported in `main.py`:

```python
from mockData import products
```

> **Key Takeaway:** Use `{param}` in the path and match it in the function. Type hints auto-validate (e.g., `: int` rejects non-integer values with a 422 error).

---

## <a id="chapter-3--query-parameters"></a>Chapter 3 — Query Parameters | [Back to Menu🔝](#Table-of-Contents)

### What are Query Parameters?

**Query parameters** are key-value pairs appended to the URL after `?`. They are used for filtering, searching, or passing optional data.

```
http://127.0.0.1:8000/greet1?name=harshit&age=25
                              ↑ query string starts after ?
```

### Method 1 — Typed Query Parameters

Define query parameters as **function arguments** (not in the URL path). FastAPI auto-detects them.

```python
@app.get("/greet1")
def greet1(name: str, age: int):
    return {"greet1": f"Hello, {name}! You are {age} years old."}
```

| Feature | Behavior |
|---------|----------|
| Parameters not in path `{}` | Automatically treated as **query params** |
| Type hints (`: str`, `: int`) | Auto-validated by FastAPI |
| Required by default | Missing param → 422 error |

```
# Request:  GET http://127.0.0.1:8000/greet1?name=harshit&age=25
# Response: {"greet1": "Hello, harshit! You are 25 years old."}

# Request:  GET http://127.0.0.1:8000/greet1
# Response: 422 Validation Error — name and age are required!
```

### Method 2 — Using the `Request` Object

For **dynamic/unknown** query parameters, use the `Request` object to capture all params as a dictionary.

```python
from fastapi import FastAPI, Request

@app.get("/greet2")
def greet2(request: Request):
    query_params = dict(request.query_params)
    return {
        "greet2": f"Hello {query_params.get('name')}! Your age is {query_params.get('age')}."
    }
```

| Feature | Behavior |
|---------|----------|
| `request.query_params` | Returns all query params as an immutable mapping |
| `dict(request.query_params)` | Convert to regular dictionary |
| `.get('key')` | Safe access — returns `None` if key missing |
| No type validation | All values are strings — cast manually if needed |

```
# Request:  GET http://127.0.0.1:8000/greet2?name=harshit&age=25
# Response: {"greet2": "Hello harshit! Your age is 25."}
```

### Path Params vs Query Params

| Feature | Path Params | Query Params |
|---------|-------------|--------------|
| **Syntax** | `/product/{id}` | `/greet?name=abc` |
| **Position** | Part of the URL path | After `?` in the URL |
| **Required?** | Always required | Can be optional |
| **Use case** | Identify a specific resource | Filter, search, or pass extra data |

> **Key Takeaway:** Function params **not in the path** become query params. Use typed params for validation, `Request` object for dynamic params.

---

## <a id="chapter-4--request-body--pydantic-dtos"></a>Chapter 4 — Request Body & Pydantic DTOs | [Back to Menu🔝](#Table-of-Contents)

### What is a Request Body?

A **request body** is the data sent by the client in the body of an HTTP request (usually with `POST` or `PUT`). Unlike query/path params, it can carry complex, structured data.

### What is Pydantic?

**Pydantic** is a data validation library that uses Python type hints. FastAPI uses it to:
- **Validate** incoming request data
- **Parse** JSON into Python objects
- **Serialize** Python objects to JSON
- **Generate** API documentation schemas

### What is a DTO (Data Transfer Object)?

A **DTO** defines the **shape** of data being transferred. In FastAPI, you create DTOs by extending Pydantic's `BaseModel`.

```python
# dtos.py
from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    title: str
    price: float = 0       # default value = 0
    count: int = 0          # default value = 0
```

### How DTOs Work

| Field | Type | Default | Required? |
|-------|------|---------|-----------|
| `id` | `int` | — | ✅ Yes |
| `title` | `str` | — | ✅ Yes |
| `price` | `float` | `0` | ❌ No (has default) |
| `count` | `int` | `0` | ❌ No (has default) |

### Using a DTO in a Route

When you use a Pydantic model as a function parameter, FastAPI knows to read the data from the **request body**.

```python
from dtos import ProductDTO

@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()  # Convert to dict
    products.append(product_data)
    return {
        "STATUS": "Product created successfully!",
        "Added Product": product_data,
        "Total Products": products
    }
```

### What is `model_dump()`?

`model_dump()` converts a Pydantic model instance into a **plain Python dictionary**.

```python
product = ProductDTO(id=3, title="Tablet", price=499.99, count=8)

product.model_dump()
# Output: {"id": 3, "title": "Tablet", "price": 499.99, "count": 8}
```

> ⚠️ **Note:** In older versions of Pydantic (v1), this was called `.dict()`. In Pydantic v2+, use `.model_dump()`.

### Automatic Validation

FastAPI + Pydantic **auto-validates** the request body:

```
# ✅ Valid request body:
{
    "id": 3,
    "title": "Tablet",
    "price": 499.99,
    "count": 8
}

# ❌ Invalid — "id" should be int, not string:
{
    "id": "abc",
    "title": "Tablet"
}
# Response: 422 Validation Error with detailed error messages
```

### Importing the DTO

```python
# In main.py
from dtos import ProductDTO
```

> **Key Takeaway:** Extend `BaseModel` to create DTOs. FastAPI reads them from the request body, validates automatically, and `model_dump()` converts them back to dicts.

---

## <a id="chapter-5--crud-operations--post-put-delete"></a>Chapter 5 — CRUD Operations — POST, PUT, DELETE | [Back to Menu🔝](#Table-of-Contents)

### What is CRUD?

**CRUD** stands for the four basic operations of persistent storage:

| Operation | HTTP Method | Description |
|-----------|-------------|-------------|
| **C**reate | `POST` | Add new data |
| **R**ead | `GET` | Retrieve data |
| **U**pdate | `PUT` | Modify existing data |
| **D**elete | `DELETE` | Remove data |

### HTTP Methods in FastAPI

| Decorator | HTTP Method | Typical Use |
|-----------|-------------|-------------|
| `@app.get()` | GET | Fetch / read data |
| `@app.post()` | POST | Create new data |
| `@app.put()` | PUT | Update existing data |
| `@app.delete()` | DELETE | Remove data |

---

### READ — `GET` (Fetch a Product by ID)

```python
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"ERROR": "Product not found"}
```

```
# Request:  GET http://127.0.0.1:8000/product/1
# Response: {"id": 1, "title": "Mobile Phone", "price": 299.99, "count": 10}

# Request:  GET http://127.0.0.1:8000/product/999
# Response: {"ERROR": "Product not found"}
```

---

### CREATE — `POST` (Add a New Product)

```python
@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {
        "STATUS": "Product created successfully!",
        "Added Product": product_data,
        "Total Products": products
    }
```

```
# Request:  POST http://127.0.0.1:8000/create_product
# Body:
# {
#     "id": 3,
#     "title": "Tablet",
#     "price": 499.99,
#     "count": 8
# }
#
# Response:
# {
#     "STATUS": "Product created successfully!",
#     "Added Product": {"id": 3, "title": "Tablet", "price": 499.99, "count": 8},
#     "Total Products": [... all products including the new one ...]
# }
```

**How it works:**
1. `product_data: ProductDTO` → FastAPI reads JSON body and validates it against `ProductDTO`
2. `.model_dump()` → Converts the Pydantic object to a dictionary
3. `products.append(...)` → Adds to the in-memory list

---

### UPDATE — `PUT` (Update an Existing Product)

```python
@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {
                "STATUS": "Product updated successfully...",
                "Updated Product": product_data,
                "Total Products": products
            }
    return {"ERROR": "Product not found with this ID"}
```

```
# Request:  PUT http://127.0.0.1:8000/update_product/1
# Body:
# {
#     "id": 1,
#     "title": "Smartphone Pro",
#     "price": 599.99,
#     "count": 15
# }
#
# Response:
# {
#     "STATUS": "Product updated successfully...",
#     "Updated Product": {"id": 1, "title": "Smartphone Pro", ...},
#     "Total Products": [... updated list ...]
# }
```

**How it works:**
1. `product_id: int` → Path param to identify which product to update
2. `product_data: ProductDTO` → New data from the request body
3. `enumerate(products)` → Loop with index so we can replace the item at that position
4. `products[index] = product_data.model_dump()` → Replace the old product with the new data

---

### DELETE — `DELETE` (Remove a Product)

```python
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {
                "STATUS": "Product deleted successfully...",
                "Deleted Product": deleted_product,
                "Total Products": products
            }
    return {"ERROR": "Product not found with this ID"}
```

```
# Request:  DELETE http://127.0.0.1:8000/delete_product/2
#
# Response:
# {
#     "STATUS": "Product deleted successfully...",
#     "Deleted Product": {"id": 2, "title": "Laptop", "price": 999.99, "count": 5},
#     "Total Products": [... remaining products ...]
# }
```

**How it works:**
1. `product_id: int` → Path param to identify which product to delete
2. `products.pop(index)` → Removes the item from the list and returns it
3. Returns both the deleted product and the remaining list

---

### Complete CRUD Flow Diagram

```
Client                          Server (FastAPI)
  │                                    │
  │── GET    /products ──────────────→ │  Read all products
  │← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│  [list of products]
  │                                    │
  │── GET    /product/1 ─────────────→ │  Read one product
  │← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│  {product details}
  │                                    │
  │── POST   /create_product ────────→ │  Create product (body: JSON)
  │← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│  {status + new product}
  │                                    │
  │── PUT    /update_product/1 ──────→ │  Update product (body: JSON)
  │← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│  {status + updated product}
  │                                    │
  │── DELETE /delete_product/1 ──────→ │  Delete product
  │← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│  {status + deleted product}
```

> **Key Takeaway:** FastAPI decorators map 1:1 to HTTP methods — `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()`. Use path params to identify resources, request body for data.

---

## <a id="chapter-6--quick-cheat-sheet--api-reference"></a>Chapter 6 — Quick Cheat Sheet & API Reference | [Back to Menu🔝](#Table-of-Contents)

### 📌 FastAPI Decorator Cheat Sheet

| Decorator | HTTP Method | Use Case |
|-----------|-------------|----------|
| `@app.get("/path")` | GET | Read / Fetch data |
| `@app.post("/path")` | POST | Create new data |
| `@app.put("/path")` | PUT | Update existing data |
| `@app.delete("/path")` | DELETE | Remove data |
| `@app.patch("/path")` | PATCH | Partial update |

### 📌 Parameter Types

| Type | Where | Example |
|------|-------|---------|
| **Path Param** | In URL path | `@app.get("/product/{id}")` → `def func(id: int)` |
| **Query Param** | After `?` in URL | `@app.get("/greet")` → `def func(name: str)` |
| **Request Body** | JSON in body | `def func(data: ProductDTO)` |

### 📌 Pydantic Quick Reference

| Feature                  | Code                                          |
| --------------------------| -----------------------------------------------|
| Create a model           | `class ProductDTO(BaseModel):`                |
| Required field           | `id: int`                                     |
| Optional field (default) | `price: float = 0`                            |
| Convert to dict          | `model.model_dump()`                          |
| Validate data            | Automatic — just use the model as a type hint |

### 📌 Common Commands

| Command | Description |
|---------|-------------|
| `pip install fastapi uvicorn` | Install FastAPI + server |
| `uvicorn main:app --reload` | Run dev server with hot reload |
| `uvicorn main:app --host 0.0.0.0 --port 8080` | Run on custom host/port |

### 📌 Key Imports

```python
from fastapi import FastAPI          # Core framework
from fastapi import Request          # Access raw request data
from pydantic import BaseModel       # Create DTOs / data models
```

### 📌 HTTP Status Codes (Common)

| Code | Meaning | When |
|------|---------|------|
| `200` | OK | Successful GET, PUT, DELETE |
| `201` | Created | Successful POST |
| `204` | No Content | Successful DELETE (no body) |
| `400` | Bad Request | Invalid client input |
| `404` | Not Found | Resource doesn't exist |
| `422` | Unprocessable Entity | Validation error (FastAPI auto) |
| `500` | Internal Server Error | Server-side error |

### 📌 Project API Routes Summary

| Method | Route | Description | Params |
|--------|-------|-------------|--------|
| GET | `/` | Home page | — |
| GET | `/contact` | Contact info | — |
| GET | `/products` | Get all products | — |
| GET | `/product/{product_id}` | Get one product | Path: `product_id` (int) |
| GET | `/greet1` | Greet with typed params | Query: `name` (str), `age` (int) |
| GET | `/greet2` | Greet with Request object | Query: dynamic via `Request` |
| POST | `/create_product` | Create a product | Body: `ProductDTO` |
| PUT | `/update_product/{product_id}` | Update a product | Path: `product_id`, Body: `ProductDTO` |
| DELETE | `/delete_product/{product_id}` | Delete a product | Path: `product_id` (int) |

---

> 💡 **Tip:** Bookmark this file and come back anytime for a quick revision before interviews or project work!

---

*Built with ❤️ while learning FastAPI*
