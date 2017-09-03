import click
from slogger.cli import pass_context, db
from tinydb import Query


@click.command()
@click.option('--project', prompt='Project', help="how many helps??")
@pass_context
def cli(ctx, project):
    """Print messages logged for Project"""
    ctx.debug(db.all())

    Project = Query()
    data = db.search(Project.project == project)

    ctx.info("Project: %s" % project)
    for item in data:
        ctx.debug(item)
        print("Message: %s" % item['message'])
