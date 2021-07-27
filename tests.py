import unittest
from reddit import find_word_in_text, get_comment_reply

from smeagol import trigger_dictionary as smeagol_trigger_dictionary


class TestStringMethods(unittest.TestCase):

    def test_find_word_in_text(self):
        self.assertFalse(find_word_in_text("There are infinite numbers between 1 and 2, but none of them are 3.", "hobbits"))
        self.assertTrue(find_word_in_text("Those darn **hobbits**.", "hobbits"))
        self.assertTrue(find_word_in_text("Po-ta-toes", "Po-ta-toes"))

    def test_get_comment_reply(self):
        self.assertTrue(get_comment_reply("Protect the Hobbits!!", smeagol_trigger_dictionary) in smeagol_trigger_dictionary[("hobbits",)])
        self.assertFalse(get_comment_reply("Where was Gondor when the Westfold fell?", smeagol_trigger_dictionary) in smeagol_trigger_dictionary[("hobbits",)])


unittest.main()
