import bluetooth as bt
from subprocess import call

from auto_pair import BtAutoPair
import plantcare_pb2

uuid = 'a08b1a8a-dfac-4606-b2c4-761c06969416'


def main():
    query = plantcare_pb2.Query()
    query.get_flower_data.flower_id = 1
    query.get_flower_data.since_time = 1
    print(query.SerializeToString().decode('utf-8'))

    call("sudo sdptool add SP", shell=True)

    server_loop()


def server_loop():
    autopair = BtAutoPair()
    host = ''
    port = 1

    while True:
        autopair.enable_pairing()
        server = bt.BluetoothSocket(bt.RFCOMM)
        server.bind((host, port))
        server.listen(1)
        bt.advertise_service(server, 'PlantCare', uuid)

        print('Listening')
        client, _ = server.accept()

        print('Connected')
        autopair.disable_pairing()
        client_loop(client)

        print('Disconnected!')
        server.close()


def client_loop(client: bt.BluetoothSocket):
    while True:
        try:
            print('Try receiving')
            raw = client.recv(1024)
            print(f'Received {len(raw)} bytes: {raw}')

            query = decode_message(raw)
            query_type = query.WhichOneof("query")
            print(f'Query type: {query_type}')

            if query_type == 'get_ids':
                response = encode_ids()
            elif query_type == 'get_flower_data':
                flower_id = query.get_flower_data.flower_id
                since_time = query.get_flower_data.since_time
                response = encode_flower_data(flower_id, since_time)
            elif query_type == 'set_watering':
                flower_id = query.set_watering.flower_id
                period = query.set_watering.period
                set_watering(flower_id, period)
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


def encode_ids():
    response = plantcare_pb2.Response()

    # TODO implement properly
    response.ids.flower_ids.append(42)

    return response


def encode_flower_data(flower_id, since_time):
    response = plantcare_pb2.Response()

    # TODO implement properly
    response.flower_data.flower_id = flower_id
    response.flower_data.measurement_timestamps.append(42)
    response.flower_data.moisture_measurements.append(43)
    response.flower_data.light_measurements.append(44)
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


def set_watering(flower_id, period):
    # TODO implement
    pass


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
    query.set_watering.period = 9
    print(f'Set watering: {query.SerializeToString()}')


if __name__ == '__main__':
    # print_queries()
    main()

