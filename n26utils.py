from envparse import env
import socket
import ssl
from codecs import encode


class Props:

    RESOLVER_HOSTNAME = env('RESOLVER_HOSTNAME', "cloudflare-dns.com")
    RESOLVER_IP = env('RESOLVER_IP', "1.1.1.1")
    RESOLVER_PORT = int(env('RESOLVER_TLSPORT', 853))

    BIND_HOST = env('APP_BINDHOST', "")
    BIND_PORT = int(env('APP_BINDPORT', 53))
    APP_MODE = env('APP_MODE', "TCP")  # UDP, HYBRID, etc.

    THREAD_TIMEOUT = 3


class DnsRequest:

    def resolve(query, isUDP):
        server = (Props.RESOLVER_IP, Props.RESOLVER_PORT)
        cx = ssl.create_default_context()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            with cx.wrap_socket(sock, server_hostname=Props.RESOLVER_HOSTNAME) as ssock:
                ssock.connect(server)

                if (isUDP):
                   size = encode(chr(len(query)))
                   query =  b"\x00"+ size + query

                ssock.send(query)
                data = ssock.recv(1024)
                return data
