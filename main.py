import socket
import sys

try:
    arguments_list = sys.argv
    arguments_list.pop(0)
    if len(arguments_list) == 0:
        raise Exception('Missing host.')

    target = arguments_list[0]

    if len(arguments_list) <= 1:
        raise Exception('Missing ports number.')

    ports_to_scan = arguments_list[1:]
except Exception as e:
    print(e)
    exit(0)

for port in ports_to_scan:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    code = client.connect_ex((target, int(port)))
    if code == 0:
        print('Port {} OPEN'.format(port))
