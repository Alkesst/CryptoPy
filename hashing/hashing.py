import hashlib


def brute_force_hash_cracker(hash_type: str, password_hash: str, password_wordlist_path: str):
    real_password = ''
    with open(password_wordlist_path, 'rb') as file:
        line_read = file.readline()
        line_read = line_read[:len(line_read) - 1]
        md5_current_password = hashlib.new(hash_type, line_read).hexdigest()
        current_lines = 1
        all_lines = file.readlines()
        while md5_current_password != password_hash and len(all_lines) > current_lines:
            line_read = all_lines[current_lines]
            line_read = line_read[:len(line_read) - 1]
            md5_current_password = hashlib.new(hash_type, line_read).hexdigest()
            if md5_current_password == password_hash:
                real_password = line_read
                print(f'{line_read.decode("utf-8")} {md5_current_password}')
            current_lines += 1
    if len(real_password) == 0:
        print('Could not find any math')


def one_thousand_rounds(salt: str, password: str) -> str:
    return hashlib.new('sha512', salt=salt, rounds=5000, data=password.encode('utf-8'))


def main():
    hash_password = input('Tell me the password hash: ')
    path_to_wordlist = input('Tell me the path to the wordlist: ')
    hash_type = input('What is the type of hashing: ')
    print('Possible matches: ')
    brute_force_hash_cracker(hash_type, hash_password, path_to_wordlist)


if __name__ == '__main__':
    main()
