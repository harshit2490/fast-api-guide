# ⚡ Learn FastAPI — Complete Revision Guide

> A chapter-wise FastAPI reference guide with concise definitions and code examples for quick revision.

---

## 📑 Table of Contents <a id="Table-of-Contents"></a>

| #   | Topic                                                                                                     | Key Concepts                                         |
| --- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| 0   | [What is FastAPI & Setup](#chapter-0--what-is-fastapi--setup)                                             | FastAPI, Uvicorn, installation, Swagger UI           |
| 1   | [First App & Routing Basics](#chapter-1--first-app--routing-basics)                                       | `FastAPI()`, `@app.get()`, basic routes              |
| 2   | [Path Parameters](#chapter-2--path-parameters)                                                            | Dynamic URLs, type hints, `{param}`                  |
| 3   | [Query Parameters](#chapter-3--query-parameters)                                                          | `?key=value`, typed params, `Request` object         |
| 4   | [Request Body & Pydantic DTOs](#chapter-4--request-body--pydantic-dtos)                                   | `BaseModel`, validation, `model_dump()`              |
| 5   | [CRUD Operations — POST, PUT, DELETE](#chapter-5--crud-operations--post-put-delete)                       | Create, Read, Update, Delete                         |
| 6   | [Quick Cheat Sheet & API Reference](#chapter-6--quick-cheat-sheet--api-reference)                         | All routes, decorators, status codes                 |
|     | **🗂️ Project — Task Management App**                                                                      |                                                      |
| 7   | [Project Architecture & Folder Structure](#chapter-7--project-architecture--folder-structure)             | Modular design, `src/tasks`, `src/user`, `src/utils` |
| 8   | [Environment Variables & Pydantic Settings](#chapter-8--environment-variables--pydantic-settings)         | `.env`, `BaseSettings`, `SettingsConfigDict`         |
| 9   | [Database Connection — SQLAlchemy Setup](#chapter-9--database-connection--sqlalchemy-setup)               | `create_engine`, `sessionmaker`, `declarative_base`  |
| 10  | [SQLAlchemy Models — Defining Tables](#chapter-10--sqlalchemy-models--defining-tables)                    | `Column`, `Integer`, `String`, `Boolean`, ORM        |
| 11  | [Schemas (DTOs) — Request & Response Validation](#chapter-11--schemas-dtos--request--response-validation) | `TaskSchema`, `TaskResponseSchema`, `response_model` |
| 12  | [Controllers — Business Logic Layer](#chapter-12--controllers--business-logic-layer)                      | CRUD functions, `Session`, `HTTPException`           |
| 13  | [Routers — APIRouter & Dependency Injection](#chapter-13--routers--apirouter--dependency-injection)       | `APIRouter`, `Depends`, `get_db`, prefix routing     |
| 14  | [Entry Point — Wiring Everything Together](#chapter-14--entry-point--wiring-everything-together)          | `main.py`, `include_router`, `create_all`            |
| 15  | [User Module & Authentication](#chapter-15--user-module--authentication)                                  | JWT, Argon2 hashing, `is_authenticated`              |
| 16  | [Database Relationships (One-to-Many)](#chapter-16--database-relationships-one-to-many)                   | `ForeignKey`, `ondelete="CASCADE"`, User -> Tasks    |
| 17  | [Alembic Migrations](#chapter-17--alembic-migrations)                                                     | `alembic init`, `env.py`, `revision`, `upgrade head` |

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

| Requirement | Command to check   |
| ----------- | ------------------ |
| Python 3.7+ | `python --version` |
| pip         | `pip --version`    |

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

| Flag       | Description                             |
| ---------- | --------------------------------------- |
| `main`     | The Python file name (`main.py`)        |
| `app`      | The FastAPI instance variable name      |
| `--reload` | Auto-restart on code changes (dev only) |

After running, your server is live at:

```
http://127.0.0.1:8000
```

### Swagger UI — Automatic API Docs

FastAPI **automatically generates** interactive API documentation:

| URL                           | Tool           | Description                         |
| ----------------------------- | -------------- | ----------------------------------- |
| `http://127.0.0.1:8000/docs`  | **Swagger UI** | Interactive API testing interface   |
| `http://127.0.0.1:8000/redoc` | **ReDoc**      | Alternative read-only documentation |

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

| Component       | Description                                   |
| --------------- | --------------------------------------------- |
| `@app.get("/")` | Decorator — listens for `GET` requests at `/` |
| `def home()`    | Handler function — runs when the route is hit |
| `return "..."`  | Response — FastAPI auto-converts to JSON      |

### Testing the Routes

```
# Request:  GET http://127.0.0.1:8000/
# Response: "Welcome to the FastAPI application!"

# Request:  GET http://127.0.0.1:8000/contact
# Response: "Contact us at anytime!"
```

### Return Types

FastAPI automatically serializes return values to JSON:

| Return Type    | JSON Output          |
| -------------- | -------------------- |
| `str`          | `"text"`             |
| `dict`         | `{"key": "value"}`   |
| `list`         | `[1, 2, 3]`          |
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

| Part                      | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `"/product/{product_id}"` | URL path with dynamic segment `{product_id}`                 |
| `product_id: int`         | Function parameter — **must match** the `{name}` in the path |
| `: int`                   | Type hint — FastAPI auto-validates and converts              |

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

| Feature                       | Behavior                                  |
| ----------------------------- | ----------------------------------------- |
| Parameters not in path `{}`   | Automatically treated as **query params** |
| Type hints (`: str`, `: int`) | Auto-validated by FastAPI                 |
| Required by default           | Missing param → 422 error                 |

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

| Feature                      | Behavior                                         |
| ---------------------------- | ------------------------------------------------ |
| `request.query_params`       | Returns all query params as an immutable mapping |
| `dict(request.query_params)` | Convert to regular dictionary                    |
| `.get('key')`                | Safe access — returns `None` if key missing      |
| No type validation           | All values are strings — cast manually if needed |

```
# Request:  GET http://127.0.0.1:8000/greet2?name=harshit&age=25
# Response: {"greet2": "Hello harshit! Your age is 25."}
```

### Path Params vs Query Params

| Feature       | Path Params                  | Query Params                       |
| ------------- | ---------------------------- | ---------------------------------- |
| **Syntax**    | `/product/{id}`              | `/greet?name=abc`                  |
| **Position**  | Part of the URL path         | After `?` in the URL               |
| **Required?** | Always required              | Can be optional                    |
| **Use case**  | Identify a specific resource | Filter, search, or pass extra data |

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

| Field   | Type    | Default | Required?           |
| ------- | ------- | ------- | ------------------- |
| `id`    | `int`   | —       | ✅ Yes              |
| `title` | `str`   | —       | ✅ Yes              |
| `price` | `float` | `0`     | ❌ No (has default) |
| `count` | `int`   | `0`     | ❌ No (has default) |

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

| Operation  | HTTP Method | Description          |
| ---------- | ----------- | -------------------- |
| **C**reate | `POST`      | Add new data         |
| **R**ead   | `GET`       | Retrieve data        |
| **U**pdate | `PUT`       | Modify existing data |
| **D**elete | `DELETE`    | Remove data          |

### HTTP Methods in FastAPI

| Decorator       | HTTP Method | Typical Use          |
| --------------- | ----------- | -------------------- |
| `@app.get()`    | GET         | Fetch / read data    |
| `@app.post()`   | POST        | Create new data      |
| `@app.put()`    | PUT         | Update existing data |
| `@app.delete()` | DELETE      | Remove data          |

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

| Decorator              | HTTP Method | Use Case             |
| ---------------------- | ----------- | -------------------- |
| `@app.get("/path")`    | GET         | Read / Fetch data    |
| `@app.post("/path")`   | POST        | Create new data      |
| `@app.put("/path")`    | PUT         | Update existing data |
| `@app.delete("/path")` | DELETE      | Remove data          |
| `@app.patch("/path")`  | PATCH       | Partial update       |

### 📌 Parameter Types

| Type             | Where            | Example                                           |
| ---------------- | ---------------- | ------------------------------------------------- |
| **Path Param**   | In URL path      | `@app.get("/product/{id}")` → `def func(id: int)` |
| **Query Param**  | After `?` in URL | `@app.get("/greet")` → `def func(name: str)`      |
| **Request Body** | JSON in body     | `def func(data: ProductDTO)`                      |

### 📌 Pydantic Quick Reference

| Feature                  | Code                                          |
| ------------------------ | --------------------------------------------- |
| Create a model           | `class ProductDTO(BaseModel):`                |
| Required field           | `id: int`                                     |
| Optional field (default) | `price: float = 0`                            |
| Convert to dict          | `model.model_dump()`                          |
| Validate data            | Automatic — just use the model as a type hint |

### 📌 Common Commands

| Command                                       | Description                    |
| --------------------------------------------- | ------------------------------ |
| `pip install fastapi uvicorn`                 | Install FastAPI + server       |
| `uvicorn main:app --reload`                   | Run dev server with hot reload |
| `uvicorn main:app --host 0.0.0.0 --port 8080` | Run on custom host/port        |

### 📌 Key Imports

```python
from fastapi import FastAPI          # Core framework
from fastapi import Request          # Access raw request data
from pydantic import BaseModel       # Create DTOs / data models
```

### 📌 HTTP Status Codes (Common)

| Code  | Meaning               | When                            |
| ----- | --------------------- | ------------------------------- |
| `200` | OK                    | Successful GET, PUT, DELETE     |
| `201` | Created               | Successful POST                 |
| `204` | No Content            | Successful DELETE (no body)     |
| `400` | Bad Request           | Invalid client input            |
| `404` | Not Found             | Resource doesn't exist          |
| `422` | Unprocessable Entity  | Validation error (FastAPI auto) |
| `500` | Internal Server Error | Server-side error               |

### 📌 Project API Routes Summary

| Method | Route                          | Description               | Params                                 |
| ------ | ------------------------------ | ------------------------- | -------------------------------------- |
| GET    | `/`                            | Home page                 | —                                      |
| GET    | `/contact`                     | Contact info              | —                                      |
| GET    | `/products`                    | Get all products          | —                                      |
| GET    | `/product/{product_id}`        | Get one product           | Path: `product_id` (int)               |
| GET    | `/greet1`                      | Greet with typed params   | Query: `name` (str), `age` (int)       |
| GET    | `/greet2`                      | Greet with Request object | Query: dynamic via `Request`           |
| POST   | `/create_product`              | Create a product          | Body: `ProductDTO`                     |
| PUT    | `/update_product/{product_id}` | Update a product          | Path: `product_id`, Body: `ProductDTO` |
| DELETE | `/delete_product/{product_id}` | Delete a product          | Path: `product_id` (int)               |

---

> 💡 **Tip:** Bookmark this file and come back anytime for a quick revision before interviews or project work!

---

## <a id="chapter-7--project-architecture--folder-structure"></a>Chapter 7 — Project Architecture & Folder Structure | [Back to Menu🔝](#Table-of-Contents)

### Why a Modular Architecture?

In Project 1 (`01-crud-operation`), everything was in a single `main.py` — routes, logic, data all in one file. That works for learning, but **real-world apps** need separation of concerns.

Project 2 (`02-task-management-app`) uses a **modular, layered architecture** where each feature (tasks, user) gets its own folder with dedicated files for routing, business logic, data models, and schemas.

### Folder Structure

```
02-task-management-app/
├── main.py                    # Entry point — creates app, registers routers
├── .env                       # Environment variables (DB connection string)
├── requirement.txt            # Python dependencies
├── src/
│   ├── tasks/                 # 📋 Task feature module
│   │   ├── __init__.py        # Makes this folder a Python package
│   │   ├── router.py          # API routes (endpoints) for tasks
│   │   ├── controller.py      # Business logic — CRUD operations
│   │   ├── models.py          # SQLAlchemy model (database table definition)
│   │   └── dtos.py            # Pydantic schemas (request/response validation)
│   │
│   ├── user/                  # 👤 User feature module (🚧 coming soon)
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── dtos.py
│   │
│   └── utils/                 # 🔧 Shared utilities
│       ├── __init__.py
│       ├── settings.py        # Loads environment variables using Pydantic
│       ├── db.py              # Database engine, session, and connection
│       ├── constant.py        # App-wide constants (placeholder)
│       └── helpers.py         # Helper functions (placeholder)
└── .venv/                     # Virtual environment
```

### The Layered Pattern

Each feature module follows a consistent 4-file pattern:

```
Request → Router → Controller → Model/DB
                                    ↑
                              DTO validates
                              the request body
```

| File            | Role                                     | Analogy                                           |
| --------------- | ---------------------------------------- | ------------------------------------------------- |
| `router.py`     | Defines API endpoints, receives requests | **Receptionist** — takes your request             |
| `controller.py` | Business logic, talks to DB              | **Manager** — processes the request               |
| `models.py`     | Database table definition (ORM)          | **Blueprint** — defines the table structure       |
| `dtos.py`       | Request/response data validation         | **Security** — validates what comes in & goes out |

### What is `__init__.py`?

The `__init__.py` file tells Python that a directory is a **package** (importable module). Without it, Python won't recognize the folder for imports.

```python
# src/tasks/__init__.py
# __init__.py - Allows the folder to be treated as a package
```

> **Key Takeaway:** Modular architecture separates concerns — each feature gets its own `router`, `controller`, `models`, and `dtos`. Shared utilities live in `src/utils/`.

---

## <a id="chapter-8--environment-variables--pydantic-settings"></a>Chapter 8 — Environment Variables & Pydantic Settings | [Back to Menu🔝](#Table-of-Contents)

### Why Environment Variables?

**Environment variables** store configuration that changes between environments (dev, staging, production) — like database URLs, API keys, and secrets. They keep sensitive data **out of your source code**.

### The `.env` File

A `.env` file stores key-value pairs that are loaded at runtime:

```env
# .env
# DB_CONNECTION_STRING = "postgresql://user:password@localhost:port/dbname"
DB_CONNECTION_STRING = "postgresql://postgres:admin@localhost:5432/PostgreSQL 17"
```

| Part            | Value         | Description                |
| --------------- | ------------- | -------------------------- |
| `postgresql://` | Protocol      | Database type (PostgreSQL) |
| `postgres`      | Username      | Database user              |
| `admin`         | Password      | Database password          |
| `localhost`     | Host          | Server address             |
| `5432`          | Port          | PostgreSQL default port    |
| `PostgreSQL 17` | Database name | The target database        |

> ⚠️ **Never commit `.env` to Git!** Add it to `.gitignore`.

### Pydantic Settings — Loading `.env` Automatically

`pydantic-settings` is a library that loads environment variables and **validates** them using Pydantic:

```python
# src/utils/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    DB_CONNECTION_STRING: str

settings = Settings()
```

### How It Works

| Component                             | Description                                                |
| ------------------------------------- | ---------------------------------------------------------- |
| `BaseSettings`                        | Base class that auto-loads env variables into fields       |
| `SettingsConfigDict(env_file=".env")` | Tells Pydantic to read from the `.env` file                |
| `extra='ignore'`                      | Ignores any env variables that don't have a matching field |
| `DB_CONNECTION_STRING: str`           | Field name **must match** the env variable name exactly    |
| `settings = Settings()`               | Creates a singleton instance — use this everywhere         |

### ⚠️ Common Pitfall — Name Mismatch

The field name in `Settings` **must exactly match** the variable name in `.env`:

```python
# ❌ WRONG — .env has DB_CONNECTION_STRING but field says DB_CONNECTION
class Settings(BaseSettings):
    DB_CONNECTION: str          # Pydantic can't find this → ValidationError!

# ✅ CORRECT — names match exactly
class Settings(BaseSettings):
    DB_CONNECTION_STRING: str   # Matches .env → works!
```

### Using Settings in Your App

```python
# Anywhere in your project:
from src.utils.settings import settings

print(settings.DB_CONNECTION_STRING)
# Output: "postgresql://postgres:admin@localhost:5432/PostgreSQL 17"
```

### Installation

```bash
pip install pydantic-settings
```

> **Key Takeaway:** Use `pydantic-settings` to load `.env` variables into a typed `Settings` class. Field names must **exactly match** env variable names. Access via `settings.FIELD_NAME`.

---

## <a id="chapter-9--database-connection--sqlalchemy-setup"></a>Chapter 9 — Database Connection — SQLAlchemy Setup | [Back to Menu🔝](#Table-of-Contents)

### What is SQLAlchemy?

**SQLAlchemy** is Python's most popular ORM (Object-Relational Mapper). It lets you interact with databases using **Python classes** instead of raw SQL queries.

```
Python Object  ←→  SQLAlchemy ORM  ←→  Database Table
TaskModel      ←→  ORM translates  ←→  user_tasks table
```

### Database Connection Setup

```python
# src/utils/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

# Base - Base class for all ORM models
Base = declarative_base()

# Engine - Creates the connection to the database
engine = create_engine(settings.DB_CONNECTION_STRING)

# LocalSession - Factory for creating database sessions
LocalSession = sessionmaker(bind=engine)

# get_db - Dependency that provides a session per request
def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()
```

### Breaking It Down

| Component                   | What It Does                                        | Analogy                                                  |
| --------------------------- | --------------------------------------------------- | -------------------------------------------------------- |
| `create_engine(url)`        | Creates a connection pool to the database           | **Phone line** to the database                           |
| `declarative_base()`        | Returns a base class that all models inherit from   | **Template** for building table blueprints               |
| `sessionmaker(bind=engine)` | Creates a session factory bound to the engine       | **Ticket counter** — gives you a session when needed     |
| `get_db()`                  | Generator that yields a session and cleans up after | **Loan desk** — gives a session, takes it back when done |

### Why `get_db()` Uses `yield` (Not `return`)

`yield` makes `get_db()` a **generator function**. This is important because:

1. `yield session` → Provides the session to the route handler
2. `finally: session.close()` → **Always** closes the session, even if an error occurs

```python
# This is what happens under the hood:
def get_db():
    session = LocalSession()     # 1. Create session
    try:
        yield session            # 2. Give session to the route
    finally:
        session.close()          # 3. Clean up after route finishes
```

> Think of it like borrowing a library book — you get it (`yield`), use it, and it's always returned (`finally`).

### The Connection Flow

```
Settings (.env)          Engine              Session            Route Handler
     │                     │                    │                     │
     │── DB_URL ────────→ │                    │                     │
     │                     │── connection ───→ │                     │
     │                     │   pool             │── yield session ──→│
     │                     │                    │                     │── uses session
     │                     │                    │← session.close() ──│
```

### Installation

```bash
pip install sqlalchemy psycopg2
```

| Package      | Purpose                                         |
| ------------ | ----------------------------------------------- |
| `sqlalchemy` | The ORM framework                               |
| `psycopg2`   | PostgreSQL database adapter (driver) for Python |

> **Key Takeaway:** `create_engine` connects to the DB, `sessionmaker` creates sessions, and `get_db()` is a generator that provides a session per request and auto-cleans up with `yield` + `finally`.

---

## <a id="chapter-10--sqlalchemy-models--defining-tables"></a>Chapter 10 — SQLAlchemy Models — Defining Tables | [Back to Menu🔝](#Table-of-Contents)

### What is a Model?

A **model** is a Python class that represents a **database table**. Each attribute maps to a column. SQLAlchemy uses these to create, read, update, and delete rows.

```python
# src/tasks/models.py
from sqlalchemy import Column, Integer, String, Boolean
from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
```

### How the Model Maps to a Table

```
Python Class (TaskModel)          →    Database Table (user_tasks)
─────────────────────────               ──────────────────────────
id = Column(Integer, PK)          →    id         INTEGER  PRIMARY KEY
title = Column(String)            →    title      VARCHAR
description = Column(String)      →    description VARCHAR
is_completed = Column(Boolean)    →    is_completed BOOLEAN DEFAULT FALSE
```

### Breaking It Down

| Component                           | Description                                                              |
| ----------------------------------- | ------------------------------------------------------------------------ |
| `Base`                              | Inherited from `declarative_base()` — registers this class as a DB table |
| `__tablename__`                     | Sets the **actual table name** in the database                           |
| `Column(Integer, primary_key=True)` | Auto-incrementing integer ID, unique identifier                          |
| `Column(String)`                    | Variable-length text column                                              |
| `Column(Boolean, default=False)`    | Boolean column with a default value                                      |

### Common SQLAlchemy Column Types

| SQLAlchemy Type | Python Type | SQL Type                  |
| --------------- | ----------- | ------------------------- |
| `Integer`       | `int`       | `INTEGER`                 |
| `String`        | `str`       | `VARCHAR`                 |
| `Boolean`       | `bool`      | `BOOLEAN`                 |
| `Float`         | `float`     | `FLOAT`                   |
| `Text`          | `str`       | `TEXT` (unlimited length) |
| `DateTime`      | `datetime`  | `TIMESTAMP`               |

### Column Options

| Option             | Description                 | Example                             |
| ------------------ | --------------------------- | ----------------------------------- |
| `primary_key=True` | Unique row identifier       | `Column(Integer, primary_key=True)` |
| `default=value`    | Default value for new rows  | `Column(Boolean, default=False)`    |
| `nullable=False`   | Column cannot be NULL       | `Column(String, nullable=False)`    |
| `unique=True`      | No duplicate values allowed | `Column(String, unique=True)`       |

### Model vs DTO — What's the Difference?

| Feature           | Model (`models.py`)           | DTO / Schema (`dtos.py`)           |
| ----------------- | ----------------------------- | ---------------------------------- |
| **Library**       | SQLAlchemy                    | Pydantic                           |
| **Purpose**       | Defines the database table    | Validates request/response data    |
| **Inherits from** | `Base` (declarative_base)     | `BaseModel` (Pydantic)             |
| **Used for**      | DB operations (CRUD)          | API input/output validation        |
| **Has `id`?**     | ✅ Yes (auto-generated by DB) | ❌ Not in request (✅ in response) |

> **Key Takeaway:** Models define database tables using SQLAlchemy. Each class attribute is a `Column` that maps to a table column. Inherit from `Base` and set `__tablename__`.

---

## <a id="chapter-11--schemas-dtos--request--response-validation"></a>Chapter 11 — Schemas (DTOs) — Request & Response Validation | [Back to Menu🔝](#Table-of-Contents)

### Why Two Schemas?

We need **different shapes** of data for requests vs responses:

- **Request** → Client sends `title`, `description`, `is_completed` (no `id` — the DB generates it)
- **Response** → Server returns all fields **including** the `id`

### The Schemas

```python
# src/tasks/dtos.py
from pydantic import BaseModel

# Request schema — what the client sends
class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False

# Response schema — what the server returns
class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
```

### Request Schema — `TaskSchema`

Used to **validate incoming data** from the client:

| Field          | Type   | Default | Required?           |
| -------------- | ------ | ------- | ------------------- |
| `title`        | `str`  | —       | ✅ Yes              |
| `description`  | `str`  | —       | ✅ Yes              |
| `is_completed` | `bool` | `False` | ❌ No (has default) |

```json
// ✅ Valid request body:
{
    "title": "Learn FastAPI",
    "description": "Complete chapter 11"
}
// is_completed defaults to false

// ❌ Invalid — missing required field "title":
{
    "description": "No title provided"
}
// Response: 422 Validation Error
```

### Response Schema — `TaskResponseSchema`

Used to **shape the response** sent back to the client:

| Field          | Type   | Description                    |
| -------------- | ------ | ------------------------------ |
| `id`           | `int`  | Auto-generated by the database |
| `title`        | `str`  | Task title                     |
| `description`  | `str`  | Task description               |
| `is_completed` | `bool` | Completion status              |

### How `response_model` Works

In the router, `response_model` tells FastAPI to **filter and validate** the response using the specified schema:

```python
@task_routes.post("/create", response_model=TaskResponseSchema)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)
```

| Without `response_model`                                    | With `response_model=TaskResponseSchema`                  |
| ----------------------------------------------------------- | --------------------------------------------------------- |
| Returns raw SQLAlchemy object (may include internal fields) | Returns only `id`, `title`, `description`, `is_completed` |
| No output validation                                        | Auto-validates & serializes the response                  |

> **Key Takeaway:** Use separate schemas for request (`TaskSchema` — no `id`) and response (`TaskResponseSchema` — with `id`). Set `response_model` in the router to control what gets returned.

---

## <a id="chapter-12--controllers--business-logic-layer"></a>Chapter 12 — Controllers — Business Logic Layer | [Back to Menu🔝](#Table-of-Contents)

### What is a Controller?

The **controller** contains the business logic — the actual CRUD operations. It receives data from the router, interacts with the database via SQLAlchemy, and returns results.

```python
# src/tasks/controller.py
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
```

### CREATE — Add a New Task

```python
def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
    )
    db.add(new_task)        # Stage the new task
    db.commit()             # Save to database
    db.refresh(new_task)    # Reload to get the auto-generated id
    return new_task
```

| Step | Method                 | Description                                              |
| ---- | ---------------------- | -------------------------------------------------------- |
| 1    | `body.model_dump()`    | Convert Pydantic schema to a dictionary                  |
| 2    | `TaskModel(...)`       | Create a new ORM object                                  |
| 3    | `db.add(new_task)`     | Add to the session (staged, not yet saved)               |
| 4    | `db.commit()`          | Write changes to the database                            |
| 5    | `db.refresh(new_task)` | Reload the object to get DB-generated fields (like `id`) |

### READ — Get All Tasks

```python
def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    if not tasks:
        raise HTTPException(404, detail="No tasks found")
    return tasks
```

| Method                      | Description                                |
| --------------------------- | ------------------------------------------ |
| `db.query(TaskModel).all()` | Fetch all rows from the `user_tasks` table |
| `HTTPException(404, ...)`   | Return a 404 error if no tasks exist       |

### READ — Get One Task by ID

```python
def get_one_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task not found")
    return one_task
```

| Method          | Description                       |
| --------------- | --------------------------------- |
| `.get(task_id)` | Fetch a single row by primary key |

### UPDATE — Modify an Existing Task

```python
def update_task(body: TaskSchema, task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task not found")

    data = body.model_dump()
    for field, value in data.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task
```

| Step                                        | Description                                     |
| ------------------------------------------- | ----------------------------------------------- |
| `db.query(TaskModel).get(task_id)`          | Find the existing task                          |
| `body.model_dump()`                         | Convert new data to dict                        |
| `setattr(one_task, field, value)`           | Dynamically update each field on the ORM object |
| `db.add()` → `db.commit()` → `db.refresh()` | Save and reload                                 |

> 💡 `setattr(obj, "title", "New Title")` is equivalent to `obj.title = "New Title"` — but works dynamically with variable field names!

### DELETE — Remove a Task

```python
def delete_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task not found")
    db.delete(one_task)
    db.commit()
    return None
```

| Method                | Description                          |
| --------------------- | ------------------------------------ |
| `db.delete(one_task)` | Mark the row for deletion            |
| `db.commit()`         | Execute the deletion in the database |
| `return None`         | No content to return (204 status)    |

### SQLAlchemy Session Methods Cheat Sheet

| Method                    | Description                                        |
| ------------------------- | -------------------------------------------------- |
| `db.add(obj)`             | Stage a new/modified object                        |
| `db.commit()`             | Save all staged changes to the DB                  |
| `db.refresh(obj)`         | Reload object from DB (gets auto-generated values) |
| `db.delete(obj)`          | Stage an object for deletion                       |
| `db.query(Model).all()`   | Get all rows                                       |
| `db.query(Model).get(id)` | Get one row by primary key                         |

> **Key Takeaway:** Controllers handle business logic. Use `db.add()` → `db.commit()` → `db.refresh()` for create/update. Use `db.delete()` → `db.commit()` for delete. Raise `HTTPException` for errors.

---

## <a id="chapter-13--routers--apirouter--dependency-injection"></a>Chapter 13 — Routers — APIRouter & Dependency Injection | [Back to Menu🔝](#Table-of-Contents)

### What is `APIRouter`?

`APIRouter` lets you **group related routes** into separate files. Instead of defining everything on `app`, you define routes on a router and then **include** it in the main app.

```python
# Without APIRouter (everything in main.py):
app = FastAPI()
@app.post("/tasks/create")       # ← all routes in one file 😰

# With APIRouter (modular):
task_routes = APIRouter(prefix="/tasks")
@task_routes.post("/create")     # ← routes in their own file 😎
```

### The Task Router

```python
# src/tasks/router.py
from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/all_tasks", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/one_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_one_task(task_id, db)

@task_routes.put("/update_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(body: TaskSchema, task_id: int, db: Session = Depends(get_db)):
    return controller.update_task(body, task_id, db)

@task_routes.delete("/delete_task/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)
```

### What is `Depends()` — Dependency Injection?

`Depends(get_db)` is FastAPI's **dependency injection** system. It automatically calls `get_db()`, provides the session to your route, and cleans up afterward.

```python
# ✅ CORRECT — pass the function reference (not a call!)
db: Session = Depends(get_db)     # FastAPI calls get_db() for you

# ❌ WRONG — calling get_db() yourself returns a generator object
db: Session = Depends(get_db())   # TypeError: generator is not callable!
```

### How Dependency Injection Works

```
Client Request
     │
     ▼
  Router receives request
     │
     ├── Depends(get_db) → FastAPI calls get_db()
     │                      → yields a Session
     │                      → passes it as `db` parameter
     │
     ▼
  Controller uses `db` to query the database
     │
     ▼
  Response sent back
     │
     ▼
  FastAPI calls session.close() (via the `finally` block in get_db)
```

### Key Router Features Explained

| Feature           | Example                                   | Description                                   |
| ----------------- | ----------------------------------------- | --------------------------------------------- |
| `prefix="/tasks"` | `APIRouter(prefix="/tasks")`              | All routes in this router start with `/tasks` |
| `response_model`  | `response_model=TaskResponseSchema`       | Filters and validates the response shape      |
| `status_code`     | `status_code=status.HTTP_201_CREATED`     | Sets the success status code                  |
| `Depends()`       | `Depends(get_db)`                         | Injects dependencies (like DB sessions)       |
| `List[Schema]`    | `response_model=List[TaskResponseSchema]` | Returns a list of items                       |

### Route Summary — Task Module

| Method | Route                    | Full URL               | Status | Description        |
| ------ | ------------------------ | ---------------------- | ------ | ------------------ |
| POST   | `/create`                | `/tasks/create`        | 201    | Create a new task  |
| GET    | `/all_tasks`             | `/tasks/all_tasks`     | 200    | Get all tasks      |
| GET    | `/one_task/{task_id}`    | `/tasks/one_task/1`    | 200    | Get one task by ID |
| PUT    | `/update_task/{task_id}` | `/tasks/update_task/1` | 201    | Update a task      |
| DELETE | `/delete_task/{task_id}` | `/tasks/delete_task/1` | 204    | Delete a task      |

> **Key Takeaway:** Use `APIRouter(prefix=...)` to group routes by feature. Use `Depends(get_db)` (without parentheses!) to inject database sessions. Set `response_model` and `status_code` on each route.

---

## <a id="chapter-14--entry-point--wiring-everything-together"></a>Chapter 14 — Entry Point — Wiring Everything Together | [Back to Menu🔝](#Table-of-Contents)

### The Main File

`main.py` is the **entry point** of the application. It creates the FastAPI app, creates database tables, and registers all routers.

```python
# main.py
from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes

# Create all database tables defined by models
Base.metadata.create_all(bind=engine)

# Create the FastAPI application
app = FastAPI(
    title="Task Management App",
    description="This is my Task Management Application",
    version="1.0.0"
)

# Register the task router
app.include_router(task_routes)
```

### Breaking It Down

| Line                                               | Description                                                                                      |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `Base.metadata.create_all(bind=engine)`            | Scans all models that inherit from `Base` and creates their tables in the DB if they don't exist |
| `FastAPI(title=..., description=..., version=...)` | Creates the app with metadata shown in Swagger UI                                                |
| `app.include_router(task_routes)`                  | Registers all routes from `task_routes` (with the `/tasks` prefix)                               |

### How `create_all` Works

```
Base.metadata.create_all(bind=engine)
     │
     ├── Finds: TaskModel (table: "user_tasks")
     ├── Finds: UserModel (table: "users")  ← when added later
     │
     ▼
     Creates tables in PostgreSQL (if they don't already exist)
```

> 💡 `create_all` is **safe to call multiple times** — it only creates tables that don't already exist. It won't drop or modify existing tables.

### Running the App

```bash
# Using FastAPI CLI (recommended for dev)
fastapi dev main.py --reload

# Using Uvicorn directly
uvicorn main:app --reload
```

### The Complete Request Flow

```
Client (Browser/Postman)
     │
     │── POST /tasks/create  { "title": "Learn FastAPI", "description": "Ch 14" }
     │
     ▼
main.py (app)
     │── include_router(task_routes) → matches /tasks/create
     │
     ▼
router.py (task_routes)
     │── @task_routes.post("/create")
     │── Depends(get_db) → gets a DB session
     │── TaskSchema validates the request body
     │
     ▼
controller.py (create_task)
     │── model_dump() → converts to dict
     │── TaskModel() → creates ORM object
     │── db.add() → db.commit() → db.refresh()
     │
     ▼
models.py (TaskModel)
     │── Maps to "user_tasks" table in PostgreSQL
     │
     ▼
Response ← TaskResponseSchema filters the output
     │
     │── { "id": 1, "title": "Learn FastAPI", "description": "Ch 14", "is_completed": false }
     │
     ▼
Client receives the response (201 Created)
```

### Dependencies (requirement.txt)

```
"fastapi[standard]"
SQLAlchemy
pydantic_settings
psycopg2
```

| Package             | Purpose                                         |
| ------------------- | ----------------------------------------------- |
| `fastapi[standard]` | FastAPI + Uvicorn + all standard extras         |
| `SQLAlchemy`        | ORM for database operations                     |
| `pydantic_settings` | Load `.env` variables into typed Settings class |
| `psycopg2`          | PostgreSQL driver for Python                    |

## <a id="chapter-15--user-module--authentication"></a>Chapter 15 — User Module & Authentication | [Back to Menu🔝](#Table-of-Contents)

### The User Module (`src/user`)

The User module handles user registration, login, and authentication. It follows the same layered architecture as the Tasks module: `models.py`, `dtos.py`, `controller.py`, and `router.py`.

### User Registration & Password Hashing

To securely store passwords, we never save plain text. We hash passwords using `pwdlib` with the Argon2 algorithm.

```python
# src/user/controller.py
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register_user(body: UserRegisterSchema, db: Session):
    # 1. Validation logic here (username/email uniqueness)

    # 2. Hash the password
    hash_password = get_password_hash(body.password)

    # 3. Save to DB
    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hash_password,
        email=body.email
    )
    db.add(new_user)
    db.commit()
    # ...
```

### JWT Authentication (Login)

When a user logs in successfully, the server generates a **JSON Web Token (JWT)** using `pyjwt`.

```python
import jwt
from datetime import datetime, timedelta

def login_user(body: UserLoginSchema, db: Session):
    # 1. Validate username and password

    # 2. Set token expiration
    expire_time = datetime.utcnow() + timedelta(minutes=30)

    # 3. Generate JWT Token
    token = jwt.encode(
        {"_id": user.id, "exp": expire_time.timestamp()},
        settings.SECRET_KEY,
        settings.ALGORITHM
    )

    return {"token": token}
```

### Protecting Routes with `is_authenticated`

We created a dependency called `is_authenticated` (in `src/utils/helpers.py`) to extract the JWT from the `Authorization` header, verify it, and return the logged-in user object.

```python
# src/utils/helpers.py
def is_authenticated(request: Request, db: Session = Depends(get_db)):
    try:
        # 1. Get token from header
        token = request.headers.get("authorization").split(" ")[-1]

        # 2. Decode token
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        # 3. Fetch user from DB
        user = db.query(UserModel).filter(UserModel.id == data.get("_id")).first()
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Unauthorized")
```

In the **Task Router**, we inject this dependency to protect our endpoints:

```python
# src/tasks/router.py
@task_routes.post("/create")
def create_task(body: TaskSchema, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db, user)
```

> **Key Takeaway:** Use `pwdlib` to hash passwords. Use `pyjwt` to generate and decode tokens. Protect routes by injecting a custom `Depends(is_authenticated)` function that verifies the token.

---

## <a id="chapter-16--database-relationships-one-to-many"></a>Chapter 16 — Database Relationships (One-to-Many) | [Back to Menu🔝](#Table-of-Contents)

### One-to-Many Relationship

A single user can have multiple tasks. In SQL, this is represented by adding a **Foreign Key** to the child table (`user_tasks`) that references the primary key of the parent table (`user_table`).

### Defining the Foreign Key

In our `TaskModel`, we added `user_id` to link a task to a specific user.

```python
# src/tasks/models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)

    # Foreign Key linking to the 'id' column of 'user_table'
    user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))
```

### What is `ondelete="CASCADE"`?

If a user deletes their account, we don't want their tasks left floating in the database (orphan records).

Setting `ondelete="CASCADE"` tells the database: **"If the parent row in `user_table` is deleted, automatically delete all related rows in `user_tasks`."**

> **Key Takeaway:** Use `Column(Type, ForeignKey("table.column"))` to establish relationships between tables. Use `ondelete="CASCADE"` to ensure child records are deleted when the parent is deleted.

---

## <a id="chapter-17--alembic-migrations"></a>Chapter 17 — Alembic Migrations | [Back to Menu🔝](#Table-of-Contents)

### What is Alembic?

While `Base.metadata.create_all()` is great for creating tables initially, it **cannot update existing tables** (like adding a new column). **Alembic** is a database migration tool for SQLAlchemy that tracks changes to your models and updates the database schema accordingly.

### 1. Initialize Alembic

```bash
pip install alembic
alembic init migrations
```

_This creates an `alembic.ini` file and a `migrations/` directory._

### 2. Configure `env.py`

Edit `migrations/env.py` to point Alembic to your database and your models:

```python
# migrations/env.py
from src.utils.settings import settings
from src.user.models import UserModel
from src.tasks.models import TaskModel
from src.utils.db import Base

# 1. Set the DATABASE_URL environment variable
config.set_main_option("sqlalchemy.url", settings.DB_CONNECTION_STRING)

# 2. Tell Alembic about your models' metadata
target_metadata = Base.metadata
```

### 3. Generate a Migration Script

When you make changes to your models (e.g., adding `user_id`), generate a migration script:

```bash
alembic revision --autogenerate -m "Added user_id to tasks"
```

_This scans your models and compares them to the actual DB schema, generating a Python script in `migrations/versions/` with the required SQL commands._

### 4. Apply the Migration

To actually apply the changes to the database, run the upgrade command:

```bash
alembic upgrade head
```

### Useful Alembic Commands

| Command                                    | Purpose                                       |
| ------------------------------------------ | --------------------------------------------- |
| `alembic init <folder>`                    | Initialize Alembic in the project             |
| `alembic revision --autogenerate -m "msg"` | Generate a new migration script automatically |
| `alembic upgrade head`                     | Apply all pending migrations to the database  |
| `alembic history`                          | View the history of migrations                |
| `alembic downgrade -1`                     | Undo the last migration                       |

> **Key Takeaway:** Use Alembic to safely manage database schema changes over time. Configure `env.py`, generate revisions with `--autogenerate`, and apply them with `upgrade head`.

---

> **Final Key Takeaway:** `main.py` wires everything together. The request flow is: **Client → Router → `Depends(Auth)` → Controller → Model → DB → Schema Validation → Response**.

---

> 💡 **Tip:** Bookmark this file and come back anytime for a quick revision before interviews or project work!

---

_Built with ❤️ while learning FastAPI_
