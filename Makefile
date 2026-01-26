.PHONY: install test clean 

VENV = .venv

ifeq ($(OS),Windows_NT)
	PYTHON = $(VENV)/Scripts/python.exe
	ACTIVATE = $(VENV)/Scripts/activate
else
	PYTHON = $(VENV)/bin/python
	ACTIVATE = $(VENV)/bin/activate
endif

all: install test run

install: $(ACTIVATE)
	@echo "Dependencies installed."

$(ACTIVATE): requirements.txt
	@echo "Creating virtual environment..."
	python -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Virtual environment ready."

test:
	@echo "Running tests..."
	$(PYTHON) -m  unittest discover -s tests

run: 
	$(PYTHON) main.py 

integration: 
	$(PYTHON) runner.py

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
