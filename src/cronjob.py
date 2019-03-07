class CronJob:
    """
    A cronjob to be queued in the user's crontab.

    ###########################################################################
    A quick primer on cronjob syntax:

    Given the following arguments:

        [MM] - (0-59) - Minute
        [HH] - (0-23) - Hour
        [DM] - (1-31) - Day of the Month
        [MY] - (1-12) - Month of the Year
        [DW] - (0-7)  - Day of the Week, where 0 and 7 are Sunday.

    Crontabs take the form

        [MM] [HH] [DM] [MY] [DW] [Command]

    For example, to call '~/scripts/foo.sh' on Tuesday, Jan 21, 2020 at 20:50,
    schedule the crontab

        50 20 21 1 2 ~/scripts/foo.sh
    ###########################################################################
    """

    def __init__(self, minute, hour, date, month, day, command):
        self._minute = minute
        self._hour = hour
        self._date = date
        self._month = month
        self._day = day
        self._command = command


    @property
    def minute(self):
        return self._minute


    @property
    def hour(self):
        return self._hour


    @property
    def date(self):
        return self._date


    @property
    def month(self):
        return self._month


    @property
    def day(self):
        return self._day


    @property
    def command(self):
        return self._command
