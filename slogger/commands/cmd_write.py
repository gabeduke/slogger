import click
from datetime import datetime
from slogger.cli import pass_context, db


@click.command()
@click.option('--project', required=False, default='default', prompt='Project', help='Project to log message under')
@click.option('--message', prompt='your message',
              help='Message to log for Project')
@pass_context
def cli(ctx, project, message):
    """Log messages for activity"""
    ctx.info('writing ')
    ctx.debug('bla bla bla, debug info')
    db.insert({'project': project, 'message': message})

