#!/bin/sh
if command -v python3 >/dev/null 2>&1; then
    echo "Found python3, using it..."
    python3 main.py
elif command -v python >/dev/null 2>&1; then
    echo "Found python, using it..."
    python main.py
else
    echo "ERROR: No Python installation found!"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi