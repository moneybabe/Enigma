def config():
    # print instruction for plugboard configurations
    print('\nYou can set up to 10 configurations for the plugboard, press enter to finish configuring')

    # request input of plugboard setting, and store the settings as a list
    plugboard_setting = []
    for i in range(10):
        lst = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
        setting = input('Enter the ' + lst[i] + ' two letters you want to connect in plugboard (examples: pt or yo): ').lower()
        
        # check if format is correct
        break_plugboard_setting = False
        is_plugboard_format_wrong = True

        # enter while loop for format checking
        while is_plugboard_format_wrong:
            is_plugboard_format_wrong = False

            # finish config if user enter nothing
            if setting == '':
                print('Final plugboard setting: ', end = '')
                print(plugboard_setting)
                break_plugboard_setting = True

            # reenter if input is not two characters
            elif len(setting) != 2:
                setting = input('Please enter only two characters: ')
                is_plugboard_format_wrong = True

            # reenter if not within letters range
            elif (not 97 <= ord(setting[0]) <=122) or (not 97 <= ord(setting[-1]) <= 122):
                setting = input('Please enter only letters: ')
                is_plugboard_format_wrong = True

            # reenter if setting has repeasted
            else:
                for x in plugboard_setting:
                    if setting[0] in x or setting[-1] in x:
                        setting = input('Your setting has repeated, please reenter: ')
                        is_plugboard_format_wrong = True

        if break_plugboard_setting:
            break

        # append input setting into plugboard_setting list
        plugboard_setting.append(setting)

        # print plugboard_setting
        print('Current plugboard setting: ', end = '')
        print(plugboard_setting)




    # request rotors' order
    print('\nChoose three rotors from number 1 to 5')

    rotor_numbers = []
    for i in range(3):
        capital_lst = ['First', 'Second', 'Third']
        rotor_number = input(capital_lst[i] + ' rotor number: ')

        # enter while loop for checking if rotor number format is wrong
        is_rotor_number_wrong = True
        while is_rotor_number_wrong:
            is_rotor_number_wrong = False

            if len(rotor_number) != 1:

                if rotor_number == '':
                    rotor_number = input('You entered nothing, please reenter: ')
                    is_rotor_number_wrong = True
                
                else:
                    rotor_number = input('Please enter only one character: ')
                    is_rotor_number_wrong = True

            elif not 49 <= ord(rotor_number) <= 53:
                rotor_number = input('Please enter only integer from 1 to 5: ')
                is_rotor_number_wrong = True

            elif int(rotor_number) in rotor_numbers:
                rotor_number = input('Your rotor has repeated, please reenter: ')
                is_rotor_number_wrong = True
        
        rotor_numbers.append(int(rotor_number))

        # print rotors' order
        if i == 3:
            print('Final rotors\' order: ', end = '')
            print(rotor_numbers)    

        else:
            print('Current rotors\' order: ', end = '')
            print(rotor_numbers)





    # request initial position of rotors
    print('\nEnter the rotors\' initial positions (from 0 to 25 corresponding A to Z)')

    rotor_positions = []
    for i in range(3):
        rotor_position = input('Initial position of ' + lst[i] + ' rotor: ')

        # enter while loop for checking if rotor position format is wrong
        is_rotor_position_wrong = True
        while is_rotor_position_wrong:
            is_rotor_position_wrong = False

            if not 1 <= len(rotor_position) <= 2:
                rotor_position = input('Please enter only intergers from 0 to 25: ')
                is_rotor_position_wrong = True
            
            elif (not 48 <= ord(rotor_position[0]) <= 57) or (not 48 <= ord(rotor_position[-1]) <= 57):
                rotor_position = input('Please enter only integers: ')
                is_rotor_position_wrong = True

            elif not 0 <= int(rotor_position) <= 25:
                rotor_position = input('Please enter only intergers from 0 to 25: ')
                is_rotor_position_wrong = True

        rotor_positions.append(int(rotor_position))

    print('Final rotors\' positions: ', end = '')
    print(rotor_positions)

    return [plugboard_setting, rotor_numbers, rotor_positions]