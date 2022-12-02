import modules.classes.plugboard_class as pb
import modules.classes.rotor_class as rtr


def request_message():
    '''
    Request input message and check if input is valid.

    Returns
    -------
    raw_message : str
        Message to be encrypted / decrypted.
    '''

    raw_message = input('\nEnter your message (only letters, space allowed): ').lower()

    # check if raw message contains special character
    while True:
        invalid_raw_message = False

        for i in raw_message:
            if not (i.isalpha() or ord(i) == 32):
                raw_message = input('No special character, please reenter: ').lower()
                invalid_raw_message = True
                break

        if not invalid_raw_message:
            break

    return raw_message


def cipher_message(config_lst, raw_message):
    '''
    Encrypt / decrypt message according to user's configurations.

    Parameters
    ----------
    config_lst : list
        List of [plugboard setting, rotors' arrangement, rotors' rotational positions].
    raw_message : str
        User's input message.

    Returns
    -------
    ciphered_message : str
        Output message after encryption / decryption.
    '''

    # initialize plugboard config
    plugboard = pb.Plugboard(config_lst[0])

    # initialize rotors' order
    rotors = rtr.Rotors(config_lst[1][0], config_lst[1][1], config_lst[1][2])

    #initialize rotors' positions
    rotors.r1.position = config_lst[2][0]
    rotors.r2.position = config_lst[2][1]
    rotors.r3.position = config_lst[2][2]

    # remove all blank spaces and record the blank spaces' index; preparing to encrypt
    blank_space_index = []
    while True:
        index = raw_message.find(' ')
        
        if index == -1:
            break

        blank_space_index.append(index)
        raw_message = raw_message[:index] + raw_message[index + 1:]


    # encrypt the letters in message one by one
    ciphered_message = []
    for i in raw_message:

        # first rotor shifts
        rotors.r1.position += 1

        # second rotor shifts
        if rotors.r1.position % 26 == rotors.r1.notch:
            rotors.r2.position += 1

        # third rotor shifts
        if rotors.r2.position % 26 == rotors.r2.notch:
            rotors.r3.position += 1
        
        # first time passing plugboard 
        ciphertxt = i
        for x, y in plugboard.setting.items():
            if i == x:
                ciphertxt = y
            elif i == y:
                ciphertxt = x


        # entering first rotor
        plaintxt = chr((((ord(ciphertxt) + rotors.r1.position % 26) - 97) % 26) + 97)

        # transformed within first rotor
        ciphertxt = rotors.r1.setting[plaintxt]

        # entering second rotor
        plaintxt = chr((((ord(ciphertxt) + rotors.r2.position % 26 - rotors.r1.position % 26) - 97) % 26) + 97)

        # transformed within second rotor 
        ciphertxt = rotors.r2.setting[plaintxt]

        # entering third rotor
        plaintxt = chr((((ord(ciphertxt) + rotors.r3.position % 26 - rotors.r2.position % 26) - 97) % 26) + 97)
        
        # transformed within third rotor
        ciphertxt = rotors.r3.setting[plaintxt]

        # entering the reflector
        plaintxt = chr((((ord(ciphertxt) - rotors.r3.position % 26) - 97) % 26) + 97)

        # transformed within reflector
        ciphertxt = rotors.reflector[plaintxt]

        # reentering third rotor
        plaintxt = chr((((ord(ciphertxt) + rotors.r3.position % 26) - 97) % 26) + 97)
        
        # transformed within third rotor
        for a, b in rotors.r3.setting.items():
            if plaintxt == b:
                ciphertxt = a
                break

        # reentering second rotor
        plaintxt = chr((((ord(ciphertxt) + rotors.r2.position % 26 - rotors.r3.position % 26) - 97) % 26) + 97)

        # transformed within second rotor
        for a, b in rotors.r2.setting.items():
            if plaintxt == b:
                ciphertxt = a
                break

        # reentering first rotor
        plaintxt = chr((((ord(ciphertxt) + rotors.r1.position % 26 - rotors.r2.position % 26) - 97) % 26) + 97)

        # transformed within first rotor
        for a, b in rotors.r1.setting.items():
            if plaintxt == b:
                ciphertxt = a
                break

        # exiting first rotor
        ciphertxt = chr((((ord(ciphertxt) - rotors.r1.position % 26) - 97) % 26) + 97)

        # second time passing plugboard and return encrypted letter
        for x, y in plugboard.setting.items():
            if ciphertxt == x:
                ciphertxt = y
            elif ciphertxt == y:
                ciphertxt = x

        # finished encrypting one letter and append to the previous results
        ciphered_message.append(ciphertxt)
    
    # combine all ciphered letter to form the message; preparing to print a legible message
    ciphered_message = ''.join(ciphered_message).upper()

    # put back all blank spaces
    x = 0
    for i in blank_space_index:
        ciphered_message = ciphered_message[:i+x] + ' ' + ciphered_message[i+x:]
        x += 1

    # remind user's of their configurations and print the ciphered_message
    print('\nYour final plugboard config: ') 
    print(config_lst[0])
    print('Your final rotors\' order: ') 
    print(config_lst[1])
    print('Your final rotors\' positions: ') 
    print(config_lst[2])
    print('Your cipher text: ')
    print(ciphered_message)
    print('')

    return ciphered_message