import pytest
import os
import configparser
from click.testing import CliRunner
from awscreds import update_aws_credentials


@pytest.fixture
def runner():
    return CliRunner()


def test_update_aws_credentials(runner):
    clipboard_content = """
    {
        "aws_account": "arn:aws:iam::XXXXXX:role/poweruser",
        "aws_access_key_id": "88888",
        "aws_secret_access_key": "99999",
        "aws_session_token": "999",
        "aws_session_expiration": "17/05/2023 17:29:13"
    }
    """

    profile = "test_profile"

    temp_credentials_path = "/tmp/temp_credentials"
    with open(temp_credentials_path, "w") as temp_file:
        temp_file.write("[default]\n")

    os.environ["HOME"] = "/tmp"
    os.environ["AWS_SHARED_CREDENTIALS_FILE"] = temp_credentials_path

    result = runner.invoke(update_aws_credentials, ["--profile", profile], input=clipboard_content)

    assert result.exit_code == 0
    assert f"Profile '{profile}' atualizado com sucesso!" in result.output

    config = configparser.ConfigParser()
    config.read(temp_credentials_path)
    assert config.has_section(profile)
    assert config.get(profile, "aws_access_key_id") == "88888"
    assert config.get(profile, "aws_secret_access_key") == "99999"
    assert config.get(profile, "aws_session_token") == "999"

    os.remove(temp_credentials_path)
