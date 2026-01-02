import json

import pytest
from click.testing import CliRunner
from awscreds import update, delete, list


@pytest.fixture
def runner():
    return CliRunner()


def test_update_aws_credentials(runner):
    clipboard_content = '''
    {
        "aws_account": "arn:aws:iam::XXXXXX:role/poweruser",
        "aws_access_key_id": "88888",
        "aws_secret_access_key": "99999",
        "aws_session_token": "999",
        "aws_session_expiration": "17/05/2023 17:29:13"
    }
    '''
    profile = 'my_profile'

    with runner.isolated_filesystem():
        result = runner.invoke(update, ['--profile', profile], input=clipboard_content)

        assert result.exit_code == 0
        assert f"Profile '{profile}' atualizado com sucesso!" not in result.output


def test_list_aws_credentials(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(list)

        assert result.exit_code == 0


def test_delete_aws_credential(runner):
    profile = 'test_profile'
    with runner.isolated_filesystem():
        result = runner.invoke(update, ['--profile', profile, '--data', json.dumps({
            "aws_access_key_id": "88888",
            "aws_secret_access_key": "99999",
            "aws_session_token": "999",
        })])

        assert result.exit_code == 0
        assert f"Profile '{profile}' atualizado com sucesso!" in result.output

        result = runner.invoke(delete, ['--profile', profile])

        assert result.exit_code == 0
        assert f"Profile '{profile}' deletado com sucesso!" in result.output

        result = runner.invoke(delete, ['--profile', profile])

        assert result.exit_code == 0
        assert f"Profile '{profile}' não encontrado." in result.output


def test_update_aws_credentials_invalid_json(runner):
    clipboard_content = 'not a valid json or ini'
    profile = 'my_profile'

    with runner.isolated_filesystem():
        result = runner.invoke(update, ['--profile', profile, '--data', clipboard_content])

        assert result.exit_code == 0
        assert 'Conteúdo do data não é um JSON ou INI válido.' in result.output


def test_update_aws_credentials_ini_format(runner):
    ini_content = '''[994528329112_poweruser]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_session_token=FwoGZXIvYXdzEBYaDH'''
    profile = 'test_ini_profile'

    with runner.isolated_filesystem():
        result = runner.invoke(update, ['--profile', profile, '--data', ini_content])

        assert result.exit_code == 0
        assert f"Profile '{profile}' atualizado com sucesso!" in result.output


def test_update_aws_credentials_ini_format_without_token(runner):
    ini_content = '''[my_profile]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'''
    profile = 'test_ini_no_token'

    with runner.isolated_filesystem():
        result = runner.invoke(update, ['--profile', profile, '--data', ini_content])

        assert result.exit_code == 0
        assert f"Profile '{profile}' atualizado com sucesso!" in result.output
