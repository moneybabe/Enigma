# create a class for plugboard
class Plugboard():
    
    # take user's plugboard_setting argument to define plugboard.setting
    def __init__(self, plugboard_setting):
        
        # create self.setting as a dictionary {'a': 'e', 'b': 'z'} for example
        self.setting = {}
        for i in plugboard_setting:
            self.setting[i[0]] = i[-1]