# markgreene74/python-template [![Run tests and lint (Python 3.12)](https://github.com/markgreene74/python-template/actions/workflows/python-run-tests.yml/badge.svg?branch=main)](https://github.com/markgreene74/python-template/actions/workflows/python-run-tests.yml)

Simple template for Python `3.12` with `pyenv`/`pyenv-virtualenv` and `poetry`.

- [quickstart](#quickstart)
  - [pyenv/pyenv-virtualenv](#pyenvpyenv-virtualenv)
  - [poetry](#poetry)
  - [pre-comit](#pre-commit)
- [docker](#docker)
- [vagrant](#vagrant)
- [reference](#reference)

## quickstart

### clone the repo

```shell
git clone git@github.com:markgreene74/python-template.git
 ```

### pyenv/pyenv-virtualenv

- make sure `pyenv` and `pyenv-virtualenv` are installed
- install python `3.12`, for example `3.12.3`
  ```bash
  pyenv install 3.12.3
  ```
- create a virtual environment
  ```bash
  pyenv virtualenv 3.12.3 python-template-3-12
  ```
- activate the virtual environment
  ```bash
  pyenv activate python-template-3-12
  ```
- make sure `pip` and `setuptools` are up-to-date
  ```bash
  pip install --upgrade pip setuptools
  ```

### poetry

- install poetry
  ```bash
  pip install --upgrade poetry==1.8.3
  ```
- to install
  - the application runtime dependencies
    ```bash
    poetry install --only main
    ```
  - the application test dependencies
    ```bash
    poetry install --with test
    ```
  - the application dev and test dependencies
    ```bash
    poetry install --with test,dev
    ```
  - the dependencies but not the current project
    ```bash
    poetry install --no-root --with test,dev
    ```

### pre-commit

This project uses [`pre-commit`](https://pre-commit.com/).

- install the hooks from the `.pre-commit-config.yaml` file
  ```bash
  pre-commit install
  ```

## docker

- build the image
  ```shell
  docker build -t python-template .
  ```
- run the container
  ```shell
  docker run -it --rm python-template
  ```

Intermediate stages (`test`, `dev`) are available in the `Dockerfile`. Build them with:
```shell
docker build -t python-template . --target <stage>
```

For example, build and tun the tests with:
```shell
docker build -t python-template . --target test && \
  docker run -it --rm python-template
```

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
