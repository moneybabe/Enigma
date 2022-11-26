class Rotor():
    '''
    Initialize the chosen rotor.

    Parameters
    ----------
    number : int
        The chosen number of rotor, from 1 to 5.

    Attributes
    ----------
    position : int
        Rotational position of the chosen rotor.
    notch : int
        Notch position of the chosen rotor.
    setting : dict
        Wiring of the chosen rotor.
    '''

    # class Rotor has three attributes in total: position, notch, and setting
    position = 0
    notch = 0
    setting = {}

    def __init__(self, number):
        if number == 1:
            self.setting = {
                'a': 'e',
                'b': 'k',
                'c': 'm',
                'd': 'f',
                'e': 'l',
                'f': 'g',
                'g': 'd',
                'h': 'q',
                'i': 'v',
                'j': 'z',
                'k': 'n',
                'l': 't',           # EKMFLGDQVZNTOWYHXUSPAIBRCJ
                'm': 'o',           # notch = Q
                'n': 'w',
                'o': 'y',
                'p': 'h',
                'q': 'x',
                'r': 'u',
                's': 's',
                't': 'p',
                'u': 'a',       
                'v': 'i',
                'w': 'b',
                'x': 'r',
                'y': 'c',
                'z': 'j'
                }
            self.notch = 16

        elif number == 2:
            self.setting = {
                'a': 'a',
                'b': 'j',
                'c': 'd',
                'd': 'k',
                'e': 's',
                'f': 'i',
                'g': 'r',
                'h': 'u',
                'i': 'x',
                'j': 'b',
                'k': 'l',
                'l': 'h',           # ABCDEFGHIJKLMNOPQRSTUVWXYZ = AJDKSIRUXBLHWTMCQGZNPYFVOE
                'm': 'w',           # notch = E
                'n': 't',
                'o': 'm',
                'p': 'c',
                'q': 'q',
                'r': 'g',
                's': 'z',
                't': 'n',
                'u': 'p',
                'v': 'y',
                'w': 'f',
                'x': 'v',
                'y': 'o',
                'z': 'e'
                }
            self.notch = 4

        elif number == 3:
            self.setting = {
                'a': 'b',
                'b': 'd',
                'c': 'f',
                'd': 'h',
                'e': 'j',
                'f': 'l',
                'g': 'c',
                'h': 'p',
                'i': 'r',
                'j': 't',
                'k': 'x',
                'l': 'v',           # ABCDEFGHIJKLMNOPQRSTUVWXYZ = BDFHJLCPRTXVZNYEIWGAKMUSQO
                'm': 'z',           # notch = V
                'n': 'n',
                'o': 'y',
                'p': 'e',
                'q': 'i',
                'r': 'w',
                's': 'g',
                't': 'a',
                'u': 'k',
                'v': 'm',
                'w': 'u',
                'x': 's',
                'y': 'q',
                'z': 'o'
                }
            self.notch = 21

        elif number == 4:
            self.setting = {
                'a': 'e',
                'b': 's',
                'c': 'o',
                'd': 'v',
                'e': 'p',
                'f': 'z',
                'g': 'j',
                'h': 'a',
                'i': 'y',
                'j': 'q',
                'k': 'u',
                'l': 'i',           # ABCDEFGHIJKLMNOPQRSTUVWXYZ = ESOVPZJAYQUIRHXLNFTGKDCMWB
                'm': 'r',           # notch = J
                'n': 'h',
                'o': 'x',
                'p': 'l',
                'q': 'n',
                'r': 'f',
                's': 't',
                't': 'g',
                'u': 'k',
                'v': 'd',
                'w': 'c',
                'x': 'm',
                'y': 'w',
                'z': 'b'
                }
            self.notch = 9

        elif number == 5:
            self.setting = {
                'a': 'v',
                'b': 'z',
                'c': 'b',
                'd': 'r',
                'e': 'g',
                'f': 'i',
                'g': 't',
                'h': 'y',
                'i': 'u',
                'j': 'p',
                'k': 's',
                'l': 'd',           # ABCDEFGHIJKLMNOPQRSTUVWXYZ = VZBRGITYUPSDNHLXAWMJQOFECK
                'm': 'n',           # notch = Z
                'n': 'h',
                'o': 'l',
                'p': 'x',
                'q': 'a',
                'r': 'w',
                's': 'm',
                't': 'j',
                'u': 'q',
                'v': 'o',
                'w': 'f',
                'x': 'e',
                'y': 'c',
                'z': 'k'
                }
            self.notch = 25


# group all three rotors into one class
class Rotors():
    '''
    Group all three chosen rotors into one object according to user's arrangement.

    Parameters
    ----------
    first_rotor : int
        Number of first rotor.
    second_rotor : int
        Number of second rotor.
    third_rotor : int
        Number of third rotor.

    Attributes
    ----------
    reflector : dict
        Wiring of the reflector
    r1 : obj
        First rotor object.
    r2 : obj
        Second rotor object.
    r3 : obj
        Third rotor object.
    '''

    reflector = {
        'a': 'e',
        'b': 'j',
        'c': 'm',
        'd': 'z',
        'e': 'a',
        'f': 'l',
        'g': 'y',
        'h': 'x',
        'i': 'v',
        'j': 'b',
        'k': 'w',
        'l': 'f',           # ABCDEFGHIJKLMNOPQRSTUVWXYZ = EJMZALYXVBWFCRQUONTSPIKHGD
        'm': 'c',
        'n': 'r',
        'o': 'q',
        'p': 'u',
        'q': 'o',
        'r': 'n',
        's': 't',
        't': 's',
        'u': 'p',
        'v': 'i',
        'w': 'k',
        'x': 'h',
        'y': 'g',
        'z': 'd'
        }

    # initialize the rotors order
    def __init__(self, first_rotor, second_rotor, third_rotor):
        self.r1 = Rotor(first_rotor)
        self.r2 = Rotor(second_rotor)
        self.r3 = Rotor(third_rotor)
