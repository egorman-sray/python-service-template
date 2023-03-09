# {{cookiecutter.service_name}}

{{cookiecutter.description}}

## Installation

Clone the repository:

```bash
git clone https://github.com/arabesque-sray/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
```

Create and activate a virtual environment:

```bash
python -m venv .env
source .env/bin/activate
```

Install the requirements:
```bash
python -m pip install -r requirements.txt
python setup.py install
```

Install the git hooks:
```bash
# TODO
```

## Linting and Testing

To lint the project:

```bash
# TODO
```

To test the project:

```bash
python -m pytest -svv tests
```

## Deployment

```bash
# TODO
```

## License

{{cookiecutter.license}}
