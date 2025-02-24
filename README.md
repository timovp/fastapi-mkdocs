# Fastapi-mkdocs: 🚧🚧  WIP 🚧🚧  

The aim of this project is to integrate documentation generated with mkdocs into routes of a fastapi app.

Before running first run: 
```
mkdocs build
```
then a folder `./site/` is created, which we serve with fastapi.

TODO:

- [ ] create 'utils' module with functions used in the `Fastapimkdocs` class init.
- [ ] add '.json' file extension in the docs route file extension list.
- [x] Give the `setup_application` ~more~ any optional arguments.
- [x] Write some more docstrings/comments for the examples provided.
- [ ] add site to repo.
- [ ] create pre-commit hook to build this packages own docs.
- [ ] add some tests.

PRs and suggestions are welcome 😊
