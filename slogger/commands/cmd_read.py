import click
from slogger.cli import pass_context, db
from tinydb import Query


@click.command()
@click.option('--project', prompt='Project', help="how many helps??")
@pass_context
def cli(ctx, project):
    """Print messages logged for Project"""
    ctx.debug(db.all())
    ctx.info('Querying db for project')

    Project = Query()
    data = db.search(Project.project == project)
    print("Project: %s" % data)

    ctx.info("Print messages for project")
    for item in data:
        print("Message: %s" % item['message'])
