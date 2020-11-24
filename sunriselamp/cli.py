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
    Run test sequences.
    """
    backend.test()


@cli.command()
@click.argument("angle", type=click.FLOAT)
def set(angle):
    """
    Set a color.
    """
    pos = angle * 0.708333
    print(angle, pos)
    backend.set(pos)


if __name__ == "__main__":
    cli()
