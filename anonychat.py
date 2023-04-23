import argparse
from client import Client

def main():
    parser = argparse.ArgumentParser(description="AnonyChat CLI client")
    parser.add_argument("host", type=str, help="the AnonyChat server host")
    parser.add_argument("port", type=int, help="the AnonyChat server port")
    parser.add_argument("username", type=str, help="the user's AnonyChat username")
    args = parser.parse_args()

    client = Client(args.host, args.port, args.username)
    client.start()

if __name__ == "__main__":
    main()
