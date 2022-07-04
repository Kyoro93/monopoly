run_main:
	python -m main

run_main_flake8_isort:
	flake8 monopoly/*.*
	isort **/*.py

run_main_test: run_main_flake8_isort
	pytest --cov-append --cov=monopoly tests/

run_main_test_to_html:
	rm -rf htmlcov
	pytest --cov-report html --cov=monopoly tests/