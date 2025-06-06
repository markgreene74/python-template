import datetime as dt

from application import main

# variables
MAIN_MSG = "The current datetime is:"

# tests start below this point


def test_main():
    assert isinstance(main.main(), dt.datetime)


def test_main_output(capsys):
    main.main()
    out, err = capsys.readouterr()
    assert MAIN_MSG in out
    assert "\x1b[1;35m" in out  # the output contains colours
    assert err == ""
