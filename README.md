# cookiecutter-python

A simple template for my own personal Python3.6+ projects utilizing black + isort + flake8 + poetry + mypy + bandit + bugbear + more goodness. Best used with [cruft](https://pypi.org/project/cruft/)

To use:

        cruft create https://github.com/ashb/cookiecutter-python/

Takes inspiration from these

- https://github.com/timothycrosley/cookiecutter-python/
- https://github.com/pytest-dev/cookiecutter-pytest-plugin/

## Features

- GitHub Actions for tests and lint
- [pre-commit] for lintint/style checking locally
- Poetry and setup.cfg for project (no setup.py)
- importlib.metadata for setting `__version__`
- A choice of licenses for your project
- Sphinx or mkdocs for docs


[pre-commit]: https://pre-commit.com/
