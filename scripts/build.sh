#! /bin/bash
python -m nuitka --follow-imports --standalone --onefile --include-package=lib --include-package=PIL src/main.py -o image_converter
