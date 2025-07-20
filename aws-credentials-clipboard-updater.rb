class AwsCredentialsClipboardUpdater < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to manage AWS credentials from clipboard or data"
  homepage "https://github.com/vavasilva/aws-credentials-clipboard-updater"
  url "https://github.com/vavasilva/aws-credentials-clipboard-updater/archive/v1.0.tar.gz"
  sha256 "ed791192ab756f76a364e1cf979e66ca4c8837c5196f6dece105c6db47c0b04e"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "Usage:", shell_output("#{bin}/awscreds --help")
  end
end