import base64


def encode_file(path: str) -> bytes:
    with open(path, 'rb') as file:
        data = file.read()
        encoded_file = base64.b64encode(data)
    return encoded_file


def decode_file(encoded_file: bytes) -> bytes:
    return base64.b64decode(encoded_file)


def create_new_file_with_decoded_info(path: str, decoded_file: bytes):
    with open(path, 'wb+') as new_file:
        new_file.write(decoded_file)


def main():
    path = input('Path from file to open: ')
    encoded = encode_file(path)
    path = input('Path from new file: ')
    create_new_file_with_decoded_info(path, decode_file(encoded))


if __name__ == "__main__":
    main()
