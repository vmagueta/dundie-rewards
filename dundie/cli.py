import argparse
from dundie.core import load


def main():
    parser = argparse.ArgumentParser(
        description="Dundler Mifflin Rewards CLI",
        epilog="Enjoy and use with cautious.",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help"
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="Filepath to load",
        default=None
    )
    args = parser.parse_args()


    print(*globals()[args.subcommand](args.filepath))