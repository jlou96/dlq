"""
Inspired by Streamlink's implementation of their argparser.
https://github.com/streamlink/streamlink/blob/master/src/streamlink_cli/argparser.py
"""

import argparse
from textwrap import dedent


class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    """A nicer help formatter.

    Help for arguments can be indented and contain new lines.
    It will be de-dented and arguments in the help will be
    separated by a blank line for better readability.

    Originally written by Jakub Roztocil of the httpie project.
    """

    def __init__(self, max_help_position=4, *args, **kwargs):
        # A smaller indent for args help.
        kwargs["max_help_position"] = max_help_position
        argparse.RawDescriptionHelpFormatter.__init__(self, *args, **kwargs)

    def _split_lines(self, text, width):
        text = dedent(text).strip() + "\n\n"
        return text.splitlines()


def build_parser():
    parser = argparse.ArgumentParser(
        prog='dlq',
        usage='dlq [OPTIONS] <URL> <START> <STOP>',
        description='A command-line utility for scheduling download jobs.',
        epilog='Visit github.com/jlou96/dlq for detailed documentation.',
        formatter_class=HelpFormatter
    )

    # Positional arguments
    positional = parser.add_argument_group('Positional arguments')

    positional.add_argument(
        'url',
        metavar='URL',
        nargs='?',
        help="""
        A URL to attempt to download from.

        Unless specified, the protocol will be HTTP(S).
        """
    )

    positional.add_argument(
        'start',
        metavar='START',
        nargs='?',
        help="""
        The time at which the job is queued to start.

        This argument is required to be passed in 24-hour format.
        For example, 02:00 would queue the job to start at 2 a.m., local time.
        """
    )
    
    positional.add_argument(
        'stop',
        metavar='STOP',
        nargs='?',
        help="""
        The time at which the job is meant to stop.

        This argument is required to be passed in 24-hour format.
        For example, 08:00 would queue the job to start at 8 a.m., local time.
        """
    )

    # General arguments
    general = parser.add_argument_group('General arguments')

    general.add_argument(
        '--dest',
        metavar='DESTINATION',
        nargs='?',
        default='~/Downloads',
        help="""
        The directory in which the file will be downloaded.

        If not specified, this will default to $HOME/Downloads
        """
    )
