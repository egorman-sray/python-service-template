# Python Service Template

This is a cookiecutter template for bootstrapping a Python service.

## Usage

Install cookiecutter:

```bash
python -m pip install cookiecutter
```

Run cookiecutter with this template:
```bash
cookiecutter gh:egorman-sray/python-service-template
```

Follow the prompts until the repo is created, see `cookiecutter.json` for the full list of arguments.

## Initialise

Create the repository under the [Arabesque organisation](https://github.com/arabesque-sray), and then initialise your new repo:

```bash
cd <your-service>
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:arabesque-sray/<your-service>
git push -u origin master
```
