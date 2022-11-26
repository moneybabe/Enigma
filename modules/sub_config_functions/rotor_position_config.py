def rotor_position_config():
    '''
    Request rotors' initial rotational positions and check if the input values are valid.

    Returns
    -------
    rotor_positions : list
        List of the rotors' initial rotational positions, total of 3 elements.
    '''
    
    # request initial position of rotors
    print('\nEnter the rotors\' initial positions (from 0 to 25 corresponding A to Z)')
    
    rotor_positions = []
    lst = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for i in range(3):
        rotor_position = input('Initial position of ' + lst[i] + ' rotor: ')

        # enter while loop for checking if rotor position format it_righTrue  is_rotor_position_right = True
        while True:
            is_rotor_position_right = True

            if not 1 <= len(rotor_position) <= 2:
                rotor_position = input('Please enter only intergers from 0 to 25: ')
                is_rotor_position_right = False
            
            elif (not 48 <= ord(rotor_position[0]) <= 57) or (not 48 <= ord(rotor_position[-1]) <= 57):
                rotor_position = input('Please enter only integers: ')
                is_rotor_position_right = False

            elif not 0 <= int(rotor_position) <= 25:
                rotor_position = input('Please enter only intergers from 0 to 25: ')
                is_rotor_position_right = False

            if is_rotor_position_right:
                break

        rotor_positions.append(int(rotor_position))

    print('Final rotors\' positions: ')
    print(rotor_positions)

    return rotor_positions