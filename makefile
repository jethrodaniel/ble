PY = ~/.asdf/installs/python/3.6.9/bin/python
PIP = $(PY) -m pip
run:
	sudo $(PY) blutooth.py
install: gattlib
	sudo $(PIP) install -r requirements.txt
clean:
	rm -rf tmp
gattlib: clean
	$(PIP) download gattlib
	mkdir -p tmp
	mv gattlib-* tmp/
	cd tmp && tar xvzf ./gattlib*
	cd tmp/gattlib* && sudo $(PIP) install .

