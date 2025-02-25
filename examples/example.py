"""Example usage of the fastapi_mkdocs package."""

from fastapi import FastAPI

from fastapi_mkdocs.core import setup_application

# create a FastAPI app without an OpenAPI schema and docs route
app = FastAPI(openapi_url="")
# add the FastAPI MkDocs router to the FastAPI app
# if no docs route is provided, it will default to the root route.
setup_application(app, docs_route="/docs")


@app.get("/")
def read_root() -> dict:
    """Return a simple JSON response."""
    return {"Hello": "World"}
