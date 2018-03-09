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
    # check that we get a 303 on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")

    # test our first GET request to /game
    resp = app.request("/game")
    assert_response(resp)

    # test that we POST request to /game
    data = {'action': 'tell a joke'}
    resp = app.request("/game", method='POST', data=data)
    assert_response(resp, status='303')
