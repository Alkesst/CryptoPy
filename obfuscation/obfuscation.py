import base64
import binascii
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"
base64_challenge = "VWtkc2EwbEliSFprVTBJeFI6SIZaMWxUUW5OaU1qbDNVSGM5UFFvPQo="


def caesar_cipher(to_cipher: str, offset: int = 3) -> str:
    ciphered_text = ''
    for i in range(len(to_cipher)):
        current_char = to_cipher[i]
        if current_char.isalpha():
            if current_char.isupper():
                ciphered_text += alpha_upper[(offset + alpha_upper.find(current_char)) % 26]
            elif current_char.islower():
                ciphered_text += alpha_lower[(offset + alpha_lower.find(current_char)) % 26]
        else:
            ciphered_text += current_char
    return ciphered_text


def rot13(to_cipher: str) -> str:
    return caesar_cipher(to_cipher, 13)


def base64cipher(to_cipher: bytes) -> bytes:
    return base64.b64encode(to_cipher)


def caesar_crack(ciphered_text: str):
    """
    This method cracks the caesar cipher using brute force.
    Caesar cipher is easy to crack, because there are only 26 possible offsets
    :param ciphered_text: Ciphered text to crack
    :return: None
    """
    for i in range(26):
        print('{} {}'.format(i, caesar_cipher(ciphered_text, i)))


def xor_cipher(to_cipher: str, key: str) -> str:
    cipher = b''
    for i in range(len(to_cipher)):
        char = to_cipher[i]
        key_char = key[i % len(key)]
        cipher += bytes([ord(key_char) ^ ord(char)])
    return binascii.hexlify(cipher).decode('ascii')


def xor_cipher_crack_one_digit_key(ciphered: str):
    for k in '0123456789':
        clear = ''
        for i in range(len(ciphered)):
            char = ciphered[i]
            clear += chr(ord(k) ^ ord(char))
        print(k, clear)


def xor_cipher_crack_two_digit_key(cipher: str):
    undo_cipher = binascii.unhexlify(cipher.encode('ascii'))
    for k1 in '0123456789':
        for k2 in '0123456789':
            result = ''
            for i in range(len(undo_cipher)):
                char = undo_cipher[i]
                if i % 2 != 0:
                    result += chr(ord(k1) ^ char)
                else:
                    result += chr(ord(k2) ^ char)
            print('{} {} {}'.format(k1, k2, result))


def main():
    to_cipher = input('Enter a message to cipher: ')
    offset = input('Enter an offset (leave blank to use default): ')
    while not offset.isdigit() and len(offset) != 0:
        print('That was not a number')
        offset = input('Enter an offset (leave blank to use default): ')
    if len(offset) != 0:
        offset = int(offset)
        caesar = caesar_cipher(to_cipher, offset)
    else:
        caesar = caesar_cipher(to_cipher)
    key = input('Enter a key (for XOR cipher): ')
    xor = xor_cipher(to_cipher, key)
    print(f'Obfuscated version of the message using caesar cipher: {caesar}')
    print('Obfuscated version of the message using ROT13: ' + rot13(to_cipher))
    print('Obfuscated version of the message using base64: ' + base64cipher(bytes(to_cipher, 'utf')).decode('utf-8'))
    print('Obfuscated version of the message using {} as key in xor: {}'.format(key, xor))
    print('Cracking caesar cipher...')
    caesar_crack(caesar)
    print('Cracking xor cipher...')
    xor_cipher_crack_one_digit_key(to_cipher)


if __name__ == "__main__":
    xor_cipher_crack_two_digit_key('70155d5c45415d5011585446424c')
    # main()
