import unittest
from unittest.mock import patch
import modules.encryption_function as ef
import modules.sub_config_functions.plugboard_config as pb
import random
import string
from mock_input_output_module import set_keyboard_input, get_display_output, mock_input_output_start


class TestEnigma(unittest.TestCase):

    def setUp(self):
        self.random_string = ''.join(random.choices(string.ascii_lowercase, k=10))

    def tearDown(self):
        pass

    # check if request_message() deny invalid input
    def test_request_message(self):
        set_keyboard_input([self.random_string.upper()])
        raw_message = ef.request_message()
        output = get_display_output()
        self.assertEqual(output, ['Enter your message (no special character, space allowed): '])
        self.assertEqual(self.random_string, raw_message)

    # test plugboard_config() can respond to valid input correctly
    def test_plugboard_config(self):
        set_keyboard_input(['hi', ''])
        pb.plugboard_config()
        output = get_display_output()
        print(output)
        self.assertEqual(output, ['\nYou can set up to 10 configurations for the plugboard, press enter to finish configuring',
        'Enter the first two letters you want to connect in plugboard (examples: pt or yo): ',
        'Current plugboard setting: ',
        ['hi'],
        'Enter the second two letters you want to connect in plugboard (examples: pt or yo): ',
        'Final plugboard setting: ',
        ['hi'],
        output[-1]
        ])

    # encrypt random plaintxt, then decrypt the ciphertxt to check if it returns to original plaintxt
    def test_encryption_function(self):
        mock_input_output_start()
        ciphertxt = ef.cipher_message([[], [1, 4, 3], [15, 4, 21]], self.random_string)
        plaintxt = ef.cipher_message([[], [1, 4, 3], [15, 4, 21]], ciphertxt.lower())
        output = get_display_output()
        self.assertEqual(plaintxt.lower(), self.random_string)
        self.assertEqual(output, ['\nYour final plugboard config: ',
        [],
        'Your final rotors\' order: ',
        [1, 4, 3],
        'Your final rotors\' positions: ',
        [15, 4, 21],
        'Your cipher text: ',
        ciphertxt,
        '',
        '\nYour final plugboard config: ',
        [],
        'Your final rotors\' order: ',
        [1, 4, 3],
        'Your final rotors\' positions: ',
        [15, 4, 21],
        'Your cipher text: ',
        self.random_string.upper(),
        ''
        ])


if __name__ == '__main__':
    unittest.main()