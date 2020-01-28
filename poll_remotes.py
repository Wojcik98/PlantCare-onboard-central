import smbus
from time import sleep, time
import sqlite3

MEASURE_CMD = 0
COIL_ON_CMD = 1
COIL_OFF_CMD = 2

ACK = 42
BAD_REQUEST = 33

DB_PATH = '/home/pi/PlantCare-onboard-central/plantcare.db'


def scan_devices(bus: smbus.SMBus):
    connected = []

    for device in range(20, 120):
        try:
            bus.write_quick(device)
            connected.append(device)
        except Exception:
            pass

    return connected


if __name__ == '__main__':
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    now = int(time())

    bus = smbus.SMBus(1)
    devices = scan_devices(bus)
    print(devices)

    for device in devices:
        bus.write_byte(device, MEASURE_CMD)
        sleep(0.01)

        light_high = bus.read_byte(device)
        light_low = bus.read_byte(device)
        light = (light_high << 8) + light_low

        moisture_high = bus.read_byte(device)
        moisture_low = bus.read_byte(device)
        moisture = (moisture_high << 8) + moisture_low

        cursor.execute(f'INSERT INTO readings VALUES ({device}, {light}, {moisture}, {now})')
        try:
            cursor.execute(f'INSERT INTO flower_ids VALUES ({device})')
            print(f'inserted device {device}')
        except sqlite3.IntegrityError:
            pass

        print(f'Light   : {light}')
        print(f'Moisture: {moisture}')

    connection.commit()
    connection.close()
    bus.close()
