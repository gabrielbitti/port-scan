import socket
import sys

arguments_list = sys.argv
arguments_list.pop(0)
target = arguments_list[0]
arguments_list.pop(0)

ports_to_scan = arguments_list
for port in ports_to_scan:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    code = client.connect_ex((target, int(port)))

    if code == 0:
        print('Port {} OPEN'.format(port))
