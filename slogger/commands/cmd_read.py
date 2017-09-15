import click
from slogger.cli import pass_context, db
from tinydb import Query
from beautifultable import BeautifulTable

table = BeautifulTable()
table.column_headers = ["eid", "hours", "project", "message"]


@click.command()
@click.option('--project', prompt='Project', default='all', help="Project name to read")
@pass_context
def cli(ctx, project):
    """Print messages logged for Project"""
    ctx.debug(db.all())

    elements = []

    if project == 'all':
        for item in iter(db):
            elements.append(item['project'])
        trimmed_elements = set(elements)
        for element in trimmed_elements:
            print_data(ctx, element)
    else:
        print_data(ctx, project)

    table.column_alignments['message'] = BeautifulTable.ALIGN_LEFT
    table.column_alignments['project'] = BeautifulTable.ALIGN_LEFT
    print(table)


def print_data(ctx, project):
    Project = Query()
    data = db.search(Project.project == project)
    for item in data:
        ctx.debug(item)
        table.append_row([item.eid, item['logged_hours'], item['project'], item['message']])
