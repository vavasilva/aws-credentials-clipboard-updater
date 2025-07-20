class AwsCredentialsClipboardUpdater < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to manage AWS credentials from clipboard or data"
  homepage "https://github.com/vavasilva/aws-credentials-clipboard-updater"
  url "https://github.com/vavasilva/aws-credentials-clipboard-updater/archive/v1.0.2.tar.gz"
  sha256 "0da7b2942fc429f29f52e09811e8f44ade19572bbd7adf3eebeb034b2c3b25b5"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "Usage:", shell_output("#{bin}/awscreds --help")
  end
end