# Add any tasks that are not dependent on files to the .PHONY list.
.PHONY: dev test lint pip_dev

dev:
    python dev.py

test:
    py.test tests/ --cov crud_app --cov-report term-missing

lint:
    flake8 crud_app/ tests/

pip_dev:
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
