import argparse

def vl64_encode_len(v):
    """Returns the number of bytes required to represent a variable-length base64-encoded integer."""
    if v < 0:
        v = -v
    return (v.bit_length() + 9) // 6

def vl64_decode_len(b):
    """Returns the byte length of a variable-length base64-encoded integer, given (and including) the first byte."""
    return (b >> 3) & 7

def vl64_encode(v):
    """Encodes an integer to variable-length base64 and returns the resulting byte array."""
    abs_v = abs(v)
    n = vl64_encode_len(v)
    b = bytearray(n)

    b[0] = 64 | ((n & 7) << 3) | (abs_v & 3)
    if v < 0:
        b[0] |= 4
    
    for i in range(1, n):
        b[i] = 64 | ((abs_v >> (2 + 6 * (i - 1))) & 0x3f)
    
    return b

def vl64_decode_verbose(s):
    """Decodes a variable-length base64-encoded string from the given input, outputting detailed results."""
    base_offset = 64
    decoded_values = []

    i = 0
    while i < len(s):
        startCode = ord(s[i])
        finish = (startCode - 72 + 8) // 8
        code1 = startCode - 64 - 8 * finish
        otherCodes = 0
        multiplier = 4

        for count in range(finish - 1):
            i += 1
            otherCodes += multiplier * (ord(s[i]) - base_offset)
            multiplier *= 64

        decodedValue = code1 + otherCodes if code1 < 4 else 4 - code1 + otherCodes
        processedString = s[i-finish+1:i+1]
        decoded_values.append(f"{processedString} = {decodedValue}")
        i += 1
    
    return decoded_values

def main():
    parser = argparse.ArgumentParser(description="VL64 Encoder/Decoder")
    parser.add_argument('--encode', type=int, help="Encode an integer to VL64 format")
    parser.add_argument('--decode', type=str, help="Decode a VL64 formatted string")

    args = parser.parse_args()

    if args.encode is not None:
        encoded = vl64_encode(args.encode)
        encoded_string = ''.join(chr(b) for b in encoded)
        print(f"Encoded: {encoded_string}")
    elif args.decode is not None:
        decoded_values = vl64_decode_verbose(args.decode)
        for decoded in decoded_values:
            print(decoded)
    else:
        print("Please specify either --encode or --decode with a value.")

if __name__ == "__main__":
    main()