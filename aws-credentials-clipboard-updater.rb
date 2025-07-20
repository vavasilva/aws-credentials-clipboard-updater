class AwsCredentialsClipboardUpdater < Formula
  include Language::Python::Virtualenv

  desc "CLI tool to manage AWS credentials from clipboard or data"
  homepage "https://github.com/vavasilva/aws-credentials-clipboard-updater"
  url "https://github.com/vavasilva/aws-credentials-clipboard-updater/archive/v1.0.1.tar.gz"
  sha256 "fe721211ccdca69c55c2ce28836c503e2fdb8946583ed7e88472f205cb0a3dfa"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "Usage:", shell_output("#{bin}/awscreds --help")
  end
end