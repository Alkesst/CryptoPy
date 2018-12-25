import base64
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"


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


def main():
    to_cipher = input('Enter a message to cipher: ')
    offset = input('Enter an offset (leave blank to use default): ')
    while not offset.isalnum() and len(offset) != 0:
        print('That was not a number')
        offset = input('Enter an offset (leave blank to use default): ')
    if len(offset) != 0:
        offset = int(offset)
        caesar = caesar_cipher(to_cipher, offset)
    else:
        caesar = caesar_cipher(to_cipher)
    print('Obfuscated version of the message using caesar cipher: ' + caesar)
    print('Obfuscated version of the message using ROT13: ' + rot13(to_cipher))
    print('Obfuscated version of the message using base64: ' + base64cipher(bytes(to_cipher, 'utf')).decode('utf-8'))


if __name__ == "__main__":
    main()
