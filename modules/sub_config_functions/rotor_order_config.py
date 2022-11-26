def rotor_order_config():
    '''
    Request rotors' arrangement and check if the input values are valid.

    Returns
    -------
    rotor_numbers : list
        List of the rotors' arrangment, total of 3 elements.
    '''

    # request rotors' order
    print('\nChoose three rotors from number 1 to 5')

    rotor_numbers = []
    for i in range(3):
        capital_lst = ['First', 'Second', 'Third']
        rotor_number = input(capital_lst[i] + ' rotor number: ')

        # enter while loop for checking if rotor number format it_righTrue  is_rotor_numbet_right = True
        while True: 
            is_rotor_numbet_right = True

            if len(rotor_number) != 1:

                if rotor_number == '':
                    rotor_number = input('You entered nothing, please reenter: ')
                    is_rotor_numbet_right = False
                
                else:
                    rotor_number = input('Please enter only one character: ')
                    is_rotor_numbet_right = False

            elif not 49 <= ord(rotor_number) <= 53:
                rotor_number = input('Please enter only integer from 1 to 5: ')
                is_rotor_numbet_right = False

            elif int(rotor_number) in rotor_numbers:
                rotor_number = input('Your rotor has repeated, please reenter: ')
                is_rotor_numbet_right = False

            if is_rotor_numbet_right:
                break

        rotor_numbers.append(int(rotor_number))

        # print rotors' order
        if i == 3:
            print('Final rotors\' order: ')
            print(rotor_numbers)    

        else:
            print('Current rotors\' order: ')
            print(rotor_numbers)

    return rotor_numbers