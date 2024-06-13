import mfrc522
import byteutil

rdr = mfrc522.MFRC522(18, 19, 16, 20, 17)

def read_raw():
    out = None
    

    while out == None:
        print("reading...")
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:

            (stat, raw_uid) = rdr.anticoll()

            if stat == rdr.OK:

                if rdr.select_tag(raw_uid) == rdr.OK:

                    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                    if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                        out = rdr.read(8)
                        rdr.stop_crypto1()
                    else:
                        print("Authentication error")
                else:
                    print("Failed to select tag")
        else:
            print(stat)
    
    return out


def write_raw(data = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"):

    written = False
    while not written:
        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:

            (stat, raw_uid) = rdr.anticoll()

            if stat == rdr.OK:

                if rdr.select_tag(raw_uid) == rdr.OK:

                    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                    if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                        stat = rdr.write(8, data)
                        rdr.stop_crypto1()
                        if stat == rdr.OK:
                            print("Data written to card")
                            written = True
                        else:
                            print("Failed to write data to card")
                    else:
                        print("Authentication error")
                else:
                    print("Failed to select tag")

if __name__ == "__main__":
    print(write_raw())
    print(read_raw())