"""FastAPI MkDocs Router."""

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, Response
from fastapi.templating import Jinja2Templates


class FastAPIMkDocs:
    """FastAPI MkDocs Router.

    See example.py for usage.
    """

    def __init__(
        self,
        doc_route: str | None = "documentation",
        mkdocs_site_folder: str = "./site",
        mkdocs_favicon_location: str = "./site/img/favicon.ico",
    ) -> None:
        """Generates some things somewhere."""
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

        @self.router.get(f"/{doc_route}/" + "{file_path:path}")
        async def documentation(request: Request, file_path: str) -> Response:
            """Render the documentation page.

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
