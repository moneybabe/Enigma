import sub_config_functions.rotor_position_config as rpc
import sub_config_functions.rotor_order_config as roc
import sub_config_functions.plugboard_config as pc

def config():

    plugboard_setting = pc.plugboard_config()
    rotor_numbers = roc.rotor_order_config()
    rotor_positions = rpc.rotor_position_config()

    return [plugboard_setting, rotor_numbers, rotor_positions]