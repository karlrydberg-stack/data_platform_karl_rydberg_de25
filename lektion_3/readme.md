## Servlet Container
* Hosting of application (Locally)
* FastAPI introduces this new concept
* Removes traditional 'play/start' button
* Requires FastAPI

## FastAPI
* Install: $ pip install "fastapi[standard]"
* Verify installation through .venv package
    * Keep main.py in root folder (best practice)
    * START APP: $ fastapi dev FILENAME.py
        * IMPORTANT: stand in the same folder as main.py
    * Bonus: uv alternative for performance
    * Bonus: CONTROL + F (filter for 'Success')
    * WARNING: Consider adding this to path
    * $ pip list

## Endpoint
* API & URL related
* Consists of a path: "/example"
* Accompanied by a HTTP-Method (GET, POST, PUT, DELETE)

## Decorator
* Identified by the @ symbol
* (Difference in how function executes)
* Runs logic from external decorator function
    * (Function over function)
* returns JSON data (automatic conversion)

<!--python
@decorator
def test_function():
-->

## URL
# Example URL: https://www.google.com/search?q=bananas&
* In this example we see a dynamic parameter
    * q == query (just a varable name)
    * ? == start of query
    * What comes after == is Dynamic_Value (client input)

## Pydantic
* Uses Schema (defines logical data type structure)
* Class based
* Used for Data Validation
* Facilitates conversion of JSON -> Python objects
* Best practice - separated from its own package
* Includes 'BaseModel' within class parameters




