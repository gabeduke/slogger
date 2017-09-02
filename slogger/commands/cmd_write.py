import click
import os
from tinydb import TinyDB, Query
from datetime import datetime
from slogger.cli import pass_context


@click.command()
@click.option('--project', required=False, default='default', prompt='Project', help='Project to log message under')
@click.option('--message', prompt='your message',
              help='Message to log for Project')
@pass_context
def cli(ctx, project, message):
    """Log messages for activity"""
    ctx.log('writing ')
    ctx.vlog('bla bla bla, debug info')
    db = TinyDB(os.path.expanduser('~/.slogger.json'))
    db.insert({'project': project, 'message': message})

