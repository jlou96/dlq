"""
Inspired by Streamlink's implementation of their argparser.
https://github.com/streamlink/streamlink/blob/master/src/streamlink_cli/argparser.py
"""

import argparse
from textwrap import dedent


class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    """
    A nicer help formatter.

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
    """
    Builds the argument parser.

    An in-depth documentation on valid arguments
    and their usage can be found in the README.

    Returns:
        The argument parser.
    """
    parser = argparse.ArgumentParser(
        prog='dlq',
        usage='dlq [OPTIONS] <URL>',
        description='A command-line utility for scheduling download jobs.',
        epilog='Visit github.com/jlou96/dlq for detailed documentation.',
        formatter_class=HelpFormatter
    )

    # Positional arguments
    positional = parser.add_argument_group('Positional arguments')

    positional.add_argument(
        'action',
        metavar='ACTION',
        nargs='?',
        default='enqueue'
        help="""
        The action to execute.

        Can be one of the following options:
        * enqueue <URL>
        * dequeue <URL>
        * print

        Unless specified, the action will be enqueue.
        """
    )

    positional.add_argument(
        'url',
        metavar='URL',
        nargs='?',
        default=''
        help="""
        A URL to attempt to download from.

        Unless specified, the protocol will be HTTP(S).
        """
    )

    # Optional arguments
    optional = parser.add_argument_group('General arguments')

    optional.add_argument(
        '--start',
        metavar='START',
        nargs='?',
        dest='start',
        help="""
        The time at which the job is queued to start.

        This argument is required to be passed in 24-hour format.
        For example, 02:00 would queue the job to start at 2 a.m., local time.
        """
    )
    
    optional.add_argument(
        '--stop',
        metavar='STOP',
        nargs='?',
        dest='stop',
        help="""
        The time at which the job is meant to stop.

        This argument is required to be passed in 24-hour format.
        For example, 08:00 would queue the job to start at 8 a.m., local time.
        """
    )

    optional.add_argument(
        '--dest', '-d',
        metavar='DEST',
        nargs='?',
        dest='dest',
        default='~/Downloads',
        help="""
        The directory in which the file will be downloaded.

        If not specified, this will default to '$HOME/Downloads'.
        """
    )

    # Flags
    flags = parser.add_argument_group('Flags')

    flags.add_argument(
        '--all', '-a',
        metavar='PRINT_ALL',
        action='store_true',
        dest='print_all',
        help="""
        When passed along with a print command, prints all existing jobs.
        """
    )

    return parser
