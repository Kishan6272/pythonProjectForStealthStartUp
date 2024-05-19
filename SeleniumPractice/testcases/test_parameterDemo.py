import pytest


@pytest.mark.parametrize("name,role",[("Ram","QA"),("Shweta","dev"),("ravi","manager")])
def test_validation(name,role):
    assert name != None
    assert role != None


@pytest.fixture(scope="module", params=["www.google.com","www.amazon.com"])
def val(request):
    return request.param

def test_val():
    assert val != None