.PHONY: test
test:
	@. env/bin/activate && PYTHONPATH=./ && \
		export GOOGLE_APPLICATION_CREDENTIALS=./gcs-credentials.json && \
		python tests/manual.py

.PHONY: install
install:
	@python3 -m venv env && . env/bin/activate && pip install -r requirements.txt

.PHONY: publish
publish:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
