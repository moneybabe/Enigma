import encryption_function as ef

while True:
    ef.cipher_message()
    is_keep_going = input('Keep going? (y/n) ').lower()

    if is_keep_going != 'y':
        print('HEIL NEO')
        break