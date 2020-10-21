run:
	sudo python3 blutooth.py
install: gattlib
	sudo pip3 install -r requirements.txt
clean:
	rm -rf tmp
gattlib: clean
	pip3 download gattlib
	mkdir -p tmp
	mv gattlib-* tmp/
	cd tmp && tar xvzf ./gattlib*
	cd tmp/gattlib* && sudo pip3 install .

