default: help

help:
	@echo "Commands - Monopoly"
	@echo "Help"
	@echo
	@echo  "uso: make <sub command>"
	@echo  "Sub commands:"
	@echo  "    run""					        ""Runs the project and show results on console"
	@echo  "    pkg_install_python3_and_pip""				""Installs python3 and pip3"
	@echo  "    pkg_install_poetry""				""installs the dependency manager: poetry"
	@echo  "    pkg_install_dev""				""Installs the dependencies on the dev environment"
	@echo  "    pkg_install_from_zero_dev""				""Installs python3, pip3, poetry and dependencies on the dev environments"
	@echo  "    pkg_add_dev pkg=dependency_name""		""Add dependency to the dev environment"
	@echo  "    run_test""					""Run coverage test of code and pytest with modular fixture"
	@echo  "    run_test_to_html""				""Export the code test's result into a folder named 'html_test_results'"

pkg_req_del:
	rm -rf requirements.txt

pkg_install_python3_and_pip:
	sudo apt install python3 python3-pip -y 

pkg_install_poetry:
	pip3 install poetry

pkg_req_create:
	python3 -m poetry export -f requirements.txt -o requirements.txt

pkg_install_dev:
	python3 -m poetry install
	python3 -m poetry shell

pkg_install_from_zero_dev:
	make pkg_install_python3_and_pip
	make pkg_install_poetry
	make pkg_install_dev

pkg_install_prod: pkg_req_del pkg_req_create
	pip install --require-hashes -r requirements.txt

pkg_add_dev:
	python3 -m poetry add -D ${pkg}

pkg_add_prod:
	python3 -m poetry add ${pkg}

pkg_search:
	python3 -m poetry search ${pkg}

pkg_list_env:
	python3 -m poetry env list

pkg_info_env:
	python3 -m poetry env info

run_test:
	$(MAKE) -C src run_main_test

run_test_to_html: run_test
	$(MAKE) -C src run_main_test_to_html

run:
	$(MAKE) -C src run_main