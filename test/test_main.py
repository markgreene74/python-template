import pytest
import datetime as dt
import main

# variables
MAIN_MSG = "The current datetime is:"

# tests start below this point


def test_main():
    assert isinstance(main.main(), dt.datetime)


def test_main_output(capsys):
    main.main()
    out, err = capsys.readouterr()
    assert MAIN_MSG in out
    assert err == ""
