"""Example usage of the fastapi_mkdocs package."""

from fastapi import FastAPI

from fastapi_mkdocs.core import setup_application

app = FastAPI(openapi_url="")

setup_application(app)


@app.get("/")
def read_root() -> dict:
    """Return a simple JSON response."""
    return {"Hello": "World"}
