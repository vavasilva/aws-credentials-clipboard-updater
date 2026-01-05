import click
import json
import configparser
import os
import subprocess
import platform
import sys


def get_clipboard():
    """Get clipboard content using native OS commands."""
    system = platform.system()

    if system == 'Darwin':  # macOS
        result = subprocess.run(['pbpaste'], capture_output=True, text=True)
        return result.stdout
    elif system == 'Linux':
        # Try xclip first, then xsel
        try:
            result = subprocess.run(
                ['xclip', '-selection', 'clipboard', '-o'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return result.stdout
        except FileNotFoundError:
            pass
        try:
            result = subprocess.run(
                ['xsel', '--clipboard', '--output'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return result.stdout
        except FileNotFoundError:
            pass
        raise RuntimeError('xclip or xsel required on Linux. Install with: sudo apt install xclip')
    elif system == 'Windows':
        result = subprocess.run(
            ['powershell', '-command', 'Get-Clipboard'],
            capture_output=True, text=True
        )
        return result.stdout
    else:
        raise RuntimeError(f'Unsupported OS: {system}')


def parse_ini_credentials(data):
    """Parse credentials from INI format string."""
    config = configparser.ConfigParser()
    config.read_string(data)
    sections = config.sections()
    if not sections:
        raise ValueError("No sections found in INI data")
    section = sections[0]
    return {
        'aws_access_key_id': config.get(section, 'aws_access_key_id'),
        'aws_secret_access_key': config.get(section, 'aws_secret_access_key'),
        'aws_session_token': config.get(section, 'aws_session_token', fallback=None)
    }


@click.group()
def cli():
    pass


@cli.command()
@click.option('--profile', prompt='Enter the profile name to update',
              help='Name of the AWS profile you want to update.')
@click.option('--data', help='Credentials data in JSON or INI format.', default=None)
def update(profile, data):
    try:
        if not data:
            try:
                data = get_clipboard()
            except RuntimeError as e:
                click.echo(f'Error reading clipboard: {e}')
                sys.exit(1)

        credentials = None

        # Try JSON format first
        try:
            raw_credentials = json.loads(data)
            if 'Credentials' in raw_credentials:
                credentials = raw_credentials['Credentials']
            else:
                credentials = raw_credentials
        except json.JSONDecodeError:
            # Try INI format
            try:
                credentials = parse_ini_credentials(data)
            except (configparser.Error, ValueError, KeyError):
                click.echo('Invalid JSON or INI format.')
                sys.exit(1)

        aws_credentials_path = os.path.expanduser('~/.aws/credentials')
        config = configparser.ConfigParser()
        config.read(aws_credentials_path)

        if not config.has_section(profile):
            config.add_section(profile)

        access_key = credentials.get('AccessKeyId') or credentials.get('aws_access_key_id')
        secret_key = credentials.get('SecretAccessKey') or credentials.get('aws_secret_access_key')
        session_token = credentials.get('SessionToken') or credentials.get('aws_session_token')

        if not access_key or not secret_key:
            click.echo('Missing required keys (AccessKeyId/aws_access_key_id or SecretAccessKey/aws_secret_access_key).')
            sys.exit(1)

        config.set(profile, 'aws_access_key_id', access_key)
        config.set(profile, 'aws_secret_access_key', secret_key)

        if session_token:
            config.set(profile, 'aws_session_token', session_token)

        with open(aws_credentials_path, 'w') as configfile:
            config.write(configfile)

        click.echo(f"Profile '{profile}' updated successfully!")

    except KeyError:
        click.echo('Missing required keys (AccessKeyId/aws_access_key_id or SecretAccessKey/aws_secret_access_key).')
        sys.exit(1)


@cli.command()
def list():
    aws_credentials_path = os.path.expanduser('~/.aws/credentials')
    config = configparser.ConfigParser()
    config.read(aws_credentials_path)

    profiles = config.sections()
    click.echo("Existing profiles:")
    for profile in profiles:
        click.echo(profile)


@cli.command()
@click.option('--profile', prompt='Enter the profile name to delete',
              help='Name of the AWS profile you want to delete.')
def delete(profile):
    aws_credentials_path = os.path.expanduser('~/.aws/credentials')
    config = configparser.ConfigParser()
    config.read(aws_credentials_path)

    if config.has_section(profile):
        config.remove_section(profile)
        with open(aws_credentials_path, 'w') as configfile:
            config.write(configfile)
        click.echo(f"Profile '{profile}' deleted successfully!")
    else:
        click.echo(f"Profile '{profile}' not found.")
        sys.exit(1)


def main():
    cli()


if __name__ == '__main__':
    main()