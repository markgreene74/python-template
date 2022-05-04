# markgreene74/python-template

Simple template with `pyenv`/`pyenv-virtualenv` and Python `3.10` in a `vagrant` box.

## quickstart

- clone the repo
  ```shell
  git clone git@github.com:markgreene74/python-template.git
  ```
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

## `vagrant`

## `pyenv`/`pyenv-virtualenv`

## `vagrant` + `pyenv`/`pyenv-virtualenv`
