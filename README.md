# general-purpose

## setup

- clone the repo
```
git clone git@github.com:markgreene74/general-purpose.git
```

- use `pyenv` install Python `3.9.2`
```
pyenv install 3.9.2
pyenv local 3.9.2
python --version
```

- create a virtual environment using `venv`
```
python -m venv .venv
```

- update `pip` in the virtual environment
```
source .venv/bin/activate
pip --version
pip install --upgrade setuptools pip
```

- install the requirements
```
pip install -r requirements.txt
```

- run `pytest`
The output should look like this:
```
(.venv) cabox@test:~/workspace/coding-test/github/general-purpose$ pytest 
========================================= test session starts =========================================
platform linux -- Python 3.9.2, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/cabox/workspace/coding-test/github/general-purpose
collected 3 items                                                                                     

test_main.py ..                                                                                 [ 66%]
test/test_helpers_main.py .                                                                     [100%]

========================================== 3 passed in 0.03s ==========================================

```