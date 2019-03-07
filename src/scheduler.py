import datetime

from crontab import CronTab


cron = CronTab(tabfile='/etc/crontab', user=True)


def handle(values):
    """
    Handles an incoming job.

    Args:
        values (dict) - data to build the job.
    """
    if values['action'] == 'print':
        if values.print_all:
            print_all()
        else:
            print_job(url)
    elif values['action'] == 'dequeue':
        dequeue(values['url'])

    else:
        job = util.build_job(values)
        enqueue(job)


def enqueue(job):
    """
    Queues the input job in the user's crontab.
    For a quick primer on cronjob syntax, check the Job class.
    
    Args:
        job (CronJob) - The cronjob to be queued.
    
    Returns:
        Nothing.
    """
    cron.write_to_user(user=True)


def dequeue(url):
    """
    Removes all instances of the input job from user's crontab.
    For a quick primer on cronjob syntax, check the Job class.
    
    Args:
        url (str) - the URL that uniquely identifies the CronJob to dequeue.
    
    Returns:
        Nothing.
    """
    cron.remove(comment='dlq', command='wget {}'.format(url))


def print_job(url):
    """
    Prints a specific dlq job, uniquely identified by url.

    Args:
        url (str) - the URL that uniquely identifies the CronJob to print.
    """
    for job in cron:
        if job.command == 'wget {}'.format(url):
            print(job)


def print_all():
    """
    Prints all dlq-related cronjobs.
    """
    for job in cron:
        if job[0:3] == 'dlq':
            print(job)
