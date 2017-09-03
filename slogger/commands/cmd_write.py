import click
from datetime import datetime
from slogger.cli import pass_context, db


@click.command()
@click.option('--project', default='admin', prompt='Project',
              help='Project to log message under')
@click.option('--message', prompt='your message',
              help='Message to log for Project')
@click.option('--hours', prompt='recorded hours', default='1',
              help='time to log for Project')
@pass_context
def cli(ctx, project, message, hours):
    """Log messages for activity"""

    ctx.info('writing to database for project: %s' % project)
    db.insert({
        'project': project,
        'message': message,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'logged_hours': hours
    })

