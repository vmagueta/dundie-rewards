from importlib import metadata

import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GRUOP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(metadata.version("dundie"))
def main():
    """Dunder Mifflin Rewards System.

    This CLI application controls Dunder Mifflin Rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database.

    ## Features

    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "e-mail"]
    for header in headers:
        table.add_column(header, style="italic cyan1")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[field.strip() for field in person.split(",")])

    console = Console()
    console.print(table)
