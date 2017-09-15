import click
from slogger.cli import pass_context, db


@click.command()
@click.argument('eid')
@click.option('-m', '--message',
              help='Message to log for Project')
@click.option('-h', '--hours',
              help='time to log for Project')
@pass_context
def cli(ctx, eid, message, hours):
    """Log messages for activity"""

    if message:
        db.update({'message': message}, eids=[int(eid)])
    elif hours:
        db.update({'logged_hours': hours}, eids=[int(eid)])

    ctx.info('db updated')
