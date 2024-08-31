all: dependencies install build run format lint security clean

dependencies:
	if [ ! -d "dependencies" ]; then \
		mkdir dependencies; \
	fi; \
	if [ -f requirements.txt ]; then \
		pipreqs . --force; \
	else \
		pipreqs .; \
	fi

install: requirements.txt
	pip3 install --target=dependencies -r requirements.txt

format:
	black --exclude=dependencies .

security:
	bandit --exclude=dependencies -r .

lint:
	flake8 --exclude=dependencies --ignore=E501 .

build:
	# Type check with mypy
	mypy . --strict --follow-imports=skip
	python3 -m compileall -x 'dependencies/.*' .
	
run:
	python3 main.py

clean:
	rm -rf .mypy_cache
	rm -rf __pycache__
	zip -rq ../deployment_V1.zip . && echo "Zipping completed!"
	rm -rf dependencies
