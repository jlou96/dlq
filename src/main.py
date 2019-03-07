import datetime
import os.path

from re import match

import .argparser
import .scheduler
import .util


def main():
    parser = argparser.build_parser()
    args = parser.parse_args()

    config = util.get_config()
    util.check_missing_args(args, config)
    util.check_valid_args(args)

    values = util.get_values(args, config)
    
    scheduler.handle(values)
