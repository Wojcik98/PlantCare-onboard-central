import sys
import smbus
from time import sleep

COIL_ON_CMD = 1
COIL_OFF_CMD = 2

ACK = 42


if __name__ == '__main__':
    device = int(sys.argv[1])
    bus = smbus.SMBus(1)

    bus.write_byte(device, COIL_ON_CMD)
    sleep(4)
    bus.read_byte(device)

    bus.write_byte(device, COIL_OFF_CMD)
    sleep(0.05)
    bus.read_byte(device)
