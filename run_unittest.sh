#!/usr/bin/env bash
export PYTHONPATH=app:venv/lib/python3.6:venv/lib/python3.6/site-packages
venv/bin/coverage run --source app -m pytest -vv
venv/bin/coverage report -m