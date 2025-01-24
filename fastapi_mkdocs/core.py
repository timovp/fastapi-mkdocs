"""fastapi-mkdocs, a helper package that adds routers for your mkdocs."""

from fastapi import FastAPI

from .routers.docs import FastAPIMkDocs


def setup_application(app: FastAPI) -> None:
    """Adjust settings on a FastAPI `app` object and add routes."""
    # Include your custom router
    extra_routers = FastAPIMkDocs()
    app.include_router(extra_routers.router)
