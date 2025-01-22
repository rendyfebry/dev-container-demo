
.PHONY: all test
setup: requirements.txt ## Install requirements
	pip3 install -r requirements.txt

run: ## Run app with uvicorn
	uvicorn app.main:app --reload --port 8181

test: ## Run tests
	python -m pytest -vv -n auto -m "not integration" .

test-coverage: ## Run tests & coverage
	python -m pytest -vv -m "not integration" --cov=app --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html
