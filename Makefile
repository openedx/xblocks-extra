.PHONY: help lint format test docs clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

lint:  ## Run linting checks
	ruff check .
	ruff format --check .

format:  ## Auto-fix formatting issues
	ruff check --fix .
	ruff format .

test:  ## Run tests with pytest
	pytest

docs:  ## Build documentation
	$(MAKE) -C docs html

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf docs/_build/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
