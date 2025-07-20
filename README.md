# AWS Credentials Clipboard Updater

A command-line utility to manage AWS credentials. Update, list, or delete profiles in your AWS credentials file efficiently.

## Installation

### Homebrew (macOS/Linux)

```shell
brew tap vavasilva/tap
brew install aws-credentials-clipboard-updater
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

## Usage

### Update AWS Profile

Update a profile with explicit data:

```shell
awscreds update --profile my_profile --data '{"aws_access_key_id": "123", "aws_secret_access_key": "456", "aws_session_token": "789"}'
```

Or read from clipboard:

```shell
awscreds update --profile my_profile
```

### List Profiles

List all configured profiles:

```shell
awscreds list
```

### Delete Profile

Delete a specific profile:

```shell
awscreds delete
```

## Contributing

Contributions welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/vavasilva/aws-credentials-clipboard-updater).
