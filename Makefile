.PHONY: help requirements upgrade lint format test docs clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

requirements:  ## Sync dev dependencies
	uv sync

upgrade:  ## Upgrade python dependencies
	uv lock --upgrade

lint:  ## Run linting checks
	uv run ruff check .
	uv run ruff format --check .

format:  ## Auto-fix formatting issues
	uv run ruff check --fix .
	uv run ruff format .

test:  ## Run tests with pytest
	uv run pytest

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
