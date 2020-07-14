#!/bin/sh

python3 -m venv venv && \
	. venv/bin/activate && \
	pip install -e . && \
	pyre --preserve-pythonpath check