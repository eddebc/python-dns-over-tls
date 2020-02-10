import socketserver
import threading
from n26utils import DnsRequest, Props

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} Processing TCP request .. ".format(threading.current_thread()))
        result = DnsRequest.resolve(self.data, False)
        self.request.sendall(result)


if __name__ == "__main__":

    def run():
        serverInfo = (Props.BIND_HOST, Props.BIND_PORT)
        servers = []

        if ((Props.APP_MODE == "TCP") | True):
            servers.append(socketserver.ThreadingTCPServer(serverInfo, TCPHandler, True))

        for server in servers:
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            server_thread.join(Props.THREAD_TIMEOUT)

        # Keep main thread alive
        while (True):
            threading.Event().wait()
    # App Start
    run()
