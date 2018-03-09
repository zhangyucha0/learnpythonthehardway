from nose.tools import *
try:
    import NAME
except ImportError:
    import sys
    sys.path.append("..")
    import NAME


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
