import os
import sys
import click
from tinydb import TinyDB


CONTEXT_SETTINGS = dict(auto_envvar_prefix='SLOGGER')


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def warning(self, msg, *args):
        """Logs a warning to stderr."""
        self.log(click.style("## WARNING - %s" % msg, *args, fg='yellow'))

    def error(self, msg, *args):
        """Logs an error to stderr."""
        self.log(click.style("## ERROR - %s" % msg, *args, fg='red'))

    def info(self, msg, *args):
        """Logs an info message to stderr."""
        self.log(click.style("## INFO - %s" % msg, *args, fg='blue'))

    def debug(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(click.style("DEBUG - %s" % msg, *args, fg='green'))


pass_context = click.make_pass_decorator(Context, ensure=True)
db = TinyDB(os.path.expanduser('~/.slogger.json'))
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('slogger.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@pass_context
def cli(ctx, verbose):
    """Logging interface to add messages to a file based on project"""
    ctx.verbose = verbose

if __name__ == "__main__":
    cli()