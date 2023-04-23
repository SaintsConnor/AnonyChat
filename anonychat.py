import argparse
import sys

from client import Client
from server import Server


def parse_args():
    parser = argparse.ArgumentParser(description='AnonyChat command line interface.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--server', help='run as server', action='store_true')
    group.add_argument('-c', '--client', help='run as client', action='store_true')
    parser.add_argument('-a', '--address', help='specify server address to connect to')
    parser.add_argument('-p', '--port', help='specify server port to connect to', type=int)
    return parser.parse_args()


def main():
    args = parse_args()

    if args.server:
        server = Server()
        server.start()
    elif args.client:
        if not args.address or not args.port:
            print('Error: Please specify server address and port to connect to.')
            sys.exit(1)
        client = Client(args.address, args.port)
        client.start()


if __name__ == '__main__':
    main()
