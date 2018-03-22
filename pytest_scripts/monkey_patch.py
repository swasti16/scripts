
#import pytest
import area
import mymath


def test_area(monkeypatch):
    def mockreturn():
        return 4
    monkeypatch.setattr(mymath, "raise_to_the_power", mockreturn)
    x = mymath.raise_to_the_power()
    assert x == 64
