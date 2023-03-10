from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.service_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    author="{{cookiecutter.author_name}}",
    maintainer="{{cookiecutter.author_name}}",
    maintainer_email="{{cookiecutter.author_email}}",
    license="{{cookiecutter.license}}",
    packages=find_packages(),
    extras_require={
        "test": [
            "pre-commit",
            "pre-commit-hooks",
            "black",
            "flake8",
            "isort",
            "pytest",
        ]
    },
)
