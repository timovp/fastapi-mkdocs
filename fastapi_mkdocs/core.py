"""fastapi-mkdocs, a helper package that adds routers for your mkdocs."""

from fastapi import FastAPI

from .routers.docs import FastAPIMkDocs


def setup_application(app: FastAPI, docs_route: str | None = None) -> None:
    """Adjust settings on a FastAPI `app` object and add routes.

    Adds a FastAPI MkDocs router to the FastAPI `app` object.

    Args:
        app (FastAPI): The FastAPI app object.
        docs_route (str | None): The route to the documentation, if none provided,
        it will be at the root. Defaults to "documentation".
    """
    extra_routers = FastAPIMkDocs(docs_route)
    app.include_router(extra_routers.router)
