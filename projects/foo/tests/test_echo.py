""" Test for foo.echo
"""

import unittest

from hypothesis import given, strategies

from foo.echo import echo

class TestEcho(unittest.TestCase):
    """ Test for foo.echo:echo
    """

    @given(strategies.text())
    def test_echo(utterance):
        self.assertEquals(echo(utterance), utterance)
