import click

import log_generator


@click.command()
@click.option('--count', default=100000, help='Number of logs.')
def generate_logs(count):
    """Simple program that generates random logs"""
    generator = log_generator.LogGenerator(count)
    for log in generator:
        print(log, flush=True)


if __name__ == '__main__':
    generate_logs()
