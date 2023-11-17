# markgreene74/python-template

Simple template for Python `3.11` with `pyenv`/`pyenv-virtualenv` and `poetry`.

- [quickstart](#quickstart)
- [pyenv/pyenv-virtualenv](#pyenvpyenv-virtualenv)
- [poetry](#poetry)
- [vagrant](#vagrant)
- [reference](#reference)

## quickstart

- clone the repo
  ```shell
  git clone git@github.com:markgreene74/python-template.git
  ```

## pyenv/pyenv-virtualenv

TODO
- make sure `pyenv` is installed
- make sure `pyenv-virtualenv` is installed
- install python `3.11`, for example `3.11.6`
  ```bash
  pyenv install 3.11.6
  ```
- create a virtual environment
  ```bash
  pyenv virtualenv 3.11.6 python-template-3-11
  ```
- activate the virtual environment
  ```bash
  pyenv activate python-template-3-11
  ```
- make sure `pip` and `setuptools` are up-to-date
  ```bash
  pip install --upgrade pip setuptools
  ```

## poetry

- install poetry
  ```bash
  pip install --upgrade poetry
  ```
- install the application runtime dependencies
  ```bash
  poetry install --only main
  ```
- install the application test dependencies
  ```bash
  poetry install --with test
  ```
- install the application dev, test dependencies
  ```bash
  poetry install --with test,dev
  ```
- install the dependencies but not the current project
  ```bash
  poetry install --no-root --with test,dev
  ```

## pre-commit

This project use `pre-commit`. A `.pre-commit-config.yaml` is included.

Run `pre-commit install` to install the Git hooks.

## vagrant

- create the file `.with_pyenv` if you want to install Python using `pyenv`
  ```shell
  touch .with_pyenv
  ```
- start the `vagrant` box
  ```shell
  vagrant up
  ```
  **NOTE:** when the VM is started for the first time `vagrant` will run the provisioning script. It's a good idea to redirect the output to a log file for troubleshooting.
  ```shell
  vagrant up 2>&1 | tee -a $(date +%F)-vagrant-up.log
  ```
- login to the box
  ```shell
  vagrant ssh
  ```

## reference

- poetry
  - [Installation](https://python-poetry.org/docs/#installation)
  - [Installing poetry manually](https://python-poetry.org/docs/#installing-manually)
  - [Managing dependencies](https://python-poetry.org/docs/managing-dependencies/)
- pre-commit
  - [Installation](https://pre-commit.com/#install)
  - [Usage](https://pre-commit.com/#usage)
  - [Supported hooks](https://pre-commit.com/hooks.html)
