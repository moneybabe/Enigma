def config():
    # print instruction for plugboard configurations
    print('\nYou can set up to 10 configurations for the plugboard ')
    print('Press enter when you finished configuring \n')

    # request input of plugboard setting, and store the settings as a list
    plugboard_setting = []
    flag = False
    for i in range(10):
        setting = input('Enter your plugboard configurations in the following format: \'a,c\' \n').lower()

        # finish config if user enter nothing
        if setting == '':
            print('You have finished configuring, this is your final setting')
            break

        # finish config if first or last character is not from a-z
        if (not 97 <= ord(setting[0]) <=122) or (not 97 <= ord(setting[-1]) <= 122):
            print('You trolling, this is your final setting')
            break

        # finish config if setting repeated
        for x in plugboard_setting:
            if setting[0] in x or setting[-1] in x:
                print('You trolling, this is your final setting')
                flag = True
                break
        
        if flag:
            break
        
        # append input setting into plugboard_setting list
        plugboard_setting.append(setting)

    # print final plugboard_setting
    print(plugboard_setting)

    # request order of rotors
    print('Choose three rotors from a set of five and place it in order')
    first_rotor = int(input('Which one is the first rotor? '))
    second_rotor = int(input('Which one is the second rotor? '))
    third_rotor = int(input('Which one is the third rotor? '))

    # request initial position of rotors
    print('\nPlease enter the rotors\' configurations')
    rotor1_position = int(input('Enter the initial position of rotor 1: '))
    rotor2_position = int(input('Enter the initial position of rotor 2: '))
    rotor3_position = int(input('Enter the initial position of rotor 3: '))

    return [plugboard_setting, first_rotor, second_rotor, third_rotor, rotor1_position, rotor2_position, rotor3_position]