import hashlib 
import json

def crypto_hash(*args):
    """
    Return a SHA-256 hash of the given arguments.
    """
    # lambda: stringify, dumps orignal data into a string
    # sorted, so that no matter the order of input, same hash produced
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    #print(f'stringified_args: {stringified_args}')
    joined_data = ''.join(stringified_args)
    #print(f'joined_data: {joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one, [2], 3'): {crypto_hash('one', [2], 3)}")

if __name__ == '__main__':
    main()