# Makefile for pycfd package

init:
    pip install -r requirements.txt

test:
    py.test tests
