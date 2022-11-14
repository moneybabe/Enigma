import random

# create rotor class
class Rotor():
    
    # initialize self.notch, self.position; self.setting as empty dictionary
    notch = random.choice(range(26))
    setting = {}
    position = 0

    # generate random setting to self.setting
    def __init__(self):
        
        # create an alphabet list
        alphabet_lst = []
        for i in range(97,123):
            alphabet_lst.append(chr(i))
        
        # create self.setting as a dictionary {'a': 'e', 'b': 'z'} for example
        for i in range(97,123):
            value = random.choice(alphabet_lst)
            key = chr(i)
            self.setting[key] = value
            alphabet_lst.remove(value)

class Rotors():
    r1 = Rotor()
    r2 = Rotor()
    r3 = Rotor()
    end = Rotor()
