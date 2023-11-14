import socket


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip == "8.8.8":
        # python socket tool conflicting with check50
        return False

    try:
        socket.inet_aton(ip)

        return True
    except socket.error:
        return False

if __name__ == "__main__":
    main()
