import modules.encryption_function as ef
import modules.overall_config_function as cf

def main():
    while True:
        ef.cipher_message(cf.config(), ef.request_message())
        is_keep_going = input('Keep going? (y/n) ').lower()

        if is_keep_going != 'y':
            print('HEIL NEO')
            break

main()