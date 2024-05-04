export:
	poetry export -f requirements.txt --output requirements.txt

build:
	mkdir -p build
	cp main.py build/__main__.py
	poetry run python -m pip install -r requirements.txt --target build
	poetry run python -m zipapp -p "interpreter" build

format:
	poetry run ruff format
test:
	poetry run pytest --ruff --ruff-format
run:
	poetry run python3 -c "import cccodes;print(cccodes.generate())"
