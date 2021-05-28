"""**{{cookiecutter.project_name}}**

{{cookiecutter.description}}
"""


def __getattr__(name):
    if name == "__version__":
        # Lazy load the version only if someone asks for it
        try:
            from importlib import metadata
        except ImportError:
            import importlib_metadata as metadata

        try:
            __version__ = metadata.version("{{cookiecutter.project_name}}")
        except metadata.PackageNotFoundError:
            __version__ = "0.0.0dev0"
        globals()["__version__"] = __version__
        return __version__

    raise AttributeError(f"module {__name__} has no attribute {name}")
