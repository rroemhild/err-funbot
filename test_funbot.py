import os
import unittest
import funbot

from errbot.backends.test import testbot


class TestFunBotRandomCommand(object):
    extra_plugin_dir = '.'

    def test_command_no_args(self, testbot):
        testbot.push_message('!random')
        assert 'usage: !random [min max|max]' in testbot.pop_message()

    def test_command_arg_value_error(self, testbot):
        testbot.push_message('!random xyz')
        assert 'I can only handle numbers.' in testbot.pop_message()

    def test_command_arg_max(self, testbot):
        testbot.push_message('!random 100')
        msg = testbot.pop_message()
        randint = int(msg.split()[0])
        assert 0 < randint < 100
        assert '%s (1 - 100)' % randint in msg

    def test_command_arg_min_max(self, testbot):
        testbot.push_message('!random 123 321')
        msg = testbot.pop_message()
        randint = int(msg.split()[0])
        assert 123 < randint < 321
        assert '%s (123 - 321)' % randint in msg
