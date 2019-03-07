# dlq

dlq, short for *download queue*, is a command-line utility that schedules downloads, built upon wget and [Python Crontab](https://gitlab.com/doctormo/python-crontab/).

# Installation

todo

# Documentation

## Commands

dlq accepts three basic commands: `enqueue`, `dequeue`, and `print`.

### Enqueue

Description: Enqueues a job into the queue.

Alias: `e`

Arguments:

 - `url`: The URL from which to download.
 - `--start <TIME>`: The time at which to start the download. Must be given in 24-hour format.
 - `--stop <TIME>`: The time at which to stop the download. Must be given in 24-hour format.
 - `--dest (-d)`: The directory to which the download is saved. Defaults to `$HOME/Downloads`.

The flags `--start`, `--stop`, and `--dest` can be configured to take a default value in a configuration file. In the case that both exist, the arguments passed through the command line will be used.

Examples:
```
$ dlq enqueue <URL> --start 04:00 --stop 07:30 --dest '~/Pictures'
$ dlq e <URL> --start 04:00 --stop 07:30 -d '~/Pictures'
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

### Print

Description: Prints jobs to console.

Alias: `p`

Parameters:

 - `url`: The URL that identifies the job to print.
 - `--all (-a)`: A flag that causes all enqueued jobs to be printed.

Examples:
```
$ dlq print <URL>
$ dlq p <URL>
$ dlq p -a
```

## Configuration

dlq checks for a configuration file named `dlq.conf` in `$HOME/.config/dlq/`.
A template can be found in the project directory.
