.PHONY: test
test:
	@. env/bin/activate && python test/tests.py

.PHONY: install
install:
	@python3 -m virtualenv env && . env/bin/activate && pip install -r requirements.txt

.PHONY: publish
publish:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
