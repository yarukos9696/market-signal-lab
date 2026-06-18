PYTHON ?= python

.PHONY: figures check clean

figures:
	$(PYTHON) scripts/generate_public_figures.py

check:
	$(PYTHON) scripts/generate_public_figures.py
	@test -f reports/figures/case_study_tearsheet.png
	@grep -RInE '(api[_-]?key|secret|token|password|private_key|BEGIN RSA|OPENAI|ANTHROPIC|telegram|bybit|binance)' . --exclude-dir=.git --exclude-dir=.venv --exclude='*.md' || true
	@find . -type f -size +5M -not -path './.git/*' -print

clean:
	rm -rf .pytest_cache .venv
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
