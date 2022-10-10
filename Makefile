.PHONY: all

install:
	pip install -e '.[dev]'

run:
	~/.local/bin/uvicorn main:app --reload