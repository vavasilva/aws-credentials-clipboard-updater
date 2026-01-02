# AWS Credentials Clipboard Updater

A command-line utility to manage AWS credentials. Update, list, or delete profiles in your AWS credentials file efficiently.

## Installation

### Homebrew (macOS/Linux)

```shell
brew tap vavasilva/tap
brew install aws-credentials-clipboard-updater
```

### pip (Global)

```shell
pip install git+https://github.com/vavasilva/aws-credentials-clipboard-updater.git
```

### From Source

#### Prerequisites
- Python 3.7 or higher
- Virtual environment recommended

#### Steps

1. Clone the repository:
```shell
git clone https://github.com/vavasilva/aws-credentials-clipboard-updater.git
cd aws-credentials-clipboard-updater
```

2. Install:
```shell
pip install -e .
```

### System Dependencies

For clipboard functionality on Linux systems:

- **Debian/Ubuntu**: `sudo apt-get install xclip xsel`
- **Fedora**: `sudo dnf install xclip xsel`
- **Arch**: `sudo pacman -S xclip xsel`

## Supported Formats

The tool accepts credentials in multiple formats:

### AWS STS Response (JSON)

Direct output from `aws sts assume-role` or similar commands:

```json
{
  "Credentials": {
    "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "SessionToken": "AQoDYXdzEJr..."
  }
}
```

### Simple JSON (PascalCase)

```json
{
  "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
  "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "SessionToken": "AQoDYXdzEJr..."
}
```

### Simple JSON (snake_case)

```json
{
  "aws_access_key_id": "AKIAIOSFODNN7EXAMPLE",
  "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "aws_session_token": "AQoDYXdzEJr..."
}
```

### INI Format

```ini
[profile_name]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_session_token = AQoDYXdzEJr...
```

> **Note:** `SessionToken`/`aws_session_token` is optional for permanent credentials.

## Usage

### Update AWS Profile

**From clipboard** (copy credentials first, then run):

```shell
awscreds update --profile my_profile
```

**With explicit data:**

```shell
awscreds update --profile my_profile --data '{"AccessKeyId": "AKIA...", "SecretAccessKey": "secret...", "SessionToken": "token..."}'
```

### List Profiles

```shell
awscreds list
```

### Delete Profile

```shell
awscreds delete --profile my_profile
```

## Examples

### Example 1: Update profile from AWS STS assume-role

```shell
# Copy the output from AWS CLI to clipboard
aws sts assume-role --role-arn arn:aws:iam::123456789:role/MyRole --role-session-name session1 | pbcopy

# Update profile
awscreds update --profile dev
```

### Example 2: Quick update with inline JSON

```shell
awscreds update --profile prod --data '{
  "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
  "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}'
```

### Example 3: Update from SSO/Identity Center portal

1. Copy credentials from AWS SSO portal (usually in INI format)
2. Run:
```shell
awscreds update --profile sso-dev
```

## Contributing

Contributions welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/vavasilva/aws-credentials-clipboard-updater).