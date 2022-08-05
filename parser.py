import argparse
from _version import __version__

def formatter(indent_increment=2, max_help_position=40, width=None):
    return lambda prog: argparse.HelpFormatter(
        prog,
        indent_increment,
        max_help_position,
        width,
    )

parser = argparse.ArgumentParser(
    prog="stockholm",
    description="Encrypt all your files in the \"infected\" directory! (:",
    argument_default=argparse.SUPPRESS,
    formatter_class=formatter(),
)

parser.add_argument(    # Version
    '-v', '--version',
    action="version",
    version="%(prog)s v"+__version__+"",
    help="show the current program version",
)

parser.add_argument(    # Reverse infection
    "-r", "--reverse",
    action='store_true',
    help="reverse the encrypted files",
)
parser.set_defaults(reverse=False)  # Set False by default

parser.add_argument(    # Silent output infected files
    "-s", "--silent",
    action="store_true",
    help="don't output the encripted files",
)
parser.set_defaults(silent=False)

args = parser.parse_args()
