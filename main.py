import bluetooth as bt
from subprocess import call, run
import sqlite3

from auto_pair import BtAutoPair
import plantcare_pb2

uuid = 'a08b1a8a-dfac-4606-b2c4-761c06969416'


def main():
    setup_pairing()
    server_loop()


def setup_pairing():
    autopair = BtAutoPair()
    autopair.disable_pairing()
    autopair.enable_pairing()
    call("sudo sdptool add SP", shell=True)


def server_loop():
    host = ''
    port = 1
    connection = sqlite3.connect('plantcare.db')
    cursor = connection.cursor()

    while True:
        server = bt.BluetoothSocket(bt.RFCOMM)
        server.bind((host, port))
        server.listen(1)
        bt.advertise_service(server, 'PlantCare', uuid)

        print('Listening')
        client, _ = server.accept()
        print('Connected')
        client_loop(client, cursor)

        print('Disconnected!')
        server.close()


def client_loop(client: bt.BluetoothSocket, cursor: sqlite3.Cursor):
    while True:
        try:
            print('Try receiving')
            raw = client.recv(1024)
            print(f'Received {len(raw)} bytes: {raw}')

            query = decode_message(raw)
            query_type = query.WhichOneof("query")
            print(f'Query type: {query_type}')

            if query_type == 'get_ids':
                response = encode_ids(cursor)
            elif query_type == 'get_flower_data':
                flower_id = query.get_flower_data.flower_id
                since_time = query.get_flower_data.since_time
                response = encode_flower_data(flower_id, since_time, cursor)
            elif query_type == 'set_watering':
                flower_id = query.set_watering.flower_id
                hour = query.set_watering.hour
                days = query.set_watering.days
                set_watering(flower_id, hour, days, cursor)
                response = encode_watering_set()
            else:
                continue

            raw_send = response.SerializeToString()
            client.send(raw_send)
            print(f'Sent {len(raw_send)} bytes: {raw_send}')

        except Exception as e:
            print(e)
            client.close()
            break


def encode_ids(cursor: sqlite3.Cursor):

    rows = cursor.execute('SELECT * FROM flower_ids')
    ids = [id_ for (id_,) in rows]
    print(f'Ids: {ids}')

    response = plantcare_pb2.Response()
    response.ids.flower_ids.extend(ids)

    return response


def encode_flower_data(flower_id, since_time, cursor: sqlite3.Cursor):
    print(f'Device: {flower_id}, since_time: {since_time}')
    query = f'SELECT * FROM readings ' \
            f'WHERE flower_id = {flower_id} AND timestamp > {since_time}'
    rows = cursor.execute(query)
    rows = [row for row in rows]
    print(rows)

    timestamps = [timestamp for (_, _, _, timestamp) in rows]
    lights = [light for (_, light, _, _) in rows]
    moistures = [moisture for (_, _, moisture, _) in rows]
    print(f'Timestamps: {timestamps}')
    print(f'Lights: {lights}')
    print(f'Moistures: {moistures}')

    response = plantcare_pb2.Response()
    response.flower_data.flower_id = flower_id
    response.flower_data.measurement_timestamps.extend(timestamps)
    response.flower_data.light_measurements.extend(lights)
    response.flower_data.moisture_measurements.extend(moistures)
    response.flower_data.watering_timestamps.append(45)

    return response


def encode_watering_set():
    response = plantcare_pb2.Response()
    response.watering_set.SetInParent()

    return response


def decode_message(raw):
    query = plantcare_pb2.Query()
    query.ParseFromString(raw)
    return query


def set_watering(flower_id, hour, days, cursor: sqlite3.Cursor):
    print(f'flower_id: {flower_id}, hour: {hour}, days: {days}')
    cursor.execute(f'SELECT * FROM watering WHERE flower_id={flower_id}')
    exists = cursor.fetchone()

    days_string = ','.join([str(day) for day in days])
    if exists is not None:
        query = f'INSERT INTO watering VALUES ({flower_id}, {hour}, "{days_string}")'
        cursor.execute(query)
    else:
        cursor.execute(
            f'UPDATE watering '
            f'SET hour={hour}, days={days_string} '
            f'WHERE flower_id={flower_id}'
        )

    # TODO commit
    all = cursor.execute('SELECT * FROM watering')
    all = [row for row in all]

    cronjobs = []

    for (flower_id, hour, days) in all:
        schedule = f'0 {hour} * * {days}'
        cmd = f'python3 /home/pi/PlantCare-onboard-central/water.py {flower_id}'
        cronjobs.append(f'echo \'{schedule} {cmd}\'')

    combined = ';'.join(cronjobs)
    cmd = f'echo "$({combined})" | crontab -'
    run(cmd, shell=True, check=True)


def print_queries():
    query = plantcare_pb2.Query()
    query.get_ids.SetInParent()
    print(f'Get ids: {query.SerializeToString()}')

    query = plantcare_pb2.Query()
    query.get_flower_data.flower_id = 42
    query.get_flower_data.since_time = 9
    print(f'Get flower data: {query.SerializeToString()}')

    query = plantcare_pb2.Query()
    query.set_watering.flower_id = 42
    query.set_watering.hour = 9
    query.set_watering.days.append(2)
    print(f'Set watering: {query.SerializeToString()}')


if __name__ == '__main__':
    # print_queries()
    main()

