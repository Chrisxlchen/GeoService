#!/usr/bin/env bash
export PYTHONPATH=./:../venv/lib/python3.6:../venv/lib/python3.6/site-packages
py.test --cov ./
