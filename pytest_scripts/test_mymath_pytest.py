"""Import mymath module and tests them."""

from mymath import add, divide
import pytest
import sys


@pytest.fixture()
def my_fixture(request):
    """It is a fixture."""
    print "\nI'm the fixture"

    def fin():
        print "\nFinalizer"
    request.addfinalizer(fin)


def test_my_fixture(my_fixture):
    """Test fixture."""
    print "I'm the test"


@pytest.mark.parametrize(
    "num1, num2, result", [(5, 3, 8), (3, 0, 3), (1.5, 2.5, 4)])
def test_add_integers(num1, num2, result):
    """Test add function in mymath with two non zero integer inputs."""
    assert add(num1, num2) == result


def test_add_char():
    """Test add function in mymath with two char inputs."""
    with pytest.raises(AssertionError):
        add("a", "b")


def test_divide_integers_even():
    """Test divide function in mymath with two non zero integer inputs."""
    assert divide(2, 10) == 0.2


def test_divide_integer_with_zero():
    """Test divide function in mymath with one non zero integer inputs."""
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)


@pytest.mark.skipif(sys.platform != 'win32', reason="requires wiondows")
def test_func_skipped():
    """Test the function."""
    x = 0
    print " In skipped function."
    assert (x == 0)


@pytest.mark.xfail
def test_func_xfailed():
    """Test the function."""
    assert 0

# def test_update_env_var(monkeypatch):
#     monkeypatch.setenv('DOMAIN', 'Devo')
#     assert manager.method_that_uses_env_var() == 'Devo'
