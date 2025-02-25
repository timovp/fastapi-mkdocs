"""FastAPI MkDocs Router."""

import logging

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, Response
from fastapi.templating import Jinja2Templates


class FastAPIMkDocs:
    """FastAPI MkDocs Router.

    See example.py for usage.
    """

    def __init__(
        self,
        doc_route: str | None,
        mkdocs_site_folder: str = "./site",
        mkdocs_favicon_location: str = "./site/img/favicon.ico",
    ) -> None:
        """Initialize the FastAPI MkDocs Router.

        Initialize the FastAPI MkDocs Router with the provided parameters. Please
        note that the default values are set to the default MkDocs site folder and
        favicon location. If no doc_route is provided, it will default to the root.
        From there no new get-route is needed, the router will handle the rest.
        Adding extra routes will not work anymore as the router will handle all
        requests to the documentation, which is then located at the site root.

        Args:
            doc_route (str): The route to the documentation, if none provided, it will be at the root.
            mkdocs_site_folder (str): The location of the gerenated MkDocs site-folder. Defaults to "./site".
            mkdocs_favicon_location (str): The location of the favicon of the MkDocs site. Defaults to "./site/img/favicon.ico".
        """
        self.templates_docs = Jinja2Templates(mkdocs_site_folder)
        self.router = APIRouter()
        media_type_map = {
            ".css": "text/css",
            ".js": "text/javascript",
            ".png": "image/png",
            ".ico": "image/x-icon",
            ".svg": "image/svg+xml",
            ".jpeg": "image/jpeg",
            ".woff": "font/woff",
            ".woff2": "font/woff2",
            ".ttf": "font/ttf",
        }
        if doc_route is None:
            doc_route = ""
        elif not doc_route.startswith("/"):
            doc_route = "/" + doc_route
        else:
            logger = logging.getLogger("fastapi")
            logger.warning("doc_route should not start with a /.")

        @self.router.get(f"{doc_route}/" + "{file_path:path}")
        async def documentation(request: Request, file_path: str) -> Response:
            """Return the requested documentation other than default html files.

            Args:
                request (Request): The request object coming in from the client.
                file_path (str): The path to the file to render.

            Raises:
                ValueError: When a file type or a path is not recognized.

            Returns:
                Response: A response object containing the rendered file.
            """
            if not file_path:
                file_path = "index.html"
            elif file_path.endswith("/"):
                file_path += "index.html"

            if file_path.endswith(".html"):
                return self.templates_docs.TemplateResponse(
                    request, file_path, {"request": request}, media_type="text/html"
                )
            extension = next(
                (ext for ext in media_type_map if file_path.endswith(ext)), None
            )

            if extension is not None:
                return FileResponse(
                    f"./site/{file_path}", media_type=media_type_map[extension]
                )
            else:
                raise ValueError(f"Unknown file type: {file_path}")

        @self.router.get("/favicon.ico")
        async def read_favicon(request: Request) -> FileResponse:
            """Returns the favicon incase it's needed."""
            return FileResponse(mkdocs_favicon_location)
