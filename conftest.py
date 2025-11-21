"""conftest.py for problem 3 to ensure hw03 module is importable."""
import sys
import os

problem_dir = os.path.dirname(os.path.abspath(__file__))
if problem_dir not in sys.path:
    sys.path.insert(0, problem_dir)
