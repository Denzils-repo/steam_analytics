"""
Streamlit Community Cloud Entry Point
Redirects execution to programs/2647216_P6.py
"""
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
programs_dir = os.path.join(current_dir, "programs")
if programs_dir not in sys.path:
    sys.path.append(programs_dir)

import importlib
p6 = importlib.import_module("2647216_P6")

if __name__ == "__main__":
    p6.main()
