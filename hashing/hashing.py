import hashlib


def brute_force_simple_hash_cracker(hash_type: str, password_hash: str, password_wordlist_path: str, rounds: int = 1):
    real_password = ''
    with open(password_wordlist_path, 'rb') as file:
        line_read = file.readline()
        line_read = line_read[:len(line_read) - 1]
        md5_current_password = hashing_rounds(hash_type, line_read, rounds).decode('utf-8')
        current_lines = 1
        all_lines = file.readlines()
        while md5_current_password != password_hash and len(all_lines) > current_lines:
            line_read = all_lines[current_lines]
            line_read = line_read[:len(line_read) - 1]
            md5_current_password = hashing_rounds(hash_type, line_read, rounds).decode('utf-8')
            if md5_current_password == password_hash:
                real_password = line_read
                print(f'{line_read.decode("utf-8")} {md5_current_password}')
            current_lines += 1
    if len(real_password) == 0 and md5_current_password != password_hash:
        print('Could not find any math')
    elif md5_current_password == password_hash:
        print(line_read.decode('utf-8'))


def hashing_rounds(hash_type: str, to_hash: bytes, rounds: int) -> bytes:
    if rounds == 1:
        return hashlib.new(hash_type, to_hash).hexdigest().encode('utf-8')
    else:
        return hashlib.new(hash_type, hashing_rounds(hash_type, to_hash, rounds - 1)).hexdigest().encode('utf-8')


def main():
    password_to_hash = input('Tell me the password to hash: ')
    hash_type = input('What is the type of hashing: ')
    rounds = int(input('How many rounds to hash?: '))
    print(hashing_rounds(hash_type, password_to_hash.encode('utf-8'), rounds).decode('utf-8'))
    hash_password = input('Tell me the password hash: ')
    hash_type = input('What is the type of hashing: ')
    path_to_wordlist = input('Tell me the path to the wordlist: ')
    print('Possible matches: ')
    brute_force_simple_hash_cracker(hash_type, hash_password, path_to_wordlist, rounds)


if __name__ == '__main__':
    main()
