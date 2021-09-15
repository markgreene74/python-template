import pytest
import datetime as dt
import helpers.helpers_main as hlp_m


def test_get_timestamp():
    assert isinstance(hlp_m.get_timestamp(), dt.datetime)
