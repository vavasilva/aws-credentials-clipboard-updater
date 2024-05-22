import click
import json
import configparser
import os
import pyperclip


@click.group()
def cli():
    pass


@cli.command()
@click.option('--profile', prompt='Digite o nome do profile que deseja alterar',
              help='Nome do profile AWS que você deseja atualizar.')
@click.option('--data', help='Insira os dados das credenciais em formato JSON.', default=None)
def update(profile, data):
    try:
        if not data:
            data = pyperclip.paste()

        raw_credentials = json.loads(data)

        if 'Credentials' in raw_credentials:
            credentials = raw_credentials['Credentials']
        else:
            credentials = raw_credentials

        aws_credentials_path = os.path.expanduser('~/.aws/credentials')
        config = configparser.ConfigParser()
        config.read(aws_credentials_path)

        if not config.has_section(profile):
            config.add_section(profile)

        access_key = credentials['AccessKeyId'] if 'AccessKeyId' in credentials else credentials['aws_access_key_id']
        secret_key = credentials['SecretAccessKey'] if 'SecretAccessKey' in credentials else credentials[
            'aws_secret_access_key']
        session_token = credentials.get('SessionToken', credentials.get('aws_session_token'))

        config.set(profile, 'aws_access_key_id', access_key)
        config.set(profile, 'aws_secret_access_key', secret_key)

        if session_token:
            config.set(profile, 'aws_session_token', session_token)

        with open(aws_credentials_path, 'w') as configfile:
            config.write(configfile)

        click.echo(f"Profile '{profile}' atualizado com sucesso!")

    except json.JSONDecodeError:
        click.echo('Conteúdo do data não é um JSON válido.')
    except KeyError:
        click.echo('O JSON do data não contém todas as chaves necessárias (AccessKeyId ou SecretAccessKey).')


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


if __name__ == '__main__':
    cli()
