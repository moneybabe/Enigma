import config_function as cf
import plugboard_class as pb
import rotor_class as rtr


def cipher_message():

    # initialize configuration of plugboard and rotor starting position
    [plugboard_setting, rotor_numbers, rotor_positions] = cf.config()
    plugboard = pb.Plugboard(plugboard_setting)

    # initialize rotors
    rotors = rtr.Rotors(rotor_numbers[0], rotor_numbers[1], rotor_numbers[2])
    rotors.r1.position = rotor_positions[0]
    rotors.r2.position = rotor_positions[1]
    rotors.r3.position = rotor_positions[2]

    raw_message = input('Enter your message (no special character, space allowed): ').lower()

    # check if raw message contains special character
    while True:
        invalid_raw_message = False

        for i in raw_message:
            if not (97 <= ord(i) <= 122 or ord(i) == 32):
                raw_message = input('No special character, please reenter: ')
                invalid_raw_message = True

        if not invalid_raw_message:
            break


    blank_space_index = []
    while True:
        index = raw_message.find(' ')
        
        if index == -1:
            break

        blank_space_index.append(index)
        raw_message = raw_message[:index] + raw_message[index + 1:]

    ciphered_message = []
    # encrypt the letters in message one by one
    for i in raw_message:

        # first rotor turns
        rotors.r1.position += 1

        # second rotor turns
        if rotors.r1.position % 26 == rotors.r1.notch:
            rotors.r2.position += 1

        # thirs rotor turns
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


        ciphered_message.append(ciphertxt)
    
    ciphered_message = ''.join(ciphered_message).upper()

    x = 0
    for i in blank_space_index:
        ciphered_message = ciphered_message[:i+x] + ' ' + ciphered_message[i+x:]
        x += 1

    print('Your cipher text:', ciphered_message)