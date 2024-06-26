# This will become a command line tool that will run in the current directory and will output the commit message of the current changes
from diff import git_diff
import click


@click.command()
def main():
    diff = git_diff()
    if diff:
        click.echo(diff)
    else:
        click.echo("No changes to commit")


if __name__ == "__main__":
    main()
