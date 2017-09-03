import click
from slogger.cli import pass_context, db
from tinydb import Query


@click.command()
@click.option('--project', prompt='Project', default='all', help="Project name to read")
@pass_context
def cli(ctx, project):
    """Print messages logged for Project"""
    ctx.debug(db.all())

    if project == 'all':
        for item in iter(db):
            print_data(ctx, item)
    else:
        print_data(ctx, project)


def print_data(ctx, project):
    Project = Query()
    data = db.search(Project.project == project)
    ctx.info("Project: %s" % project)
    for item in data:
        ctx.debug(item)
        print("Message: %s" % item['message'])
