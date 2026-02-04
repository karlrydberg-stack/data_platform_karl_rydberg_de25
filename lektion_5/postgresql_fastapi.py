from fastapi import FastAPI,status
from schema.product import ProductSchema

app = FastAPI(title="postgresql_fastapi")

@app.get("/")
def root() -> dict:
    return {'Hello': 'World'}

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def post_product(product: ProductSchema) -> ProductSchema:
    return