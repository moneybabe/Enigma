import config_function as cf
import plugboard_class as pb
import rotor_class as rtr


def cipher_message():

    # initialize configuration of plugboard and rotor starting position
    [plugboard_setting, first_rotor, second_rotor, third_rotor, rotor1_position, rotor2_position, rotor3_position] = cf.config()
    plugboard = pb.Plugboard(plugboard_setting)

    # initialize rotors
    rotors = rtr.Rotors(first_rotor, second_rotor, third_rotor)
    rotors.r1.position = rotor1_position
    rotors.r2.position = rotor2_position
    rotors.r3.position = rotor3_position

    raw_message = input('Enter your message: ').lower()

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

    print('Your cipher text:', ''.join(ciphered_message))