import click
from datetime import datetime
from slogger.cli import pass_context, db


@click.command()
@click.option('--force', default=False,
              required=False,
              prompt='Type \'true\' to proceed',
              help='Project to log message under')
@pass_context
def cli(ctx, force):
    """Log messages for activity"""
    if force == 'true':
        ctx.info("Purging Database")
        db.purge()
    else:
        ctx.info("Purge failed, must pass --force=true")