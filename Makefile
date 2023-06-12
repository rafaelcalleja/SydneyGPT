.PHONY: docs
init:
	python -m pip install --upgrade pip
	python -m pip install -r ./requirements.txt --upgrade
build:
	python -m build
ci:
	python setup.py install
