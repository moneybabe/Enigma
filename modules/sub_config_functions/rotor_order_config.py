def rotor_order_config():
    '''
    Request rotors' arrangement and check if the input values are valid.

    Returns
    -------
    rotor_numbers : list
        List of the rotors' arrangment, total of 3 elements.
    '''

    print('\nChoose three rotors from number 1 to 5')

    rotor_numbers = []
    for i in range(3):

        capital_lst = ['First', 'Second', 'Third']
        rotor_number = input(capital_lst[i] + ' rotor number: ')

        # check if input is valid
        while True: 
            is_rotor_numbet_right = True

            if not rotor_number.isnumeric():
                rotor_number = input('Please enter only interger: ')
                is_rotor_numbet_right = False

            # if entered number is out of range
            elif not 1 <= int(rotor_number) <= 5:
                rotor_number = input('Please enter only integer from 1 to 5: ')
                is_rotor_numbet_right = False

            # if entered number has repeated
            elif int(rotor_number) in rotor_numbers:
                rotor_number = input('Your rotor has repeated, please reenter: ')
                is_rotor_numbet_right = False

            if is_rotor_numbet_right:
                break

        rotor_numbers.append(int(rotor_number))

        # remind user of current config to avoid repeating input
        if i == 3:
            print('Final rotors\' order: ')
            print(rotor_numbers)    

        else:
            print('Current rotors\' order: ')
            print(rotor_numbers)

    return rotor_numbers