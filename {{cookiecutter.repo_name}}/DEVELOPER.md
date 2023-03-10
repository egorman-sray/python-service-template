# Developer

## Table of Contents

* [Installation](#installation)
    * [Pre-requisites](#pre-requisites)
    * [Repository](#repository)
    * [Environment](#environment)
    * [Hooks](#hooks)
* [Usage](#usage)
* [Linting](#linting)
* [Testing](#testing)
* [Deployment](#deployment)

---

## Installation

### Pre-requisites

1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [Python 3.11](https://www.python.org/downloads/)

### Repository

Clone the repository:

```bash
git clone https://github.com/arabesque-sray/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
```

### Environment

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

### Hooks

Install the hooks:

```bash
pre-commit install
```

## Usage

To run the project:

```bash
# TODO
```

## Linting

To lint the project:

```bash
# TODO
```

## Testing

To test the project:

```bash
python -m pytest -v tests
```

## Deployment

```bash
# TODO
```
