""" Make all test files importable on web_app.py"""
import os
import glob
from tests import *

modules = [os.path.basename(f)[:-3] for f in glob.glob("tests/*.py")]
__all__ = [m for m in modules if m[:-3] != "__init__"]
