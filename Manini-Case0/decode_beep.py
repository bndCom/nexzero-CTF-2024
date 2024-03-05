code = "01101110011001010111100001110101011100110011001000110000001100100011010001000000"

bytes_list = [code[i:i+8] for i in range(0, len(code), 8)]
decoded_message = ''.join([chr(int(byte, 2)) for byte in bytes_list])

print(decoded_message)
