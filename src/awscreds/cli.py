import click
import json
import configparser
import os
import subprocess
import platform


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
@click.option('--profile', prompt='Digite o nome do profile que deseja alterar',
              help='Nome do profile AWS que você deseja atualizar.')
@click.option('--data', help='Insira os dados das credenciais em formato JSON ou INI.', default=None)
def update(profile, data):
    try:
        if not data:
            data = get_clipboard()

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
                click.echo('Conteúdo do data não é um JSON ou INI válido.')
                return

        aws_credentials_path = os.path.expanduser('~/.aws/credentials')
        config = configparser.ConfigParser()
        config.read(aws_credentials_path)

        if not config.has_section(profile):
            config.add_section(profile)

        access_key = credentials.get('AccessKeyId') or credentials.get('aws_access_key_id')
        secret_key = credentials.get('SecretAccessKey') or credentials.get('aws_secret_access_key')
        session_token = credentials.get('SessionToken') or credentials.get('aws_session_token')

        if not access_key or not secret_key:
            click.echo('O data não contém todas as chaves necessárias (AccessKeyId/aws_access_key_id ou SecretAccessKey/aws_secret_access_key).')
            return

        config.set(profile, 'aws_access_key_id', access_key)
        config.set(profile, 'aws_secret_access_key', secret_key)

        if session_token:
            config.set(profile, 'aws_session_token', session_token)

        with open(aws_credentials_path, 'w') as configfile:
            config.write(configfile)

        click.echo(f"Profile '{profile}' atualizado com sucesso!")

    except KeyError:
        click.echo('O data não contém todas as chaves necessárias (AccessKeyId/aws_access_key_id ou SecretAccessKey/aws_secret_access_key).')


@cli.command()
def list():
    aws_credentials_path = os.path.expanduser('~/.aws/credentials')
    config = configparser.ConfigParser()
    config.read(aws_credentials_path)

    profiles = config.sections()
    click.echo("Profiles existentes:")
    for profile in profiles:
        click.echo(profile)


@cli.command()
@click.option('--profile', prompt='Digite o nome do profile que deseja deletar',
              help='Nome do profile AWS que você deseja deletar.')
def delete(profile):
    aws_credentials_path = os.path.expanduser('~/.aws/credentials')
    config = configparser.ConfigParser()
    config.read(aws_credentials_path)

    if config.has_section(profile):
        config.remove_section(profile)
        with open(aws_credentials_path, 'w') as configfile:
            config.write(configfile)
        click.echo(f"Profile '{profile}' deletado com sucesso!")
    else:
        click.echo(f"Profile '{profile}' não encontrado.")


def main():
    cli()


if __name__ == '__main__':
    main()