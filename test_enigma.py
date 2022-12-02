import modules.encryption_function as ef
import modules.sub_config_functions.plugboard_config as pb
import modules.sub_config_functions.rotor_order_config as roc
import modules.sub_config_functions.rotor_position_config as rpc
import modules.wrapped_config_function as ocf
from main import main
import random
import string
from testing_modules.mock_input_output_module import set_keyboard_input, get_display_output

'''Test all functions'''

# test plugboard_config function returns correct config even with invalid input
def test_plugboard_config():
    set_keyboard_input(['123', 'ab', ''])
    plugboard_setting = pb.plugboard_config()
    output = get_display_output()
    assert plugboard_setting == ['ab']
    assert output == ['\nYou can set up to 10 configurations for the plugboard, press enter to finish configuring',
    'Enter the first two letters you want to connect in plugboard (examples: pt or yo): ',
    'Please enter only two characters: ',
    'Current plugboard setting: ',
    ['ab'],
    'Enter the second two letters you want to connect in plugboard (examples: pt or yo): ',
    'Final plugboard setting: ',
    ['ab']
    ]


# test rotor_order_config function returns correct config even with invalid input
def test_rotor_order_config():
    set_keyboard_input(['1', '2.0', '6', '3', '1.5', '1', ' ', '!@#', 'random', '5'])
    assert roc.rotor_order_config() == [1, 3, 5]


# test rotor_position_config function returns correect config even with invalid input
def test_rotor_position_config():
    set_keyboard_input(['-7', '12', '3.0', '26', '1.9', 'random str', '#!@$', ' ', '4', '17'])
    assert rpc.rotor_position_config() == [12, 4, 17]


# test overall_config_function returns correct config
def test_overall_config_function():
    set_keyboard_input(['qw', 'er', 'ty', '', '4', '2', '5.0', '1', '', '23', '5', '13'])
    assert ocf.config() == [['qw', 'er', 'ty'], [4, 2, 1], [23, 5, 13]]


# test request_message function returns correct config even with invalid input
def test_request_message():
    set_keyboard_input(['!@#', 'dwd23fefw', 'raNdoM     sTrINg'])
    output = ef.request_message()
    assert output == 'random     string'


# test encryption_function can encrypt 'hello world' correctly 
def test_encryption_function():
    config_lst = [['ab', 'cd', 'ef'], [1, 4, 5], [15, 24, 6]]
    assert ef.cipher_message(config_lst, 'hello world') == 'EYHYI FCWJQ'


# test main_function can encrypt a random message and decrypting the message will return the correct plain text
def test_main_function():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    set_keyboard_input(['ab', 'cd', 'ef', '', '4', '2', '5', '21', '9', '13', random_string, 'n'])
    main()
    output = get_display_output()
    set_keyboard_input(['ab', 'cd', 'ef', '', '4', '2', '5', '21', '9', '13', output[-4], 'n'])
    main()
    output = get_display_output()
    plaintxt = output[-4]
    assert plaintxt == random_string.upper()
