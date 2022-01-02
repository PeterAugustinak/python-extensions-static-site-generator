import sys
import importlib
from pathlib import Path


def load_module(directory, name):
    """Loads module called 'name' from 'directory' folder."""
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)


def load_directory(directory):
    """Loads entire directory of extensions."""
    for path in directory.rglob('*.py'):
        load_module(directory.as_posix(), path.stem)


def load_bundled():
    """Loads bundled extensions."""
    directory = Path(__file__).parent / "extensions"
    load_directory(directory)


