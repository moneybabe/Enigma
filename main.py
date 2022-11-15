import encryption_function as ef

is_keep_going = 'y'
while is_keep_going == 'y':
    ef.cipher_message()
    is_keep_going = input('Keep going? (y/n) ').lower()