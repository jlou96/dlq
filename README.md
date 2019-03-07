# dlq

**dlq**, short for *download queue*, is a command-line utility that schedules downloads, built upon `wget` and [Python Crontab](https://gitlab.com/doctormo/python-crontab/).

# Installation

todo

# Documentation

## Commands

**dlq** accepts three basic commands: enqueue, dequeue, and list.

### Enqueue

Description: Enqueues a job into the queue.

Alias: `e`

Arguments:

 - `url`: The URL from which to download.
 - `--priority (-p)`: A number denoting the priority of this job. The lower the value, the earlier **dlq** will execute it.
 - `--start <TIME>`: The time at which to start the download. Must be given in 24-hour format.
 - `--stop <TIME>`: The time at which to stop the download. Must be given in 24-hour format.
 - `--dest (-d)`: The directory to which the download is saved. Defaults to `$HOME/Downloads`.

The flags `--start`, `--stop`, and `--dest` can be configured to take a default value in a configuration file. In the case that both exist, the arguments passed through the command line will be used.

Examples:
```
$ dlq enqueue <URL> --priority 2 --start 04:00 --stop 07:30 --dest '~/Pictures'
$ dlq e <URL> -p 2 --start 04:00 --stop 07:30 -d '~/Pictures'
$ dlq e <URL>
```

### Dequeue

Description: Dequeues a job from the queue.

Alias: `d`

Parameters:

 - `url`: The URL that identifies the job dequeue.

Examples:
```
$ dlq dequeue <URL>
$ dlq d <URL>
```

### List

Prints the all current jobs to console.

Alias: `l`

Examples:
```
$ dlq list
$ dlq l
```

## Configuration

**dlq** checks for a configuration file named `dlq.conf` in `$HOME/.config/dlq/`.
A template can be found in the project directory.

