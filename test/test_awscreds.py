import pytest
from click.testing import CliRunner
from awscreds import update_aws_credentials


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
        result = runner.invoke(update_aws_credentials, ['--profile', profile], input=clipboard_content)

        assert result.exit_code == 0
        assert f"Profile '{profile}' atualizado com sucesso!" not in result.output


def test_update_aws_credentials_invalid_json(runner):
    clipboard_content = 'not a valid json'
    profile = 'my_profile'

    with runner.isolated_filesystem():
        result = runner.invoke(update_aws_credentials, ['--profile', profile], input=clipboard_content)

        assert result.exit_code == 0
        assert 'Conteúdo do clipboard não é um JSON válido.' in result.output
