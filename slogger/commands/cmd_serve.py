import click
from slogger.cli import pass_context, db
from flask import Flask

app = Flask(__name__)


@app.route('/db')
@pass_context
def database(ctx):
    # Send message back to client
    message = "%s" % db.all()
    return message


@click.command()
@pass_context
def cli(ctx):
    ctx.info('running server...')
    app.run()
