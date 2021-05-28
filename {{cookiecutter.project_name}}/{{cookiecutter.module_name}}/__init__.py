"""**{{cookiecutter.project_name}}**

{{cookiecutter.description}}
"""
{%- if cookiecutter.min_python_version | float <= 3.7 %}
import sys
{%- endif %}


def __getattr__(name):
    if name == "__version__":
        # Lazy load the version only if someone asks for it
{%- if cookiecutter.min_python_version | float <= 3.7 %}
        try:
            from importlib import metadata
        except ImportError:
            import importlib_metadata as metadata  # type: ignore
{%-else %}
        from importlib import metadata
{%- endif %}

        try:
            __version__ = metadata.version("{{cookiecutter.project_name}}")
        except metadata.PackageNotFoundError:
            __version__ = "0.0.0dev0"
        globals()["__version__"] = __version__
        return __version__

    raise AttributeError(f"module {__name__} has no attribute {name}")
{% if cookiecutter.min_python_version | float <= 3.7 %}

if sys.version_info < (3, 7):
    __import__('pep562').Pep562(__name__)
{% endif -%}
