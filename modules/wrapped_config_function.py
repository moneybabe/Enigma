import modules.sub_config_functions.rotor_position_config as rpc
import modules.sub_config_functions.rotor_order_config as roc
import modules.sub_config_functions.plugboard_config as pc


def config():
    '''
    Request plugboard wiring, rotors' arrangment, and rotors' rotational positions.

    Returns
    -------
    config_lst : list
        List of [0] plugboard setting, [1] rotors' order, [2] rotors' positions.
    '''

    plugboard_setting = pc.plugboard_config()
    rotor_order = roc.rotor_order_config()
    rotor_positions = rpc.rotor_position_config()
    config_lst = [plugboard_setting, rotor_order, rotor_positions]

    return config_lst