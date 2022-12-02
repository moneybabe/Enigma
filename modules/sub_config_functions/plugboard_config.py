def plugboard_config():
    '''
    Request plugboard wiring configurations and check if input is valid.

    Returns
    -------
    plugboard_setting : list
        List of plugboard wire connections.
    '''

    print('\nYou can set up to 10 configurations for the plugboard, press enter to finish configuring')

    # request input of plugboard setting, and store the settings as a list
    plugboard_setting = []
    lst = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for i in range(10):
        setting = input('Enter the ' + lst[i] + ' two letters you want to connect in plugboard (examples: pt or yo): ').lower()
        
        # enter while loop for format checking
        while True:
            is_plugboard_format_right = True
            is_finished_configuring = False

            # finish config if user enter nothing
            if setting == '':
                print('Final plugboard setting: ')
                print(plugboard_setting)
                is_plugboard_format_right = True
                is_finished_configuring = True

            # reenter if input is not two characters
            elif len(setting) != 2:
                setting = input('Please enter only two characters: ')
                is_plugboard_format_right = False

            # reenter if input is not letter
            elif not setting.isalpha():
                setting = input('Please enter only letters: ')
                is_plugboard_format_right = False

            # reenter if setting has repeated
            else:
                for x in plugboard_setting:
                    if setting[0] in x or setting[-1] in x:
                        setting = input('Your setting has repeated, please reenter: ')
                        is_plugboard_format_right = False

            if is_plugboard_format_right:
                break

        if is_finished_configuring:
            break

        plugboard_setting.append(setting)

        # remind users what they have configured so far to avoid repeat input
        print('Current plugboard setting: ')
        print(plugboard_setting)

    return plugboard_setting