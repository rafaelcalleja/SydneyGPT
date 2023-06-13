.PHONY: docs
init:
	python -m pip install --upgrade pip
	python -m pip install -r ./requirements.txt --upgrade
build:
	python -m build
ci:
	python setup.py install

.PHONY: test
test:
	python -m unittest discover -s test/SydneyGPT -t test/SydneyGPT

