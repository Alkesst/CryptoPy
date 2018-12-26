import hashlib


def brute_force_hash_cracker(hash_type: str, password_hash: str, password_wordlist_path: str) -> str:
    real_password = ''
    with open(password_wordlist_path, 'rb') as file:
        line_read = file.readline()
        line_read = line_read[:len(line_read) - 1]
        md5_current_password = hashlib.new(hash_type, line_read).hexdigest()
        while md5_current_password != password_hash:
            line_read = file.readline()
            line_read = line_read[:len(line_read) - 1]
            md5_current_password = hashlib.new(hash_type, line_read).hexdigest()
            if md5_current_password == password_hash:
                real_password = line_read
    if len(real_password) == 0:
        real_password = 'Could not find any math'
    return real_password.decode('utf-8')


def main():
    hash_password = input('Tell me the password hash: ')
    path_to_wordlist = input('Tell me the path to the wordlist: ')
    hash_type = input('What is the type of hashing: ')
    print(brute_force_hash_cracker(hash_type, hash_password, path_to_wordlist))


if __name__ == '__main__':
    main()
