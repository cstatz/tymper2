import hid
import struct
from time import sleep

print hid.enumerate()
d = hid.device()

#0x0c45, 0x7401
d.open_path('USB_0c45_7401_14200000')
d.set_nonblocking(1)

for i in range(1000):

    # Read Temperature 1 and 2 
    d.write([0x01,0x80,0x33,0x01,0x00,0x00,0x00,0x00])
    sleep(0.1)
    data = d.read(8)
    d.read(8)
    data_s = "".join([chr(byte) for byte in data])
    temp_c_1 = 125.0/32000.0 * (struct.unpack('>h', data_s[2:4])[0])
    temp_c_2 = 125.0/32000.0 * (struct.unpack('>h', data_s[4:6])[0])

    print temp_c_1, temp_c_2
    sleep(0.2)

d.close()
