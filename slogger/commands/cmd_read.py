import click
from slogger.cli import pass_context


@click.command('read', short_help='read tinydb')
@pass_context
def cli(ctx):
    """Read"""
    ctx.log('log')
    ctx.vlog('vlog')
