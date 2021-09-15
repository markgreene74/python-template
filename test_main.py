# imports
import pytest
import datetime as dt
import main

# global vars
main_msg = "The current datetime is:"

# tests starts below this point


def test_main():
    assert isinstance(main.main(), dt.datetime)

def test_main_output(capsys):
    main.main()
    out, err = capsys.readouterr()
    assert main_msg in out
    assert err == ""
