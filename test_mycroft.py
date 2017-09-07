import os
import mycroft
from errbot.backends.test import testbot


class TestMycroftBot(object):
    extra_plugin_dir = '.'

    def test_mycroft_docs(self, testbot):
        testbot.push_message('where are the mycroft docs')
        assert 'The mycroft documentation can be found at ' \
               'https://docs.mycroft.ai' in testbot.pop_message()


    def test_install_mycroft(self, testbot):
        testbot.push_message('where can I install mycroft')
        assert "The information for installing mycroft " \
               "can be found here, https://docs.mycroft.ai/" \
               "installing.and.running" in testbot.pop_message()

    def test_what_mycroft(self, testbot):
        testbot.push_message('what is mycroft')
        output = "Mycroft Core is the primary module that makes up the " \
                 "Mycroft Artificial Intelligence platform.  Mycroft makes " \
                 "use of the Adapt Intent Parser, Speech-to-Text software, " \
                 "and Text-to-Speech. The idea behind the platform " \
                 "is to be able to voice enable any device and turn " \
                 "it into a smart personal assistant, able to perform a " \
                 "variety of tasks. Mycroft is often used to refer " \
                 "to the hardware product produced by Mycroft AI, Inc. " \
                 "- so to avoid confusion, the software stack is " \
                 "often referred to as \"Mycroft Core\", more info can be " \
                 "found here, https://docs.mycroft.ai"

        assert output in testbot.pop_message()

    def test_about_me(self, testbot):
        testbot.push_message('!about_me')
        assert 'I am a bot to assist in Mycroft AI related questions and ' \
               'issues.' in testbot.pop_message()

    def test_mycroft_help(self, testbot):
        testbot.push_message('!mycroft_help')
        output = "I am here to help with topics related to\n " \
                 "What is mycroft\n How do I install mycroft\n " \
                 "Where is the mycroft documentation, and anything " \
                 "else about mycroft."
        assert output in testbot.pop_message()

    def test_install_picroft(self, testbot):
        testbot.push_message('how do I install picroft')
        output = "The install guide for the picroft project can be found " \
                 "here, https://github.com/MycroftAI/enclosure-picroft/wiki" \
                 "/Getting-Started-Guide."
        assert output in testbot.pop_message()
