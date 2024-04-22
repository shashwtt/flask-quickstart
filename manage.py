import click
from app.models import auth_models
from app import create_app, db

@click.group()
def cli():
    pass


@click.command()
@click.option(
    '--env', default='development',
    help='Environment to use while running server',
    type=click.STRING
)
@click.option(
    '--port', default=5000,
    help='Port to use while running server',
    type=click.STRING
)
def runserver(env, port):
    app = create_app(env)
    app.run(port=port)
    app.debug = True

@click.command()
def initdb():
    db.create_all()


# Register commands here
cli.add_command(runserver)
cli.add_command(initdb)

if __name__ == "__main__":
    cli()
