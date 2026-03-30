from fastapi import FastAPI,status
from schema.product import ProductSchema
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json
from psycopg import Connection

DATABASE_URL = ""

pool = ConnectionPool(DATABASE_URL)

app = FastAPI(title="postgresql_fastapi")

@app.get("/")
def root() -> dict:
    return {"Hello": "World"}

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def post_product(product: ProductSchema) -> ProductSchema:

    # Query-Insert
    with pool.connection() as conn:
        with conn.transaction():
            insert_product(conn, product)

    return product

def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product.model_dump()),)    # TODO - Explore the Syntax
    )