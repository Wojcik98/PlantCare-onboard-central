import smbus
from time import sleep

MEASURE_CMD = 0
COIL_ON_CMD = 1
COIL_OFF_CMD = 2

ACK = 42
BAD_REQUEST = 33

if __name__ == '__main__':
    bus = smbus.SMBus(1)
    devices = [0x45]    # TODO scan (device is connected if read_bytes does not throw exception)

    for device in devices:
        bus.write_byte(device, MEASURE_CMD)
        sleep(0.01)

        light_high = bus.read_byte(device)
        light_low = bus.read_byte(device)
        light = (light_high << 8) + light_low

        moisture_high = bus.read_byte(device)
        moisture_low = bus.read_byte(device)
        moisture = (moisture_high << 8) + moisture_low

        print(f'Light   : {light}')
        print(f'Moisture: {moisture}')

    bus.close()
