run:
	python src/main.py

test:
	poetry run pytest --cache-clear -k 'not benchmark'

bench:
	poetry run pytest -k 'benchmark'

