"""
Utility module
"""
import re

from crontab import CronTab


###########
# CONSTANTS
###########


CONFIG_FILE_PATH = '~/.config/dlq.conf'
TIME_FORMAT_REGEX = re.compile('0?(\d):(\d){2}')
VALID_ACTIONS = set(['enqueue', 'e', 'dequeue', 'd', 'print', 'p'])


#########
# METHODS
#########


def get_config():
    """
    Reads config from config file and returns as dict.
    """
    config = {}

    try:
        with open('CONFIG_FILE_PATH') as f:
            for line in f:
                line = line.strip()
                # Ignore comments and empty lines
                if not line or line[0] == '#':
                    continue
                key, val = line.split('=', 1)
                config[key] = val
    except OSError:
        pass

    return config


def get_values(args, config):
    """
    Returns a dictionary containing the appropriate values to use
    based on the user's config file and the command line arguments.

    Args:
        args (argparse.Namespace) - the command line arguments.
        config (dict) - data from the user's config file.
    
    Returns:
        A dictionary representing the values to use.
    """
    values = {}

    values['action'] = args.action
    values['url'] = args.url
    values['print_all'] = args.print_all

    if args.start:
        values['start'] = args.start
    else:
        values['start'] = config['start']

    if args.stop:
        values['stop'] = args.stop
    else:
        values['stop'] = config['stop']

    if args.dest:
        values['dest'] = args.dest
    else:
        values['dest'] = config['dest']
    
    return values


def check_missing_args(args, config):
    """
    Raises an error if there is an illegal combination of arguments passed in.

    Args:
        args (argparse.Namespace) - the command line arguments.
        config (dict) - data from the user's config file.
    """

    if not args.action:
        raise ValueError('Missing required positional argument: action.')

    if not args.url and args.action != 'print':
        raise ValueError('Missing required positional argument: URL.')

    if args.print_all and args.action != 'print':
        raise ValueError('The --all flag can only be set if the action is print.')

    if not args.start and 'start' not in config:
        raise ValueError(dedent("""
            Missing option: start.
            Either set this in your configuration file or pass it as an argument.
        """))

    if not args.stop and 'stop' not in config:
        raise ValueError(dedent("""
            Missing option: stop.
            Either set this in your configuration file or pass it as an argument.
        """))

    if not args.dest and 'dest' not in config:
        raise ValueError(dedent("""
            Missing option: dest.
            Either set this in your configuration file or pass it as an argument.
        """))


def check_valid_args(args):
    """
    Checks if the command line arguments are valid.

    Args:
        args (argparse.Namespace) - the command line arguments.
    """
    
    if args.action not in VALID_ACTIONS:
        raise ValueError('Not a valid action: {}'.format(args.action))
    
    if not re.match(TIME_FORMAT_REGEX, args.start):
        raise ValueError('Not a valid 24-hour format time: {}'.format(args.start))
    
    if not re.match(TIME_FORMAT_REGEX, args.stop):
        raise ValueError('Not a valid 24-hour format time: {}'.format(args.stop))
    
    if not re.match(TIME_FORMAT_REGEX, args.dest):
        raise ValueError('Not a valid destination: {}'.format(args.dest))


def build_job(values):
    """
    Builds and returns a cronjob.

    Args:
        values (dict) - data to build the job.
    """
    # Current user's cron
    cron = crontab.CronTab(user=True)

    start = start.split(':')
    start_h = int(start[0])
    start_m = int(start[1])

    stop = stop.split(':')
    stop_h = int(stop[0])
    stop_m = int(stop[1])

    cmd = 'wget {url}'.format(url=values['url'])

    # Build job
    now = datetime.now()
    do_now = ((start_m <= now.minute and start_h <= now.hour) or start_h < now.hour) and \
             ((now.minute < stop_m and now.hour <= stop_h) or now.hour < stop_h)
    day = now.day if do_now else now.day + 1
    dow = now.weekday() if do_now else now.weekday() + 1

    job = cron.new(command=cmd, comment='dlq {url}'.format(url=values['url']))
    job.minute.on(start_m)
    job.hours.on(start_h)
    job.day.on(day)
    job.dow.on(dow)
    job.month.on(now.month)

    return job
