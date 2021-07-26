import unittest
from main import find_word_in_text, get_comment_reply, trigger_dictionary


class TestStringMethods(unittest.TestCase):

    def test_find_word_in_text(self):
        self.assertFalse(
            find_word_in_text("There are infinite numbers between 1 and 2, but none of them are 3.", "hobbits"))
        self.assertTrue(find_word_in_text("Those darn **hobbits**.", "hobbits"))

    def test_get_comment_reply(self):
        self.assertTrue(get_comment_reply("Protect the Hobbits!!") in trigger_dictionary[("hobbits",)])
        self.assertFalse(
            get_comment_reply("Where was Gondor when the Westfold fell?") in trigger_dictionary[("hobbits",)])


unittest.main()
