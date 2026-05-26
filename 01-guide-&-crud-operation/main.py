from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the FastAPI application!"

@app.get("/contact")
def contact():
    return "Contact us at anytime!"

@app.get("/products")
def get_products():
    return products

#----------------------------------------------------------#
## Path params...
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    ## If product available with the id, return product, elase return error message.
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}

# http://127.0.0.1:8000/product/1
# http://127.0.0.1:8000/product/2
#----------------------------------------------------------#

## Query params...
@app.get("/greet1")
def greet1(name:str, age:int):
    return {"greet1": f"Hello, {name}! You are {age} years old."}
# http://127.0.0.1:8000/greet1?name=harshit&age=25


@app.get("/greet2")
def greet2(request: Request): # N number of query params can be passed, we will get all the query params in the form of dictionary.
    query_params = dict(request.query_params)

    return{
        "greet2": f"Hello {query_params.get('name')}! Your age is {query_params.get('age')}."
    }
# http://127.0.0.1:8000/greet2?name=harshit&age=25


#----------------------------------------------------------#

## Different types of HTTP Methods...
## GET - to get data from the server
## POST - to create data on the server
## PUT - to update data on the server
## DELETE - to delete data from the server

# To get a product by id, we will use GET method, and we will send the product id in the path params.
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    ## If product available with the id, return product, elase return error message.
    for product in products:
        if product["id"] == product_id:
            return product
    return {"ERROR": "Product not found"}

# To create a product, we will use POST method, and we will send the product data in the request body.
@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump() # Convert the ProductDTO object to a dictionary using model_dump() method provided by pydantic.
    products.append(product_data)
    return {"STATUS": "Product created successfully!", "Added Product": product_data, "Total Products": products}


# To update a product, we will use PUT method, and we will send the updated product data in the request body.
@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id: int):
    for index, oneProduct in enumerate(products):
        print(oneProduct,index)
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"STATUS": "Product updated successfully...", "Updated Product": product_data, "Total Products": products}
    return {"ERROR": "Product not found with this ID"}


# To delete a product, we will use DELETE method, and we will send the product id in the path params.
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"STATUS": "Product deleted successfully...", "Deleted Product": deleted_product, "Total Products": products}
    return {"ERROR": "Product not found with this ID"}