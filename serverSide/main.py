from crypt import methods

import requests
import ascii
import logins

from flask import Flask, request, render_template
from http.server import BaseHTTPRequestHandler, HTTPServer

app: Flask = Flask (__name__)



@app.route('/CLICK')
def click():
    if request.method=='POST':
        username = request.form['NICKNAME']
        password = request.form['PASSWORD']

        if request.form('username,password') in logins:
            print("welcome to the server")

        pass


def check_connection():
    pass


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(ascii.ascii_art.encode('utf-8'))

    def send_response(self, status_code):
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(data.encode('utf-8',))

    def end_headers(self):
        if not self.client_address:  # for client
            # do something else
            pass
        else:  # for server
            # do something with the client address
            pass


def main():
    addrs = ('localhost', 8000)
    server = HTTPServer(addrs, RequestHandler)
    server.serve_forever()


def send_message(client, host, port, message):
    if client:
        # do something for client
        pass
    else:
        # do something for server
        if message_format not in ["text", "string"]:
            raise Exception("Unsupported text")

        data = message.encode("utf-8")
        response = requests.get(f"http://{host}:{port}")
        print(response.status_code)
        print(response.content)

if __name__ == '__main__':
    message = "hello world"
    send_message(False, "localhost", 8000, message) # for server
    send_message(True, "localhost", 8000, message)  # for client
    main()
