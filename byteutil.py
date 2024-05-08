def int_to_bytes(value: int):
    byte_str = b""

    filled_bytes = value // 255
    last_byte_value = value % 255

    for _ in range(0, filled_bytes):
        byte_str += b"\xff"
    byte_str += int(last_byte_value).to_bytes(1, "big")

    for _ in range(0, (16-filled_bytes)-1):
        byte_str += b"\x00"
    
    return byte_str
    
def bytes_to_int(value: bytes):
    hex_values = value.hex(" ").split(" ")
    total = 0

    for val in hex_values:
        total += int(val, 16)
    return total