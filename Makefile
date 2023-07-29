.PHONY: test
test:
	@. env/bin/activate && python test/tests.py

.PHONY: install
install:
	@python3 -m virtualenv env && . env/bin/activate && pip install -r fromchaos/requirements.txt
