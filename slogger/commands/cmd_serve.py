import click
from slogger.cli import pass_context, db
from http.server import BaseHTTPRequestHandler, HTTPServer


class DataServer(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "%s" % db.all()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return


@click.command()
@pass_context
def cli(ctx):

    ctx.info('starting server...')
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, DataServer)

    ctx.info('running server...')
    click.launch('http://127.0.0.1:8081')
    httpd.serve_forever()
