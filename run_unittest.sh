#!/usr/bin/env bash
export PYTHONPATH=src:venv/lib/python3.6:venv/lib/python3.6/site-packages
venv/bin/coverage run --source src -m pytest -vv
venv/bin/coverage report -m