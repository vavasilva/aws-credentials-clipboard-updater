# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A CLI tool for managing AWS credentials profiles. Updates `~/.aws/credentials` by reading JSON data from clipboard or `--data` argument. Supports both AWS STS response format (`AccessKeyId`, `SecretAccessKey`, `SessionToken`) and snake_case format (`aws_access_key_id`, etc.).

## Development Commands

```shell
# Install in development mode
pip install -e .

# Run tests
pytest test/

# Run a single test
pytest test/test_awscreds.py::test_update_aws_credentials

# Build distribution
python -m build
```

## Architecture

- **Entry point**: `awscreds` command (defined in `pyproject.toml` and `setup.py`)
- **Main CLI**: `src/awscreds/cli.py` - Click-based CLI with three commands: `update`, `list`, `delete`
- **Module export**: `src/awscreds/__init__.py` exports `main()` from cli.py

The tool reads/writes directly to `~/.aws/credentials` using Python's `configparser`. Clipboard access uses `pyperclip`.

## Dependencies

- `click` - CLI framework
- `pyperclip` - Clipboard access
- `pytest` - Testing (dev only)
