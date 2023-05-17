import click
import pyperclip
import json
import configparser
import os


@click.command()
@click.option('--profile', prompt='Digite o nome do profile que deseja alterar',
              help='Nome do profile AWS que você deseja atualizar.')
def update_aws_credentials(profile):
    clipboard_content = pyperclip.paste()

    try:

        data = json.loads(clipboard_content)

        aws_credentials_path = os.path.expanduser('~/.aws/credentials')
        config = configparser.ConfigParser()
        config.read(aws_credentials_path)

        if not config.has_section(profile):
            config.add_section(profile)

        config.set(profile, 'aws_access_key_id', data['aws_access_key_id'])
        config.set(profile, 'aws_secret_access_key', data['aws_secret_access_key'])
        config.set(profile, 'aws_session_token', data['aws_session_token'])

        with open(aws_credentials_path, 'w') as configfile:
            config.write(configfile)

        click.echo(f"Profile '{profile}' atualizado com sucesso!")

    except json.JSONDecodeError:
        click.echo('Conteúdo do clipboard não é um JSON válido.')
    except KeyError:
        click.echo('O JSON do clipboard não contém todas as chaves necessárias.')


if __name__ == '__main__':
    update_aws_credentials()
