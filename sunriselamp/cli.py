import click
from sunriselamp import backend
from sunriselamp import morning_sequence


@click.group()
def cli():
    pass


@cli.command()
def sunrise():
    """
    Sunrise sequence.
    """
    morning_sequence.run()


@cli.command()
def off():
    """
    Turn off lamp.
    """
    backend.off()


@cli.command()
def test():
    """
    Run test sequences
    """
    backend.test()
