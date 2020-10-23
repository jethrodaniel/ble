PY = ~/.asdf/installs/python/3.6.9/bin/python
PIP = $(PY) -m pip
run:
	sudo $(PY) -m blutooth.scan
install:
	sudo $(PIP) install -r requirements.txt
clean:
	rm -rf tmp
.PHONY: test
test:
	$(PY) -m unittest
