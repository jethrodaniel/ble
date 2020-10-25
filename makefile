PY ?= ~/.asdf/installs/python/3.6.9/bin/python
PIP = $(PY) -m pip
BT_LOG=tmp/bug/FS/data/log/bt/btsnoop_hci.log
ADB=~/Android/Sdk/platform-tools/adb

run: test
	sudo $(PY) -m blutooth.scan
install: gattlib
	sudo $(PIP) install -r requirements.txt
clean:
	rm -rf tmp logs
.PHONY: test
test: lint
	$(PY) -m unittest
lint:
	$(PY) -m yapf blutooth/*.py test/*.py --recursive --in-place --verbose
gattlib: clean
	pip3 download gattlib
	mkdir -p tmp
	mv gattlib-* tmp/
	cd tmp && tar xvzf ./gattlib*
	cd tmp/gattlib* && sudo pip3 install .
log: $(BT_LOG)
tmp:
	mkdir -p tmp
logs:
	mkdir -p logs
$(BT_LOG): tmp/bug logs
	cp -v tmp/bug/FS/data/log/bt/btsnoop_hci.log* ./logs/
tmp/bug: tmp/dumpstate.zip tmp
	cd tmp && unzip -d bug dumpstate.zip
tmp/dumpstate.zip: clean
	mkdir -p tmp && cd tmp && $(ADB) bugreport
