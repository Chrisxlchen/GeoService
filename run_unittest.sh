#!/usr/bin/env bash
export PYTHONPATH=src:venv/lib/python3.6:venv/lib/python3.6/site-packages
coverage run --source src -m pytest -vv
coverage report -m