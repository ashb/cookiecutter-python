"""**{{cookiecutter.project_name}}**

{{cookiecutter.description}}
"""

def __getattr__(name):
    if name == "__version__":
        # Lazy load the version only if someone asks for it
        ...
        try:
            from importlib import metadata
        except ImportError:
            import importlib_metadata as metadata

        __version__ = metadata.version('{{cookiecutter.project_name}}')

    raise AttributeError(f"module {__name__} has no attribute {name}")
