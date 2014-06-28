import struct
little_endian = (struct.unpack('<I', struct.pack('=I', 1))[0] == 1)
if little_endian:
    print("LittleEndian")
else:
    print("BigEndian")