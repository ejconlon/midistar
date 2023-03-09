#!/usr/bin/env python3

import re
import subprocess


CLIENT_RE = re.compile('^client (\d*)\: \'(.*)\'')


def find_clients():
    output = subprocess.check_output(['aconnect', '-i', '-l'])
    lines = output.decode().split('\n')
    clients = []
    for line in lines:
        match = CLIENT_RE.search(line)
        if match is not None:
            port = int(match.group(1))
            name = match.group(2).strip()
            if port == 0 or 'Through' in name:
                continue
            else:
                print(f'Found client {port} ({name})')
                clients.append((port, name))
    return clients


def connect_all(clients):
    for (port1, name1) in clients:
        for (port2, name2) in clients:
            if port1 == port2:
                continue
            else:
                print(f'Connecting {port1} ({name1}) to {port2} ({name2})')
                subprocess.check_call(['aconnect', f'{port1}:0', f'{port2}:0'])


def main():
    print('Finding clients')
    clients = find_clients()
    print('Connecting clients')
    connect_all(clients)
    print('Done')


if __name__ == '__main__':
    main()
