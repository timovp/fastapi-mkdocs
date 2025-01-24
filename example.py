from fastapi import FastAPI

from fastapi_mkdocs.core import setup_application

app = FastAPI(openapi_url="")

setup_application(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}
