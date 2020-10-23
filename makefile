PY ?= ~/.asdf/installs/python/3.6.9/bin/python
PIP = $(PY) -m pip
run:
	sudo $(PY) -m blutooth.scan
install: gattlib
	sudo $(PIP) install -r requirements.txt
clean:
	rm -rf tmp
.PHONY: test
test:
	$(PY) -m unittest
lint:
	$(PY) -m yapf blutooth/*.py test/*.py --recursive --in-place --verbose
gattlib: clean
	pip3 download gattlib
	mkdir -p tmp
	mv gattlib-* tmp/
	cd tmp && tar xvzf ./gattlib*
	cd tmp/gattlib* && sudo pip3 install .
