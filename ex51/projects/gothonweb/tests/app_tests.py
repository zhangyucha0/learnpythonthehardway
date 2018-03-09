from nose.tools import *
try:
    from bin.app import app
    from test.tools import assert_response
except ImportError:
    import sys
    sys.path.append("..")
    from bin.app import app
    from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/hello", method='POST')
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method='POST', data=data)
    assert_response(resp, contains="Zed")
