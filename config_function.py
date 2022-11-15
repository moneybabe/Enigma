def config():
    # print instruction for plugboard configurations
    print('\nYou can set up to 10 configurations for the plugboard, press enter to finish configuring')

    # request input of plugboard setting, and store the settings as a list
    plugboard_setting = []
    for i in range(10):
        lst = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
        setting = input('Enter the ' + lst[i] + ' two letters you want to connect in plugboard (examples: pt or yo): ').lower()
        
        # check if format is correct
        break_setting = False
        format_is_wrong = True
        while format_is_wrong:
            format_is_wrong = False

            # finish config if user enter nothing
            if setting == '':
                print('You have finished configuring, this is your final setting: ', end = '')
                print(plugboard_setting)
                break_setting = True
                break

            # reenter if input is not two characters
            if len(setting) != 2:
                setting = input('You entered more than two characters, please reenter: ')
                format_is_wrong = True

            # reenter if not within letters range
            elif (not 97 <= ord(setting[0]) <=122) or (not 97 <= ord(setting[-1]) <= 122):
                setting = input('You entered something other than letters, please reenter: ')
                format_is_wrong = True

            # reenter if setting has repeasted
            else:
                for x in plugboard_setting:
                    if setting[0] in x or setting[-1] in x:
                        setting = input('Your setting has repeated, please reenter: ')
                        format_is_wrong = True

        # append input setting into plugboard_setting list
        plugboard_setting.append(setting)

        if break_setting:
            break

        # print plugboard_setting
        print('Your current plugboard setting: ', end = '')
        print(plugboard_setting)

    # request order of rotors
    print('Choose three rotors from a set of five and place it in order')
    first_rotor = int(input('Which one is the first rotor? '))
    second_rotor = int(input('Which one is the second rotor? '))
    third_rotor = int(input('Which one is the third rotor? '))

    # request initial position of rotors
    print('Please enter the rotors\' configurations')
    rotor1_position = int(input('Enter the initial position of rotor 1: '))
    rotor2_position = int(input('Enter the initial position of rotor 2: '))
    rotor3_position = int(input('Enter the initial position of rotor 3: '))

    return [plugboard_setting, first_rotor, second_rotor, third_rotor, rotor1_position, rotor2_position, rotor3_position]