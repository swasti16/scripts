# import os.path
# def getssh(): # pseudo application code
#     return os.path.join(os.path.expanduser("~admin"), '.ssh')

# def test_mytest(monkeypatch):
#     def mockreturn(path):
#         return '/abc'
#     x = getssh()
#     print x
#     monkeypatch.setattr(os.path, 'expanduser', mockreturn)
#     x = getssh()
#     print x
#     assert x == '/abc/.ssh'

"""Import mymath module and tests them."""

from mymath import divide
import pytest


def setup_module(module):
    """Setup module."""
    print ("setup_module      module:%s" % module.__name__)


def teardown_module(module):
    """Teardown module."""
    print ("teardown_module   module:%s" % module.__name__)


def setup_function(function):
    """Setup function."""
    print ("setup_function    function:%s" % function.__name__)


def teardown_function(function):
    """Teardown Function."""
    print ("teardown_function function:%s" % function.__name__)


def test_divide_integers_even():
    """Test divide function in mymath with two non zero integer inputs."""
    assert divide(2, 10) == 0.2


def test_divide_integer_with_zero():
    """Test divide function in mymath with one non zero integer inputs."""
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
