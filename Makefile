.PHONY: all

install:
	pip install -e '.[dev]'

run:
	bash ~/.local/bin/uvicorn main:app --reload