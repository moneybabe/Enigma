import modules.encryption_function as ef
import modules.wrapped_config_function as cf

def main():
    '''
    Execute main() to run Enigma.
    '''

    while True:
        config_lst = cf.config()
        raw_message = ef.request_message()
        ef.cipher_message(config_lst, raw_message)
        is_keep_going = input('Keep going? (y/n) ').lower()

        if is_keep_going != 'y':
            print('HEIL NEO')
            break


if __name__ == '__main__':
    main()