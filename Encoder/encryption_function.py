import config_function as cf
import rotor_class as rtr
import plugboard_class as pb

def encrypt_message():

    # initialize configuration of plugboard and rotor starting position
    [plugboard_setting, rotor1_position, rotor2_position, rotor3_position] = cf.config()
    plugboard = pb.Plugboard(plugboard_setting)

    # initialize rotors
    rotors = rtr.Rotors()
    rotors.r1.position = rotor1_position
    rotors.r2.position = rotor2_position
    rotors.r3.position = rotor3_position

    while True:
        
        print('Enter \'Im done\' to exit')
        raw_message = input('Enter your message: ').lower()

        if raw_message == 'im done':
            break

        encrypted_message = []
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
                    
            # passing first rotor
            plaintxt = chr((((ord(ciphertxt) + rotors.r1.position % 26) - 97) % 26) + 97)
            ciphertxt = rotors.r1.setting[plaintxt]

            # passing second rotor
            plaintxt = chr((((ord(ciphertxt) + rotors.r2.position % 26 - rotors.r1.position % 26) - 97) % 26) + 97)
            ciphertxt = rotors.r2.setting[plaintxt]

            # passing third rotor
            plaintxt = chr((((ord(ciphertxt) + rotors.r3.position % 26 - rotors.r2.position % 26) - 97) % 26) + 97)
            ciphertxt = rotors.r3.setting[plaintxt]

            # passing the end
            plaintxt = chr((((ord(ciphertxt) - rotors.r3.position % 26) - 97) % 26) + 97)
            ciphertxt = rotors.end.setting[plaintxt]

            # passing third rotor
            plaintxt = chr((((ord(ciphertxt) + rotors.r3.position % 26) - 97) % 26) + 97)
            for a, b in rotors.r3.setting.items():
                if plaintxt == b:
                    ciphertxt = a
                    break
            
            # passing second rotor
            plaintxt = chr((((ord(ciphertxt) + rotors.r2.position % 26 - rotors.r3.position % 26) - 97) % 26) + 97)
            for a, b in rotors.r2.setting.items():
                if plaintxt == b:
                    ciphertxt = a
                    break

            # passing first rotor
            plaintxt = chr((((ord(ciphertxt) + rotors.r1.position % 26 - rotors.r2.position % 26) - 97) % 26) + 97)
            for a, b in rotors.r1.setting.items():
                if plaintxt == b:
                    ciphertxt = a
                    break

            # passing back to plugboard
            plaintxt = chr((((ord(ciphertxt) - rotors.r1.position % 26) - 97) % 26) + 97)
            for a, b in rotors.r1.setting.items():
                if plaintxt == b:
                    ciphertxt = a
                    break
            
            # second time passing plugboard and return encrypted letter
            for x, y in plugboard.setting.items():
                if ciphertxt == x:
                    ciphertxt = y
                elif ciphertxt == y:
                    ciphertxt = x
                else:
                    ciphertxt = i
            
            encrypted_message.append(ciphertxt)

        print('Your cipher text:', ''.join(encrypted_message))