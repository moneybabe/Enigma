import encryption_function as ef
import overall_config_function as cf

while True:
    ef.cipher_message(cf.config())
    is_keep_going = input('Keep going? (y/n) ').lower()

    if is_keep_going != 'y':
        print('HEIL NEO')
        break